import requests
import allure
from test_api_oleg_sobol.endpoints.general_class_endpoints import Endpoint


class CreateObject(Endpoint):

    @allure.step('Creating a new object')
    def create(self, name, year, price):
        body = {
            "name": name,
            "data": {
                "year": year,
                "price": price,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        self.response = requests.post(self.url, json=body, headers=self.headers)
        return self.response

    @allure.step('Check response status is 200')
    def check_status_200(self):
        assert self.response.status_code == 200, f"Expected 200, but got {self.response.status_code}"

    @allure.step('Check the object was created correctly')
    def check_creation(self, price):
        response_data = self.response.json()
        assert 'id' in response_data, "Response does not contain 'id'"
        assert response_data['data']['price'] == price, "Price mismatch"
        return response_data['id']
