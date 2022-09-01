import pytest

import validate.snils

@pytest.mark.parametrize('val,res', [
    ("076-421-071 50", True),
    ("061-952-784 82", True),
    ("123123123", False),
    ])
def test(val, res):
    assert validate.snils.validate_snils(val) == res
