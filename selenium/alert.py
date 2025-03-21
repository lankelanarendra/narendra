from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

alertwindow=driver.switch_to.alert
print(alertwindow.text)

alertwindow.send_keys("selenium")
# alertwindow.accept() #close alert window by using ok button
alertwindow.dismiss()  #close alert window by using cancel button