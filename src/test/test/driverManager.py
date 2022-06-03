from selenium import webdriver


class DriverManager:
    driver = webdriver.Chrome(executable_path="C://chromedriver.exe")#my chromedriver is on disk C inform here the path where your choromedriver is.
    driver.implicitly_wait(10)
    driver.maximize_window()
