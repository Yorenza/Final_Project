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

    # Mendownload Personal Data
    def test_records(self):
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

        # Masuk menu Performance > 
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee")
        time.sleep(5)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(2)").click()
        time.sleep(5)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/accessEmployeeData")
        time.sleep(5)
        
        
        browser.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input:nth-child(2)").send_keys("Paul Collings")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(1)").click()
        time.sleep(5)
        

    # Mendownload Personal Data kosong
    def test_records_empty(self):
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

        # Masuk menu Performance > 
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee")
        time.sleep(5)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(2)").click()
        time.sleep(5)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/accessEmployeeData")
        time.sleep(5)
        
        
        browser.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input:nth-child(2)").send_keys("")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(5)
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
