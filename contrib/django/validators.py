from validate import *
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class InnValidator:
    """
    Check INN (personal tax number, Russia - ИНН)
    """
    message = _('Enter a PTN.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        return validate_inn(value)

    def __eq__(self, other):
        return (
            isinstance(other, InnValidator) and
            (self.message == other.message) and
            (self.code == other.code)
            )


@deconstructible
class SnilsValidator:
    """
    Check SNILS (personal social number in Russia - СНИЛС)
    """
    message = _('Enter a SNILS.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        return validate_snils(value)

    def __eq__(self, other):
        return (
            isinstance(other, SnilsValidator) and
            (self.message == other.message) and
            (self.code == other.code)
            )



@deconstructible
class EanValidator:
    """
    Check ISBN (EAN) (printed entity - book, article or newspaper - id)
    """
    message = _('Enter a EAN.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        return validate_ean(value)

    def __eq__(self, other):
        return (
            isinstance(other, EanValidator) and
            (self.message == other.message) and
            (self.code == other.code)
            )

@deconstructible
class IsbnValidator:
    """
    Check ISBN (printed entity - book, article or newspaper - id) - 8 or 10 symbols
    """
    message = _('Enter a ISBN.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        return validate_isbn(value)

    def __eq__(self, other):
        return (
            isinstance(other, IsbnValidator) and
            (self.message == other.message) and
            (self.code == other.code)
            )

@deconstructible
class IsinValidator:
    """
    Check ISIN (bank card or equity) - up to 16 symbols
    """
    message = _('Enter a ISIN.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        return validate_isin(value)

    def __eq__(self, other):
        return (
            isinstance(other, IsinValidator) and
            (self.message == other.message) and
            (self.code == other.code)
            )


inn_validator = InnValidator()
snils_validator = SnilsValidator()
ean_validator = EanValidator()
isin_validator = IsinValidator()
isbn_validator = IsbnValidator()
