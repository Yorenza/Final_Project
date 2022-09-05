from ctypes import Union
import time
import unittest
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = "Admin"
password = "admin123"

class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="D:\geckodriver-v0.31.0-win32\geckodriver.exe")

    # Filter daftar Directory dengan kriteria Job Title
    def test_filter_job_title(self):
        browser = self.driver
       
        # Login
        browser.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        browser.find_element(By.NAME,"username").send_keys(user)
        time.sleep(5)
        browser.find_element(By.NAME,"password").send_keys(password)
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,".oxd-button").click()
        time.sleep(5)

        # Masuk menu Directory
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory")
        time.sleep(5)
        
        # Isi form
        kriteria = browser.find_element(By.CSS_SELECTOR,".oxd-grid-3 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").text
        browser.find_element(By.CSS_SELECTOR,".oxd-grid-3 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click() # Database Administrator
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,"button.oxd-button:nth-child(2)").click()
        time.sleep(5)
        
        responseData = browser.find_element(By.CSS_SELECTOR, ".orangehrm-horizontal-padding").text
        self.assertIn(responseData, kriteria)

    # Filter daftar Directory dengan kriteria Location
    def test_filter_location(self):
        browser = self.driver
       
        # Login
        browser.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        browser.find_element(By.NAME,"username").send_keys(user)
        time.sleep(5)
        browser.find_element(By.NAME,"password").send_keys(password)
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,".oxd-button").click()
        time.sleep(5)
        
        # Masuk menu Directory
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory")
        time.sleep(5)
        
        # Isi form
        kriteria = browser.find_element(By.CSS_SELECTOR,".oxd-grid-3 > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").text
        browser.find_element(By.CSS_SELECTOR,".oxd-grid-3 > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click() # Database Administrator
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,"button.oxd-button:nth-child(2)").click()
        time.sleep(5)
        
        responseData = browser.find_element(By.CSS_SELECTOR, ".orangehrm-horizontal-padding").text
        self.assertIn(responseData, kriteria)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
