from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
driver.implicitly_wait(5)  

source_ele=driver.find_element(By.ID,"box3")
target_ele=driver.find_element(By.ID,"box107")
time.sleep(5)

act=ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform()

time.sleep(5)