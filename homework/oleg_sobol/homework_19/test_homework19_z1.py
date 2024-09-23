import pytest
import requests
import allure


@allure.feature("API Testing")
@allure.story("Create Object")
@allure.title("Test POST Object Creation")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Проверка создания объекта с помощью POST-запроса")
@allure.link("https://example.com/api-docs", name="API Documentation")
@allure.issue("123", "Bug related to object creation")
@allure.testcase("https://testrail.example.com/case/456", "Test Case for Object Creation")
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
    with allure.step("Отправка POST-запроса для создания объекта"):
        response = requests.post(url, json=body, headers=headers)
    assert response.status_code == 200, f"we got status {response.status_code}"
    response_data = response.json()
    with allure.step("Проверка, что объект создан корректно"):
        assert 'id' in response_data, "not 'id'"
        assert response_data['data']['price'] == price, "price incorrect"


@allure.feature("API Testing")
@allure.story("Update Object")
@allure.title("Test PUT Object Update")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Проверка обновления объекта с помощью PUT-запроса")
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
    with allure.step("Отправка PUT-запроса для обновления объекта"):
        response = requests.put(url, json=body, headers=headers)
    assert response.status_code == 200, f"no 200, got - {response.status_code}"
    response_data = response.json()
    with allure.step("Проверка, что объект обновлён корректно"):
        assert response_data['data']['price'] == 2049.99, "not updated"


@allure.feature("API Testing")
@allure.story("Patch Object")
@allure.title("Test PATCH Object")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Проверка частичного обновления объекта с помощью PATCH-запроса")
@pytest.mark.critical
def test_patch_object(create_object):
    url = f"https://api.restful-api.dev/objects/{create_object}"
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    with allure.step("Отправка PATCH-запроса для частичного обновления объекта"):
        response = requests.patch(url, json=body, headers=headers)
    assert response.status_code == 200, f"no 200, got - {response.status_code}"
    response_data = response.json()
    with allure.step("Проверка, что имя объекта обновлено"):
        assert response_data['name'] == "Apple MacBook Pro 16 (Updated Name)", "not updated"


@allure.feature("API Testing")
@allure.story("Delete Object")
@allure.title("Test DELETE Object")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("Проверка удаления объекта с помощью DELETE-запроса")
def test_delete_object(create_object):
    url = f"https://api.restful-api.dev/objects/{create_object}"
    with allure.step("Отправка DELETE-запроса для удаления объекта"):
        response = requests.delete(url)
    assert response.status_code == 200, f"actual status {response.status_code}"
    response_data = response.json()
    with allure.step("Проверка, что объект удалён"):
        assert response_data['message'] == f"Object with id = {create_object} has been deleted.", "mess incorrect"


@allure.feature("API Testing")
@allure.story("Get Object")
@allure.title("Test GET Object by ID")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Проверка получения объекта по ID с помощью GET-запроса")
def test_get_object_by_id(create_object):
    url = f"https://api.restful-api.dev/objects/{create_object}"
    with allure.step("Отправка GET-запроса для получения объекта"):
        response = requests.get(url)
    assert response.status_code == 200, f"expected status {response.status_code}"
    response_data = response.json()
    with allure.step("Проверка, что получен правильный объект"):
        assert response_data['id'] == create_object, "create object != ID"
