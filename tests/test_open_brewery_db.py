import pytest
from resources.data import DataTest

class TestOpenBreweryDB:

    BASE_URL = DataTest.OPEN_BREWERY_DB_BASE_URL

    def test_breweries_list(self, responses):
        data = responses["open_brewery_db"]["breweries_list"].json()
        assert isinstance(data, list), "Response should be a list"

    @pytest.mark.parametrize("city", ["San Diego", "New York", "Denver"])
    def test_breweries_by_city(self, city):
        response = DataTest.get_response(self.BASE_URL, params={"by_city": city})
        data = response.json()
        assert all("city" in brewery and brewery["city"] == city for brewery in data), "City mismatch in results"

    def test_search_by_name(self):
        response = DataTest.get_response(self.BASE_URL, params={"query": "dog"})
        data = response.json()
        assert isinstance(data, list), "Response should be a list"

    def test_invalid_state(self):
        response = DataTest.get_response(self.BASE_URL, params={"by_state": "InvalidState"})
        data = response.json()
        assert data == [], "Invalid state should return an empty list"