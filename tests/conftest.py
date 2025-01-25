import pytest
from resources.data import DataTest

@pytest.fixture(scope="class")
def responses():
    return {
        "dog_api": {
            "breed_list": DataTest.get_response(f"{DataTest.DOG_API_BASE_URL}/breeds/list/all"),
            "random_image": DataTest.get_response(f"{DataTest.DOG_API_BASE_URL}/breeds/image/random")
        },
        "open_brewery_db": {
            "breweries_list": DataTest.get_response(DataTest.OPEN_BREWERY_DB_BASE_URL)
        },
        "json_placeholder": {
            "posts": DataTest.get_response(f"{DataTest.JSON_PLACEHOLDER_BASE_URL}/posts"),
            "comments": DataTest.get_response(f"{DataTest.JSON_PLACEHOLDER_BASE_URL}/comments")
        }
    }


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="https://ya.ru", help="URL to test"
    )
    parser.addoption(
        "--status_code", action="store", type=int, default=200, help="Expected status code"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")

