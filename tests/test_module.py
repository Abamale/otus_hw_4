import pytest
import requests



def test_url_status_code(url, status_code):
    response = requests.get(url)
    assert response.status_code == status_code, (
        f"Expected status code {status_code}, got {response.status_code} for URL: {url}"
    )