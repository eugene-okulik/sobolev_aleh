from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_submit_and_print_result(driver):
    input_text = "example_text"
    driver.get('https://www.qa-practice.com/elements/input/simple')

    input_field = driver.find_element(By.ID, 'id_text_string')
    input_field.send_keys(input_text)
    input_field.submit()
    output_text = driver.find_element(By.ID, 'result-text')
    print("Результат:", output_text.text)
