from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.get("https://www.snapdeal.com/")
# driver.maximize_window()
# driver.back()
time.sleep(5)
# driver.forward()

# driver.refresh()

driver.close()