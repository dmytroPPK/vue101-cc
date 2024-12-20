import pytest


class Person:
    def __init__(self):
        self.first_name = None
        self.last_name = None

    def autofill_data(self):
        self.first_name = "John"
        self.last_name = "Baton"

    def clean_data(self):
        self.first_name = ""
        self.last_name = ""


@pytest.fixture
def get_person():
    person = Person()
    person.autofill_data()

    yield person

    person.clean_data()
