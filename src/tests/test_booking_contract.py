import requests
from assertpy import assert_that
from jsonschema import validate, ValidationError
from api_clients.booking_client import BookingClient

# Definimos el esquema esperado para la respuesta
booking_schema = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string"},
        "lastname": {"type": "string"},
        "totalprice": {"type": "integer"},
        "depositpaid": {"type": "boolean"},
        "bookingdates": {
            "type": "object",
            "properties": {
                "checkin": {"type": "string", "format": "date"},
                "checkout": {"type": "string", "format": "date"}
            },
            "required": ["checkin", "checkout"]
        },
        "additionalneeds": {"type": "string"}
    },
    "required": ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates", "additionalneeds"]
}


def test_get_booking_contract(auth_token):

    booking_client = BookingClient(token=auth_token)
    response = booking_client.get_booking(booking_id=2)
    assert_that(response.status_code).described_as("La solicitud GET debería devolver un código 200 si la reserva existe.")\
        .is_equal_to(200)

    data = response.json()

    # Validar la respuesta contra el esquema JSON (contrato)
    try:
        validate(instance=data, schema=booking_schema)
    except ValidationError as e:
        assert_that(e.message).described_as(f"El formato de la respuesta no coincide con el esquema. Error: {e.message}")\
            .is_empty()

    # Opcional: Verificar que el tipo de contenido es JSON
    assert_that(response.headers['Content-Type']).contains('application/json')
