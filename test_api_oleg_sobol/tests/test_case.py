import allure
import pytest


@allure.feature("API Testing")
@allure.story("Create Object")
@pytest.mark.parametrize("name, year, price", [
    ("Apple MacBook Pro 16", 2019, 1849.99),
    ("Apple MacBook Air 13", 2020, 999.99),
    ("Apple MacBook Pro 14", 2021, 2499.99)
])
def test_post_object(create_object, name, year, price):
    create_object.create(name, year, price)
    create_object.check_status_200()
    create_object.check_creation(price)


@allure.feature("API Testing")
@allure.story("Update Object")
def test_put_object(update_object, created_object_id):
    update_object.update(created_object_id, 2049.99)
    update_object.check_status_200()
    update_object.check_update(2049.99)


@allure.feature("API Testing")
@allure.story("Patch Object")
def test_patch_object(patch_object, created_object_id):
    patch_object.patch(created_object_id, "Apple MacBook Pro 16 (Updated)")
    patch_object.check_status_200()
    patch_object.check_update("Apple MacBook Pro 16 (Updated)")


@allure.feature("API Testing")
@allure.story("Delete Object")
def test_delete_object(delete_object, created_object_id):
    delete_object.delete(created_object_id)
    delete_object.check_status_200()
    delete_object.check_deletion(created_object_id)


@allure.feature("API Testing")
@allure.story("Get Object")
def test_get_object_by_id(get_object, created_object_id):
    get_object.get(created_object_id)
    get_object.check_status_200()
    get_object.check_get(created_object_id)
