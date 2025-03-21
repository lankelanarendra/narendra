from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

# emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
#
# emailbox.clear()
# emailbox.send_keys("admin@yourstore.com")
#
# print("result of text:",emailbox.text) #printed is nothing
# print("result of get_attribute:",emailbox.get_attribute('value')) #admin@yourstore.com

button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("result of text:",button.text) #Login
print("result of get_attribute:",button.get_attribute('value'))

