import pytest


@pytest.mark.positive
def test_api_positive():
    assert True


@pytest.mark.negative
def test_api_negative():
    assert False
