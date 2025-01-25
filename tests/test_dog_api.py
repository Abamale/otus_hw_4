import pytest
from resources.data import DataTest

class TestDogAPI:

    BASE_URL = DataTest.DOG_API_BASE_URL

    @pytest.mark.parametrize("endpoint", [
        "/breeds/list/all",
        "/breeds/image/random",
    ])
    def test_endpoints_status(self, endpoint):
        response = DataTest.get_response(self.BASE_URL + endpoint)
        assert response.ok, f"Endpoint {endpoint} failed"

    def test_breed_list_structure(self, responses):
        data = responses["dog_api"]["breed_list"].json()
        assert "message" in data and isinstance(data["message"], dict), "Invalid structure for breed list"

    @pytest.mark.parametrize("breed", ["hound", "retriever", "terrier"])
    def test_random_image_by_breed(self, breed):
        response = DataTest.get_response(f"{self.BASE_URL}/breed/{breed}/images/random")
        data = response.json()
        assert "message" in data and data["message"].startswith("https://"), "Invalid image URL"

    def test_random_image(self, responses):
        data = responses["dog_api"]["random_image"].json()
        assert "message" in data and data["message"].startswith("https://"), "Invalid image URL"