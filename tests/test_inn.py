import pytest

import validate.inn

@pytest.mark.parametrize('val,res', [
    ("500100732259", True),
    ("7830002293", True), # Санкт-Петербургская бумажная фабрика Гознака).
])
def test(val, res):
    assert validate.inn.validate_inn(val) == res
