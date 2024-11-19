import pytest


@pytest.mark.positive
def test_ui_positive():
    assert len("Hello") == 5



@pytest.mark.negative
def test_ui_negative():
    assert False
