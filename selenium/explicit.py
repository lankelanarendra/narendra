from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
mywait=WebDriverWait(driver,10)

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit()
# time.sleep(5)
searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()


act_title=driver.title
exp_title="Selenium"
if act_title==exp_title:
    print("selenium test case is passed")
else:
    print("selenium test case is failed")

# "//h3[text()='Selenium']"