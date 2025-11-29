import pytest
from api_clients.auth_client import AuthClient


@pytest.fixture(scope="session")
def auth_token():
    return AuthClient().get_token("admin", "password123")
