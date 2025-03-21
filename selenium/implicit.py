from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
driver.maximize_window()
searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit()
# time.sleep(5)
driver.find_element(By.XPATH,"//h3[text()='Selenium']")
act_title=driver.title
exp_title="Selenium"
if act_title==exp_title:
    print("selenium test case is passed")
else:
    print("selenium test case is failed")

