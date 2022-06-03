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
    time.sleep(4)
    visibleElement = driver.find_element(By.XPATH, "//*[@id='resultado']/center/font")
    visibleElementLogradouro = driver.find_element(By.XPATH, "//*[@id='resultado']/table/tbody/tr[2]/td[2]")
    visibleElementDistrict = driver.find_element(By.XPATH, "//*[@id='resultado']/table/tbody/tr[3]/td[2]")
    visibleElementCity = driver.find_element(By.XPATH, "//*[@id='resultado']/table/tbody/tr[4]/td[2]")
    visibleElementStreet = driver.find_element(By.XPATH, "//*[@id='resultado']/table/tbody/tr[1]/td[2]")
    visibleElementUf = driver.find_element(By.XPATH, "//*[@id='resultado']/table/tbody/tr[5]/td[2]")

    assert visibleElement.text == "sucesso - cep completo"
    assert visibleElementStreet.text == "Rua"
    assert visibleElementLogradouro.text == "Cirilino Afonso de Melo"
    assert visibleElementDistrict.text == "Campo Grande"
    assert visibleElementCity.text == "Recife"
    assert visibleElementUf.text == "PE"


def test_fill_fail(test_setup):
    zipcode_id = driver.find_element(By.ID, "campoCEP")
    zipcode_id.send_keys("0001")
    buttonElement = driver.find_element(By.XPATH, "//div[3]/fieldset/center/input[2]")
    buttonElement.click()
    time.sleep(4)

    visibleElement = driver.find_element(By.XPATH, "//*[@id='resultado']/center/font")

    assert visibleElement.text == "sucesso - cep não encontrado"
