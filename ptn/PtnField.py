import re
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import CharField
from django.utils.deconstruct import deconstructible
from django.utils.functional import SimpleLazyObject
from django.utils.translation import gettext_lazy as _


def _lazy_re_compile(regex, flags=0):
    """Lazily compile a regex with flags."""
    def _compile():
        # Compile the regex if it was not passed pre-compiled.
        if isinstance(regex, str):
            return re.compile(regex, flags)
        else:
            assert not flags, "flags must be empty if regex is passed pre-compiled"
            return regex
    return SimpleLazyObject(_compile)


@deconstructible
class PtnValidator:
    """
    Check PTN (personal tax number, Russia - ИНН)
    """
    message = _('Enter a PTN.')
    code = 'invalid'
    phone_regex = _lazy_re_compile(
        r"^\+?[\t \-\(\)\d]+$", re.IGNORECASE)

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        val = str(value)
        length = len(val)
        if not(length in [10, 12]):
            raise ValidationError(message="Длина ИНН должна быть 10 или 12 цифр", code="ERR_PTN_LENGTH")
        if not self.phone_regex.match(val):
            raise ValidationError(message="ИНН должен содержать только цифры", code="ERR_PTN_NUMBERSONLY")
        if len(val) == 10:
            weights = [2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
            inn = [a for a in map(int, str(val))]
            control = sum(a*b for a, b in zip(inn, weights)) % 11 % 10
            if control != inn[-1]:
                raise ValidationError(message="Несовпадение контрольной суммы (10)", code="ERR_PTN_CHECKSUM_10")
        if len(val) == 12:
            weights1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
            weights2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
            inn = [a for a in map(int, str(val))]
            control1 = sum(a*b for a, b in zip(inn, weights1)) % 11 % 10
            control2 = sum(a*b for a, b in zip(inn, weights2)) % 11 % 10
            if control1 != inn[-2] or control2 != inn[-1]:
                raise ValidationError(message="Несовпадение контрольной суммы (12)", code="ERR_PTN_CHECKSUM_12")
        return

    def __eq__(self, other):
        return (
            isinstance(other, PtnValidator) and
            (self.message == other.message) and
            (self.code == other.code)
            )

validate_ptn = PtnValidator()


class PtnField(CharField):
    default_validators = [validate_ptn]
    description = _("PTN number")

    def __init__(self, *args, **kwargs):
        # max_length=18 to hold any phone number
        kwargs.setdefault('max_length', 18)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # We do not exclude max_length if it matches default as we want to change
        # the default in future.
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        # As with CharField, this will cause PTN validation to be performed
        # twice.
        return super().formfield(**{
            'form_class': forms.CharField,
            **kwargs,
            })
