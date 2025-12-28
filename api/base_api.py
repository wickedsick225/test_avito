import requests


class BaseAPI:
    BASE_URL = "https://qa-internship.avito.com"

    HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    def get(self, endpoint):
        return requests.get(
            url=f"{self.BASE_URL}{endpoint}",
            headers=self.HEADERS
        )

    def post(self, endpoint, json):
        return requests.post(
            url=f"{self.BASE_URL}{endpoint}",
            json=json,
            headers=self.HEADERS
        )

    def delete(self, endpoint):
        return requests.delete(
            url=f"{self.BASE_URL}{endpoint}",
            headers=self.HEADERS
        )