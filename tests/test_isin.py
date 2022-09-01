import pytest

import validate.isin

@pytest.mark.parametrize('val,res', [
    ("5610-0000-0000-0001", True),
    ("US5949181045", True),
    ("US38259P5089", True),  # Google Inc, GGQ1
    ("IE00B4BNMY34", True),  # Accenture
    ("CA986191302", False),
    ])
def test(val, res):
    assert validate.isin.validate_isin(val) == res
