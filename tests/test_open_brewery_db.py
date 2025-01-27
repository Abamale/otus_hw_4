import pytest
from resources.data import DataTest

class TestOpenBreweryDB:

    BASE_URL = DataTest.OPEN_BREWERY_DB_BASE_URL

    def test_breweries_list(self):
        data = DataTest.get_response(self.BASE_URL)
        assert isinstance(data, list), "Response should be a list"
        for brewery in data:
            assert isinstance(brewery, dict), f"Expected a dictionary, but got {type(brewery)}"

    @pytest.mark.parametrize("city", ["San Diego", "New York", "Denver"])
    def test_breweries_by_city(self, city):
        response = DataTest.get_response(self.BASE_URL, params={"by_city": city})
        data = response.json()

        assert isinstance(data, list), "Response should be a list"
        for brewery in data:
            assert isinstance(brewery, dict), f"Expected a dictionary, but got {type(brewery)}"
            if "city" not in brewery:
                pytest.fail(f"City not found in brewery: {brewery}")
            if brewery["city"] != city:
                pytest.fail(f"City mismatch: Expected {city}, but found {brewery['city']} for brewery: {brewery}")

    def test_search_by_name(self):
        response = DataTest.get_response(self.BASE_URL, params={"query": "dog"})
        data = response.json()

        # Проверка, что ответ не пустой
        assert isinstance(data, list), "Response should be a list"
        assert len(data) > 0, "Expected non-empty list of breweries, but got an empty list"

        # Проверка, что в данных присутствуют слова, связанные с запросом
        assert any("dog" in brewery["name"].lower() for brewery in data), "No brewery names contain 'dog'"

    def test_invalid_state(self):
        response = DataTest.get_response(self.BASE_URL, params={"by_state": "InvalidState"})
        data = response.json()

        # Проверяем, что ответ действительно пустой список
        assert isinstance(data, list), "Response should be a list"
        assert not data, "Expected an empty list, but got data"