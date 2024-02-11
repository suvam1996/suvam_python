import time

import pytest
from test_orange_hrm.conftest import browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("browser")
class Test_c:
    def test_dashbord(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
        value=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6[2]').text
        # print("conform page text:- ",value)
        #User Management
        if value=="User Management":
            print('-------Admin page verified successfully-------')


    def test_username_input(self):
        username_inputbox=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input')
        username_inputbox.send_keys("Alice.Duval")


    def test_user_role(self):
        dropdown_1=self.driver.find_element(By.XPATH,"//div[@class='oxd-select-text--after']")
        dropdown_1.click()
        time.sleep(10)











