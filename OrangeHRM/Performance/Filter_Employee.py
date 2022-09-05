from ctypes import Union
import time
import unittest
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

user = "Admin"
password = "admin123"

class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="D:\geckodriver-v0.31.0-win32\geckodriver.exe")

    # Mencari Employee
    def test_filterperf_employee(self):
        browser = self.driver
       
        # Login
        browser.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        browser.find_element(By.NAME,"username").send_keys(user)
        time.sleep(5)
        browser.find_element(By.NAME,"password").send_keys(password)
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,".oxd-button").click()
        time.sleep(3)

        # Masuk menu Perfomance > 
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchEvaluatePerformanceReview")
        time.sleep(5)
        
        browser.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input:nth-child(2)").send_keys("Rebecca")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(2)").click()
        time.sleep(5)

        responseData = browser.find_element(By.CSS_SELECTOR, ".orangehrm-bottom-container").text
        # print(responseData)
        self.assertIn(responseData, "Not Found")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
