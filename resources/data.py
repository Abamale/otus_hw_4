import requests


class DataTest:
    DOG_API_BASE_URL = "https://dog.ceo/api"
    OPEN_BREWERY_DB_BASE_URL = "https://api.openbrewerydb.org/breweries"
    JSON_PLACEHOLDER_BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_response(url, params=None):
        response = requests.get(url, params=params)
        assert response.ok, f"Request to {url} failed with status code {response.status_code}"
        return response.json()  # Возвращаем сразу JSON