from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(10)
print(driver.title) # title is OrangeHRM
print(driver.current_url) #current_url is https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print(driver.page_source)