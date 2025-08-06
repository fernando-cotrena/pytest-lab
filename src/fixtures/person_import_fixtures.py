import pytest

@pytest.fixture
def valid_person_id():
    return 123

@pytest.fixture
def invalid_person_id():
    return 9999