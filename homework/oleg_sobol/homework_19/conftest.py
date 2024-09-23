import pytest
import requests


@pytest.fixture(scope="session", autouse=True)
def print_test_start_end():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def print_before_after_test():
    print("before test")
    yield
    print("after test")


@pytest.fixture
def create_object():
    url = "https://api.restful-api.dev/objects"
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(url, json=body, headers=headers)
    post_id = response.json()['id']
    yield post_id
    requests.delete(f"https://api.restful-api.dev/objects/{post_id}")
