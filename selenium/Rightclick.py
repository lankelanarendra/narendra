from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(5)

button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act=ActionChains(driver)

act.context_click(button).perform() #rightclick
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/ul/li[3]").click()
time.sleep(10)
driver.switch_to.alert.accept()
