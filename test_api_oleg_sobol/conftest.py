import pytest
from test_api_oleg_sobol.endpoints.create_object import CreateObject
from test_api_oleg_sobol.endpoints.update_object import UpdateObject
from test_api_oleg_sobol.endpoints.patch_object import PatchObject
from test_api_oleg_sobol.endpoints.delete_object import DeleteObject
from test_api_oleg_sobol.endpoints.get_object import GetObject


@pytest.fixture()
def create_object():
    return CreateObject()


@pytest.fixture()
def update_object():
    return UpdateObject()


@pytest.fixture()
def patch_object():
    return PatchObject()


@pytest.fixture()
def delete_object():
    return DeleteObject()


@pytest.fixture()
def get_object():
    return GetObject()


@pytest.fixture()
def created_object_id(create_object):
    create_object.create("Apple MacBook Pro 16", 2019, 1849.99)
    object_id = create_object.check_creation(1849.99)
    yield object_id
    delete_object = DeleteObject()
    delete_object.delete(object_id)
