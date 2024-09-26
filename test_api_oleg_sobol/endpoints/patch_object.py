import requests
import allure
from test_api_oleg_sobol.endpoints.general_class_endpoints import Endpoint


class PatchObject(Endpoint):

    @allure.step('Partially updating an object')
    def patch(self, object_id, new_name):
        body = {
            "name": new_name
        }
        self.response = requests.patch(f"{self.url}/{object_id}", json=body, headers=self.headers)
        return self.response

    @allure.step('Check response status is 200')
    def check_status_200(self):
        assert self.response.status_code == 200, f"Expected 200, but got {self.response.status_code}"

    @allure.step('Check the object name was updated correctly')
    def check_update(self, new_name):
        response_data = self.response.json()
        assert response_data['name'] == new_name, "Name mismatch"
