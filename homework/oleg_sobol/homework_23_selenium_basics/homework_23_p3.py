from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_select_submit_and_print_result(driver):
    select_value = '3'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_field = driver.find_element(By.ID, "id_choose_language")
    dropdown = Select(select_field)
    dropdown.select_by_value(select_value)
    select_field.submit()
    output_text = driver.find_element(By.ID, 'result-text')
    print("Результат:", output_text.text)


def test_button_hello_word(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button_start = driver.find_element(By.CSS_SELECTOR, "#start button")
    button_start.click()

    output_text = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'finish'))
    )
    assert output_text.text == "Hello World!", f"Ожидаемый текст 'Hello World!', но получен '{output_text.text}'"
