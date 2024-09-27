import requests
import allure
from test_api_oleg_sobol.endpoints.general_class_endpoints import Endpoint


class GetObject(Endpoint):

    @allure.step('Getting an object by ID')
    def get(self, object_id):
        self.response = requests.get(f"{self.url}/{object_id}")
        return self.response

    @allure.step('Check response status is 200')
    def check_status_200(self):
        assert self.response.status_code == 200, f"Expected 200, but got {self.response.status_code}"

    @allure.step('Check the object was retrieved correctly')
    def check_get(self, object_id):
        response_data = self.response.json()
        assert response_data['id'] == object_id, "ID mismatch"
