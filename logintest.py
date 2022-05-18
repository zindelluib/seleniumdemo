from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('http://localhost:8000/login')

driver.find_element(By.ID,'username').send_keys('admin')
driver.find_element(By.ID,'password').send_keys('Secure@123')
driver.find_element(By.ID,'btn-login').click()


time.sleep(10)
driver.quit()