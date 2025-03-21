from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
max_slider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")

print("location of slider before moving.............")
print(min_slider.location) #{'x': 59, 'y': 252}
print(max_slider.location) #{'x': 510, 'y': 252}

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-200,0).perform()
time.sleep(10)

print("location of after moving.............")
print(min_slider.location) #{'x': 158, 'y': 289}
print(max_slider.location) #{'x': 312, 'y': 289}