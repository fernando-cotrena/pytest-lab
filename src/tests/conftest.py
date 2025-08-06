import pytest
from config.settings import get_token, get_base_url

@pytest.fixture(scope="session")
def auth_token():
    return get_token()

@pytest.fixture(scope="session")
def base_url():
    return get_base_url()