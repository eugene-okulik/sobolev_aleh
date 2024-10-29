from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    yield chrome_driver


def scroll_into_view(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)


def test_submit_form(driver):
    first_name = "Alex"
    last_name = "Flex"
    user_email = "alexflex@example.com"
    phone_number = "1234567890"
    date_of_birth = "20 Nov 1995"
    subjects = "Maths"
    address = "Minsk, street"
    state = "NCR"
    city = "Delhi"

    driver.get('https://demoqa.com/automation-practice-form')

    first_name_field = driver.find_element(By.ID, 'firstName')
    scroll_into_view(driver, first_name_field)
    first_name_field.send_keys(first_name)

    last_name_field = driver.find_element(By.ID, 'lastName')
    scroll_into_view(driver, last_name_field)
    last_name_field.send_keys(last_name)

    email_field = driver.find_element(By.ID, 'userEmail')
    scroll_into_view(driver, email_field)
    email_field.send_keys(user_email)

    gender_radio = driver.find_element(By.XPATH, "//label[text()='Male']")
    scroll_into_view(driver, gender_radio)
    gender_radio.click()

    phone_field = driver.find_element(By.ID, "userNumber")
    scroll_into_view(driver, phone_field)
    phone_field.send_keys(phone_number)

    date_field = driver.find_element(By.ID, "dateOfBirthInput")
    scroll_into_view(driver, date_field)
    date_field.click()
    date_field.send_keys(Keys.COMMAND + 'a')
    date_field.send_keys(date_of_birth)
    date_field.send_keys(Keys.ENTER)

    subjects_field = driver.find_element(By.ID, 'subjectsInput')
    scroll_into_view(driver, subjects_field)
    subjects_field.send_keys(subjects)
    subjects_field.send_keys(Keys.ENTER)

    sports_checkbox = driver.find_element(By.XPATH, "//label[text()='Sports']")
    scroll_into_view(driver, sports_checkbox)
    sports_checkbox.click()

    music_checkbox = driver.find_element(By.XPATH, "//label[text()='Music']")
    scroll_into_view(driver, music_checkbox)
    music_checkbox.click()

    address_field = driver.find_element(By.ID, "currentAddress")
    scroll_into_view(driver, address_field)
    address_field.send_keys(address)

    state_field = driver.find_element(By.ID, "state")
    scroll_into_view(driver, state_field)
    state_field.click()
    driver.find_element(By.XPATH, f"//div[text()='{state}']").click()

    city_field = driver.find_element(By.ID, "city")
    city_field.click()
    driver.find_element(By.XPATH, f"//div[text()='{city}']").click()

    submit_button = driver.find_element(By.ID, "submit")
    scroll_into_view(driver, submit_button)
    submit_button.click()

    result_modal = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CLASS_NAME, "modal-body"))
    )

    result_text = result_modal.text
    print("Результат:")
    print(result_text)
