from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(10)

# windowid=driver.current_window_handle
# print(windowid)

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowid=driver.window_handles

parentwindowid=windowid[0]
childwindowid=windowid[1]
print(parentwindowid,childwindowid)

# driver.switch_to.window(childwindowid)
# print(driver.title)
#
# for widid in windowid:
#     driver.switch_to.window(widid)
#     print(driver.title)

time.sleep(10)