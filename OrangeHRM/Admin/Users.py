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

    # Mencari Username
    def test_cari_username(self):
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

        # Masuk menu Admin > User Management > Users
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        time.sleep(5)
        
        browser.find_element(By.CSS_SELECTOR, "input.oxd-input:nth-child(1)").send_keys("Admin")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(2)").click()
        time.sleep(5)

        responseData = browser.find_element(By.CSS_SELECTOR, "div.oxd-table-cell:nth-child(2) > div:nth-child(1)").text
        # print(responseData)
        self.assertIn(responseData, "Admin")

    # Mencari Username Tidak Valid
    def test_cari_username_tidakvalid(self):
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

        # Masuk menu Admin > User Management > Users
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        time.sleep(5)
        
        browser.find_element(By.CSS_SELECTOR, "input.oxd-input:nth-child(1)").send_keys("1234")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(2)").click()
        time.sleep(5)

        responseData = browser.find_element(By.CSS_SELECTOR, "div.oxd-table-cell:nth-child(2) > div:nth-child(1)").text
        # print(responseData)
        self.assertIn(responseData, "")

    # Mencari Employee
    def test_cari_employee(self):
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

        # Masuk menu Admin > User Management > Users
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        time.sleep(5)
        
        browser.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input:nth-child(2)").send_keys("Rebecca")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(2)").click()
        time.sleep(5)

        responseData = browser.find_element(By.CSS_SELECTOR, "div.oxd-table-cell:nth-child(2) > div:nth-child(1)").text
        # print(responseData)
        self.assertIn(responseData, "Rebecca.Harmony")

    # Tambah User
    def test_tambahuser(self):
        browser = self.driver
        ddelement = Select
       
        # Login
        browser.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(15)
        browser.find_element(By.NAME,"username").send_keys(user)
        time.sleep(5)
        browser.find_element(By.NAME,"password").send_keys(password)
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,".oxd-button").click()
        time.sleep(10)

        # Masuk menu Admin > Users
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button.oxd-button--secondary:nth-child(1)").click()
        time.sleep(5)

        # Dropdown
        kriteria = browser.find_element(By.CSS_SELECTOR,"div.oxd-form-row:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").text
        browser.find_element(By.CSS_SELECTOR,"div.oxd-form-row:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click() # Database Administrator
        time.sleep(5)
        kriteria = browser.find_element(By.CSS_SELECTOR,"div.oxd-grid-item:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").text
        browser.find_element(By.CSS_SELECTOR,"div.oxd-grid-item:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click() # Database Administrator
        time.sleep(5)

        browser.find_element(By.CSS_SELECTOR,".oxd-autocomplete-text-input > input:nth-child(2)").send_keys("Rebecca Harmony")
        time.sleep(15)
        browser.find_element(By.CSS_SELECTOR,"div.oxd-grid-item:nth-child(4) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("Rebecca")
        time.sleep(15)
        browser.find_element(By.CSS_SELECTOR,".user-password-cell > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("01Rebecca_02")
        time.sleep(15)
        browser.find_element(By.CSS_SELECTOR,"div.oxd-form-row:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("01Rebecca_02")
        time.sleep(15)
        browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(3)").click()
        time.sleep(10)

        responseData = browser.find_element(By.CSS_SELECTOR, ".orangehrm-horizontal-padding").text
        self.assertIn(responseData, kriteria)
        
    # Tambah User Semua Kosong
    def test_tambahuser_empty(self):
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

        # Masuk menu Admin > Users
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        time.sleep(5) 
        browser.find_element(By.CSS_SELECTOR, "button.oxd-button--secondary:nth-child(1)").click()
        time.sleep(5)

        browser.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(3)").click()
        time.sleep(5)

        responseData = browser.current_url
        self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()