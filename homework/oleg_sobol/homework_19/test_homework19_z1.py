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


@pytest.mark.parametrize("name, year, price", [
    ("Apple MacBook Pro 16", 2019, 1849.99),
    ("Apple MacBook Air 13", 2020, 999.99),
    ("Apple MacBook Pro 14", 2021, 2499.99)
])
def test_post_object(name, year, price):
    url = "https://api.restful-api.dev/objects"
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": name,
        "data": {
            "year": year,
            "price": price,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(url, json=body, headers=headers)
    assert response.status_code == 200, f"we got status {response.status_code}"
    response_data = response.json()
    assert 'id' in response_data, "not 'id'"
    assert response_data['data']['price'] == price, "price incorrect"


@pytest.mark.medium
def test_put_object(create_object):
    url = f"https://api.restful-api.dev/objects/{create_object}"
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    response = requests.put(url, json=body, headers=headers)
    assert response.status_code == 200, f"no 200, got - {response.status_code}"
    response_data = response.json()
    assert response_data['data']['price'] == 2049.99, "not updated"


@pytest.mark.critical
def test_patch_object(create_object):
    url = f"https://api.restful-api.dev/objects/{create_object}"
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    response = requests.patch(url, json=body, headers=headers)
    assert response.status_code == 200, f"no 200, got - {response.status_code}"
    response_data = response.json()
    assert response_data['name'] == "Apple MacBook Pro 16 (Updated Name)", "not updated"


def test_delete_object(create_object):
    url = f"https://api.restful-api.dev/objects/{create_object}"
    response = requests.delete(url)
    assert response.status_code == 200, f"actual status {response.status_code}"
    response_data = response.json()
    assert response_data['message'] == f"Object with id = {create_object} has been deleted.", "mess incorrect"


def test_get_object_by_id(create_object):
    url = f"https://api.restful-api.dev/objects/{create_object}"
    response = requests.get(url)
    assert response.status_code == 200, f"expected status {response.status_code}"
    response_data = response.json()
    assert response_data['id'] == create_object, "create object != ID"
