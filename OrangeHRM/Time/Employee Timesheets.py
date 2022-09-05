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

    # Melihat Employee Timesheets
    def test_lihat_timesheets(self):
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

         # Masuk menu Timesheets > view
         browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")
         time.sleep(2)
        
         browser.find_element(By.CSS_SELECTOR,".oxd-autocomplete-text-input > input:nth-child(2)").send_keys("Rebecca Harmony")
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR,"button.oxd-button:nth-child(2)").click()
         time.sleep(5)

         responseData = browser.current_url
         self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewTimesheet/employeeId/11")

    # Melihat Employee Timesheets data kosong
    def test_lihat_timesheets_empty(self):
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

         # Masuk menu Timesheets > view
         browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")
         time.sleep(2)
        
         browser.find_element(By.CSS_SELECTOR,".oxd-autocomplete-text-input > input:nth-child(2)").send_keys("")
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR,"button.oxd-button:nth-child(2)").click()
         time.sleep(5)

         responseData = browser.current_url
         self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewTimesheet/employeeId/11")


    # Edit Employee Timesheets
    def test_edit_timesheets(self):
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

         # Masuk menu Timesheets > view
         browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")
         time.sleep(2)
        
         browser.find_element(By.CSS_SELECTOR, "div.oxd-table-card:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)").click()
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR,".oxd-button").click()
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR,"td.orangehrm-timesheet-table-body-cell:nth-child(9) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys("12.00")
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(3)").click()
         time.sleep(3)

         responseData = browser.current_url
         self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewTimesheet/employeeId/7?startDate=2022-08-15")

    # Hapus Employee Timesheets
    def test_del_timesheets(self):
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

         # Masuk menu Timesheets > view
         browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")
         time.sleep(5)
        
         browser.find_element(By.CSS_SELECTOR, "div.oxd-table-card:nth-child(6) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)").click()
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR,".oxd-button--ghost").click()
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR,"tr.orangehrm-timesheet-table-body-row:nth-child(5) > td:nth-child(10) > button:nth-child(1)").click()
         time.sleep(5)
         browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(3)").click()
         time.sleep(5)

         responseData = browser.current_url
         self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewTimesheet/employeeId/7?startDate=2022-08-15")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()