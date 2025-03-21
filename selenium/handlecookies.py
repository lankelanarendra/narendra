from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.opencart.com/")
driver.maximize_window()

cookies=driver.get_cookies()
print("size of cookies",len(cookies))
#print details of all cookies
# for i in cookies:
#     # print(i)
#     print(i.get('name'),i.get("value"),i.get("expirydate"))

# adding new cookies from to the browser
# driver.add_cookie({'name':'MyCookies','value':'123456'})
# cookies=driver.get_cookies()
# print("size of cookies after adding new one:",len(cookies))

# delete specific cookie from the browser
driver.delete_cookie("MyCookies")
cookies=driver.get_cookies()
print("size of cookies after deleting one:",len(cookies))

# deleting all cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("size of cookies after deleting all cookies:",len(cookies))