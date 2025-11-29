import requests
from api_clients.env import get_base_url


class BaseClient:
    def __init__(self, token: str = None, base_url: str = None):
        self.base_url = base_url or get_base_url()
        self.token = token
        self.token = token
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        })

    def _get_url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def get(self, path: str, **kwargs):
        url = self._get_url(path)
        resp = self._session.get(url, **kwargs)
        resp.raise_for_status()
        return resp

    def post(self, path: str, data=None, json=None, **kwargs):
        url = self._get_url(path)
        resp = self._session.post(url, data=data, json=json, **kwargs)
        resp.raise_for_status()
        return resp
