import pytest

import validate.isbn

@pytest.mark.parametrize('val,res', [
    ("5-93286-005-7", True), # Ф. Брукс. «Мифический человеко-месяц», СПб, Символ, 2000 г.
    ("0-446-52087-X", True), # E. Gordeeva. «My Sergei», A Time Warner Company
    ("0033-765X", True), # ISSN, журнал — «Радио», 2-2006
    ("2-266-11156-6", True),  # Accenture
    ])
def test(val, res):
    assert validate.isbn.validate_isbn(val) == res
