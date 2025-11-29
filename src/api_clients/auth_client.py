import requests
from api_clients.env import get_base_url

class AuthClient:
    
    def __init__(self):
        self.base_url = get_base_url()
    def get_token(self, username: str = "admin", password: str = "password123") -> str:
        url = f"{self.base_url}/auth"
       
        resp = requests.post(url, json={
            "username": username,
            "password": password
        }, headers={"Content-Type": "application/json"})
        
        resp.raise_for_status()

        data = resp.json()
        token = data.get("token")

        if not token:
            raise ValueError(f"No se obtuvo token: {data}")
        return token
