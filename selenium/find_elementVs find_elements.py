from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.snapdeal.com/")
driver.maximize_window()

# find element--->returns single webelement
# 1) locator matching with single webelement
# element=driver.find_element(By.XPATH,"//input[@id='inputValEnter']")
# element.send_keys("realme6")
# time.sleep(10)

# #2)locator matching multiple webelements
# element=driver.find_element(By.XPATH,"//div[@class='middleTop row']//div[@class='footer-inner']//a")
# print(element.text) # prints first links from the footer "Privacy Policy"

#3)element not available then throw NoSuchElementException
# login_element=driver.find_elements(By.XPATH,"//a[normalize-space()='login']")
# login_element.click()

# find_elements-->return multiple webelements
#1)locator matching with single webelement
# elements=driver.find_elements(By.XPATH,"//input[@id='inputValEnter']")
# print(len(elements))
# elements[0].send_keys("realme6")

#2)locator matching multiple webelements

element=driver.find_elements(By.XPATH,"//div[@class='middleTop row']//div[@class='footer-inner']//a")
# print(len(element)) #20
print(element[0].text)

# for i in element:    #all 20 links in using for loop
    # print(i.text)

# 3) element not available--->Zero
# element=driver.find_elements(By.XPATH,"log")
# print(len(element)) #Zero
