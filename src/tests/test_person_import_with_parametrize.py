import pytest
from assertpy import assert_that
from api_clients.person_import_client import ImportClient

@pytest.fixture
def client(base_url, auth_token):
    return ImportClient(base_url=base_url, token=auth_token)
    

@pytest.mark.parametrize("person_id, expected_status, expected_msg", [
    (123, 200, "success"),
    (9999, 404, "not found"),
])
def test_import_person(client, person_id, expected_status, expected_msg):
    response = client.import_person(person_id)

    assert_that(response.status_code).is_equal_to(expected_status)
    assert_that(response.text.lower()).contains(expected_msg)