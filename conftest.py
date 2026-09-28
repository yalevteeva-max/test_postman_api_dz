import pytest
import requests


@pytest.fixture
def base_url():
   
    return "https://postman-echo.com"


@pytest.fixture
def session():
   
    with requests.Session() as s:
        yield s