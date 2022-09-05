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

    # Tambah Customers Valid
    def test_customers(self):
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

         # Masuk menu Time > Customers
         browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")
         time.sleep(2)
         browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewCustomers")
         time.sleep(2)
        
         browser.find_element(By.CSS_SELECTOR, ".oxd-button").click()
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR,"input.oxd-input:nth-child(1)").send_keys("Aadmin")
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR,".oxd-textarea").send_keys("Hello")
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(3)").click()
         time.sleep(3)

         responseData = browser.current_url
         self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewCustomers")

    # Tambah Customers Todak diisi
    def test_customers_empty(self):
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

         # Masuk menu Time > Customers
         browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")
         time.sleep(2)
         browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewCustomers")
         time.sleep(2)
        
         browser.find_element(By.CSS_SELECTOR, ".oxd-button").click()
         time.sleep(5)
        #  browser.find_element(By.CSS_SELECTOR,"input.oxd-input:nth-child(1)").send_keys("Aadmin")
        #  time.sleep(10)
        #  browser.find_element(By.CSS_SELECTOR,".oxd-textarea").send_keys("Hello")
        #  time.sleep(10)
         browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(3)").click()
         time.sleep(3)

        #  responseData = browser.current_url
        #  self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewCustomers")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()