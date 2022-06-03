import time

import pytest
from selenium.webdriver.common.by import By
from src.test.test.driverManager import DriverManager
from pageUrl import PagesURL


@pytest.fixture
def test_setup():
    global driver
    driver = DriverManager.driver
    driver.get(PagesURL.get_url_page)
    yield
    time.sleep(4)
    driver.quit()


def test_fill_success(test_setup):
    zipcode_id = driver.find_element(By.ID, "campoCEP")
    zipcode_id.send_keys("52040220")
    buttonElement = driver.find_element(By.XPATH, "//div[3]/fieldset/center/input[2]")
    buttonElement.click()
    visibleElement = driver.find_element(By.XPATH, "//*[@id='resultado']/center/font")

    print(visibleElement.is_displayed())


def test_fill_fail(test_setup):
    zipcode_id = driver.find_element(By.ID, "campoCEP")
    zipcode_id.send_keys("0")
    buttonElement = driver.find_element(By.XPATH, "//div[3]/fieldset/center/input[2]")
    buttonElement.click()
    visibleElement = driver.find_element(By.XPATH, "//*[@id='resultado']/center/font")

    if visibleElement.is_displayed() == False:
        print("success")


