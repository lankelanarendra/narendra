import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.flipkart.com/")
driver.maximize_window()

# driver.save_screenshot("C:\\Users\\user\\PycharmProjects\\selenium_tutorial\\selenium\\homepage.png")
# driver.save_screenshot(os.getcwd()+"\\homepage.png")
driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
driver.close()