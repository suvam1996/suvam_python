import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    """set up the orange HRM webpage for login purpose"""
    service_object = Service("C:\webdriver\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service_object)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    request.cls.driver = driver
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys('Admin')
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys('admin123')
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    yield
    driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    time.sleep(5)
    driver.quit()
