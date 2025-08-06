import requests

class ImportClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def import_person(self, person_id: int):
        payload = {"personID": person_id}
        response = requests.post(
            f"{self.base_url}/import",
            json=payload,
            headers=self.headers
        )
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print(response.text)
        print('-----------------------')
        return response
