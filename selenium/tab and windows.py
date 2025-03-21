from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)

# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT,"CONTACT").click()

# contactlink=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"CONTACT").send_keys(contactlink)
#
# time.sleep(10)

# New Window selenium-4: open a new tab and switch to new tab
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window("tab")
# driver.get("https://www.orangehrm.com/")
time.sleep(5)

# New Window selenium-4: open a new window and switch to new window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window("window")
driver.get("https://www.orangehrm.com/")
