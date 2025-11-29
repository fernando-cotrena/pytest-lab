from api_clients.base_client import BaseClient


class BookingClient(BaseClient):

    def __init__(self, token: str | None = None):
        super().__init__(token=token)

    def get_booking(self, booking_id: int):
        return self.get(f"/booking/{booking_id}")

    def create_booking(self, booking_data: dict):
        return self.post("/booking", json=booking_data)
