import pytest
from contextlib import nullcontext as does_not_raise

from src.main import *

def test_plus():
    x = 10
    y = 20
    assert plus(x, y) == 30

def test_minus():
    x = 10
    y = 10
    assert minus(x, y) == 0

@pytest.mark.parametrize(
        'x, y, res, expectation',
         [
           (10, 2, 5, does_not_raise()),
            (-100, '2', -50, pytest.raises(TypeError)),
            (100, 0, 100, pytest.raises(ZeroDivisionError)) 
         ]                                 
        )
def test_div(x, y, res, expectation):
    with expectation:
        assert div(x, y) == res