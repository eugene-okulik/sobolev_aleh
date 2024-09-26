import requests
import allure
from test_api_oleg_sobol.endpoints.general_class_endpoints import Endpoint


class UpdateObject(Endpoint):

    @allure.step('Updating an object')
    def update(self, object_id, price):
        body = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": price,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
                "color": "silver"
            }
        }
        self.response = requests.put(f"{self.url}/{object_id}", json=body, headers=self.headers)
        return self.response

    @allure.step('Check response status is 200')
    def check_status_200(self):
        assert self.response.status_code == 200, f"Expected 200, but got {self.response.status_code}"

    @allure.step('Check the object was updated correctly')
    def check_update(self, price):
        response_data = self.response.json()
        assert response_data['data']['price'] == price, "Price mismatch"
