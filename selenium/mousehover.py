import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(10)

point_me=driver.find_element(By.XPATH,"//button[normalize-space()='Point Me']")

mobiles=driver.find_element(By.XPATH,"//a[normalize-space()='Mobiles']")

laptops=driver.find_element(By.XPATH,"//a[normalize-space()='Laptops']")

act=ActionChains(driver)
act.move_to_element(point_me).move_to_element(mobiles).move_to_element(laptops).click().perform()
time.sleep(10)
