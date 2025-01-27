import pytest
from resources.data import DataTest

@pytest.fixture(scope="class")
def dog_api_breed_list():
    return DataTest.get_response(f"{DataTest.DOG_API_BASE_URL}/breeds/list/all")

@pytest.fixture(scope="class")
def dog_api_random_image():
    return DataTest.get_response(f"{DataTest.DOG_API_BASE_URL}/breeds/image/random")

@pytest.fixture(scope="class")
def open_brewery_db_list():
    return DataTest.get_response(DataTest.OPEN_BREWERY_DB_BASE_URL)

@pytest.fixture(scope="class")
def json_placeholder_posts():
    return DataTest.get_response(f"{DataTest.JSON_PLACEHOLDER_BASE_URL}/posts")

@pytest.fixture(scope="class")
def json_placeholder_comments():
    return DataTest.get_response(f"{DataTest.JSON_PLACEHOLDER_BASE_URL}/comments")

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

