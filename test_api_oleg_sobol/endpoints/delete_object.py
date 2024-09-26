import requests
import allure
from test_api_oleg_sobol.endpoints.general_class_endpoints import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Deleting an object')
    def delete(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}")
        return self.response

    @allure.step('Check response status is 200')
    def check_status_200(self):
        assert self.response.status_code == 200, f"Expected 200, but got {self.response.status_code}"

    @allure.step('Check the object was deleted correctly')
    def check_deletion(self, object_id):
        response_data = self.response.json()
        assert response_data['message'] == f"Object with id = {object_id} has been deleted.", "Message mismatch"
