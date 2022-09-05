from ctypes import Union
import time
import unittest
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = "Admin"
password = "admin123"

class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="D:\geckodriver-v0.31.0-win32\geckodriver.exe")

    # Tambah Nasionalis Valid
    def test_nasional(self):
         browser = self.driver
       
         # Login
         browser.get("https://opensource-demo.orangehrmlive.com/")
         time.sleep(5)
         browser.find_element(By.NAME,"username").send_keys(user)
         time.sleep(5)
         browser.find_element(By.NAME,"password").send_keys(password)
         time.sleep(1)
         browser.find_element(By.CSS_SELECTOR,".oxd-button").click()
         time.sleep(5)

         # Masuk menu Admin > Nasionality
         browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/nationality")
         time.sleep(2)
        
         browser.find_element(By.CSS_SELECTOR, ".oxd-button").click()
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR,"input.oxd-input:nth-child(1)").send_keys("Test")
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(3)").click()
         time.sleep(5)

         responseData = browser.current_url
         self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/web/index.php/admin/nationality")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()