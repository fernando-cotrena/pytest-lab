from api_clients.booking_client import BookingClient
import requests
from assertpy import assert_that

from api_clients.env import get_base_url
from api_clients.booking_client import BookingClient


def test_get_booking(auth_token):
    booking_client = BookingClient(token=auth_token)
    response = booking_client.get_booking(2)

    assert_that(response.status_code)\
        .described_as("El endpoint debería devolver 200")\
        .is_equal_to(200)
    data = response.json()

    assert_that(data['firstname']).is_equal_to("Susan")


def test_create_booking(auth_token):
    booking_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    booking_client = BookingClient(token=auth_token)

    response = booking_client.create_booking(booking_data)

    assert_that(response.status_code).described_as("La solicitud debería devolver un código 200 para una creación exitosa.")\
        .is_equal_to(200)
