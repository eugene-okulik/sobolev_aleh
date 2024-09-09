import requests


def post_object():
    url = "https://api.restful-api.dev/objects"
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=body, headers=headers)

    assert response.status_code == 200, f"no 200, got - {response.status_code}"
    response_data = response.json()
    assert 'id' in response_data, "not id"

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    return response.json()['id']


post_id = post_object()


def put_object():
    url = f"https://api.restful-api.dev/objects/{post_id}"
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
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, json=body, headers=headers)

    assert response.status_code == 200, f"no 200, got - {response.status_code}"
    response_data = response.json()
    assert response_data['data']['price'] == 2049.99, "not updated"

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")


put_object()


def patch_object():
    url = f"https://api.restful-api.dev/objects/{post_id}"
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(url, json=body, headers=headers)

    assert response.status_code == 200, f"no 200, got - {response.status_code}"
    response_data = response.json()
    assert response_data['name'] == "Apple MacBook Pro 16 (Updated Name)", "not updated"

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")


patch_object()


def delete_object():
    url = f"https://api.restful-api.dev/objects/{post_id}"
    response = requests.delete(url)

    assert response.status_code == 200, f"no 200, got - {response.status_code}"
    response_data = response.json()
    expected_message = f"Object with id = {post_id}, has been deleted."
    assert response_data.get(
        'message') == expected_message, f"unexpected  message: {response_data.get('message')}"

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")


delete_object()
