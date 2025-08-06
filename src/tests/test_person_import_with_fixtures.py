
from assertpy import assert_that
import pytest
from api_clients.person_import_client import ImportClient
from fixtures.person_import_fixtures import valid_person_id, invalid_person_id

@pytest.fixture
def client(base_url, auth_token):
    return ImportClient(base_url=base_url, token=auth_token)

def test_import_valid_person(client, valid_person_id):
    response = client.import_person(valid_person_id)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.text.lower()).contains("success")


def test_import_invalid_person(client, invalid_person_id):
    response = client.import_person(invalid_person_id)
    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.text.lower()).contains("not found")
