import pytest
from person import Person

# Test constants
INITIAL_NAME = "John"
INITIAL_AGE = 30
INITIAL_HEIGHT = 1.75

UPDATED_NAME = "Mike"
UPDATED_AGE = 35
UPDATED_HEIGHT = 1.80

@pytest.fixture
def person():
    return Person(INITIAL_NAME, INITIAL_AGE, INITIAL_HEIGHT)

def test_getters(person):
    assert person.getName() == INITIAL_NAME
    assert person.getAge() == INITIAL_AGE
    assert person.getHeight() == INITIAL_HEIGHT

def test_setters(person):
    person.setName(UPDATED_NAME)
    person.setAge(UPDATED_AGE)
    person.setHeight(UPDATED_HEIGHT)
    assert person.getName() == UPDATED_NAME
    assert person.getAge() == UPDATED_AGE
    assert person.getHeight() == UPDATED_HEIGHT
