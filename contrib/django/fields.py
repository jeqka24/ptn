from django import forms
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from validators import *


class InnField(CharField):
    default_validators = [inn_validator]
    description = _("Номер ИНН")

    def __init__(self, *args, **kwargs):
        # max_length=13 to hold any INN number
        kwargs.setdefault('max_length', 13)
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


class SnilsField(CharField):
    default_validators = [snils_validator]
    description = _("Номер СНИЛС")

    def __init__(self, *args, **kwargs):
        # max_length=13 to hold any SNILS number
        kwargs.setdefault('max_length', 13)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # We do not exclude max_length if it matches default as we want to change
        # the default in future.
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        # As with CharField, this will cause SNILS validation to be performed
        # twice.
        return super().formfield(**{
            'form_class': forms.CharField,
            **kwargs,
            })


class EanField(CharField):
    default_validators = [ean_validator]
    description = _("Номер EAN-13")

    def __init__(self, *args, **kwargs):
        # max_length=13 to hold any EAN number
        kwargs.setdefault('max_length', 13)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # We do not exclude max_length if it matches default as we want to change
        # the default in future.
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        # As with CharField, this will cause EAN validation to be performed
        # twice.
        return super().formfield(**{
            'form_class': forms.CharField,
            **kwargs,
            })


class IsbnField(CharField):
    default_validators = [isbn_validator]
    description = _("Номер ISBN")

    def __init__(self, *args, **kwargs):
        # max_length=10 to hold  ISBN number
        kwargs.setdefault('max_length', 10)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # We do not exclude max_length if it matches default as we want to change
        # the default in future.
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        # As with CharField, this will cause ISBN validation to be performed
        # twice.
        return super().formfield(**{
            'form_class': forms.CharField,
            **kwargs,
            })


class IsinField(CharField):
    default_validators = [isin_validator]
    description = _("Номер ISIN")

    def __init__(self, *args, **kwargs):
        # max_length=13 to hold any ISIN number
        kwargs.setdefault('max_length', 16)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # We do not exclude max_length if it matches default as we want to change
        # the default in future.
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        # As with CharField, this will cause ISIN validation to be performed
        # twice.
        return super().formfield(**{
            'form_class': forms.CharField,
            **kwargs,
            })
