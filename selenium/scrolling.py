from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(10)

# 1)scroll down page by pixel
# driver.execute_script("window.scrollBy(0,5000)","India")
# value=driver.execute_script("return window.pageYOffset;")
# print("number of pixel moved:",value) #5000

#scroll down page till element is visible
flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value=driver.execute_script("return window.pageYOffset;")
print("number of pixel moved:",value) #7469.33349609375
time.sleep(5)

# 3)scroll down page till end
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# value=driver.execute_script("return window.pageYOffset;")
# print("number of pixel moved:",value) #9485.3330078125
# time.sleep(5)
#
# #scroll up to starting point
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
# value=driver.execute_script("return window.pageYOffset;")
# print("number of pixel moved:",value) #0
# time.sleep(5)
