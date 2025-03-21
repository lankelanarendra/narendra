from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(10)

driver.find_element(By.CLASS_NAME,"dropbtn").click()
# driver.find_element(By.XPATH,"//input[@class='gsc-search-button']").click()

time.sleep(10)
driver.quit()