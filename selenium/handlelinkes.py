from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/digital-downloads")
driver.maximize_window()
time.sleep(10)
#1) click the link
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

#2)find the number of links in a page

links=driver.find_elements(By.TAG_NAME,"a")
print("total number of links:",len(links))

#3) print all the links
for link in links:
    print(link.text)

