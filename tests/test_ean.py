import pytest

import validate.ean

@pytest.mark.parametrize('val,res', [
    ('978-0-306-40615-7', True),
    ])
def test(val, res):
    assert validate.ean.validate_ean(val) == res