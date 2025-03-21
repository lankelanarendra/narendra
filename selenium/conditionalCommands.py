from selenium import webdriver
from selenium.webdriver.common.by import By
import  time
driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Fregisterresult%2F1")
driver.maximize_window()
time.sleep(10)
searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# is_displayed
# is_enabled
print("display status:",searchbox.is_displayed())
print("enable status:",searchbox.is_enabled())

# is_selected
male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print(male.is_selected())
print(female.is_selected())

print("after click the male button are true")
male.click()
print(male.is_selected()) #True
print(female.is_selected()) #False

print("after click the female button is True")
female.click()
print(male.is_selected()) #False
print(female.is_selected()) #True