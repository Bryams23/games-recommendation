import pytest
from sum import substrat


def test_add():
    assert substrat(2, 3) == 5
    assert substrat(-1, 1) == -2
    assert substrat(0, 0) == 0
    assert substrat(1, 3) == -2
