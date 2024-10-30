from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(3)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_add_product(driver):
    driver.get('https://www.demoblaze.com/index.html')
    product_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]")
    ActionChains(driver).key_down(Keys.COMMAND).click(product_link).key_up(Keys.COMMAND).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Add to cart')]")
    add_to_cart_button.click()
    WebDriverWait(driver, 5).until(ec.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
    cart_link.click()
    product_in_cart = driver.find_element(By.XPATH, "//td[contains(text(), 'Samsung galaxy s6')]")
    assert product_in_cart.is_displayed()


def test_add_to_compare(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    first_product = driver.find_element(By.XPATH, "(//li[@class='item product product-item'])[1]")
    ActionChains(driver).move_to_element(first_product).perform()
    add_to_compare_button = first_product.find_element(By.XPATH, ".//a[contains(@title, 'Add to Compare')]")
    add_to_compare_button.click()
    compare_section = driver.find_element(By.XPATH, "//div[@class='block block-compare']")
    product_in_compare = compare_section.find_element(By.XPATH, ".//a[contains(text(), 'Bag')]")
    assert product_in_compare.is_displayed()
