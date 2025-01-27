import pytest
from resources.data import DataTest

class TestDogAPI:

    BASE_URL = DataTest.DOG_API_BASE_URL

    @pytest.mark.parametrize("endpoint", [
        ("/breeds/list/all"),
        ("/breeds/image/random"),
    ])
    def test_endpoints_status(self, endpoint):
        data = DataTest.get_response(self.BASE_URL + endpoint)
        assert data, f"Endpoint {endpoint} failed"

    def test_breed_list_structure(self):
        data = DataTest.get_response(f"{self.BASE_URL}/breeds/list/all")
        assert "message" in data and isinstance(data["message"], dict), "Invalid structure for breed list"

    @pytest.mark.parametrize("breed", ["hound", "retriever", "terrier"])
    def test_random_image_by_breed(self, breed):
        data = DataTest.get_response(f"{self.BASE_URL}/breed/{breed}/images/random")
        assert "message" in data and data["message"].startswith("https://"), "Invalid image URL"
        assert f"{breed}" in data["message"], "Breed mismatch in the returned image URL"

    def test_random_image(self):
        data = DataTest.get_response(f"{self.BASE_URL}/breeds/image/random")
        assert "message" in data and data["message"].startswith("https://"), "Invalid image URL"
