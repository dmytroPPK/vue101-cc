import pytest


@pytest.mark.person_attr
def test_user_first_name(get_person):
    assert get_person.first_name == "John"


@pytest.mark.person_attr
def test_user_last_name(get_person):
    assert get_person.last_name == "Baton"
