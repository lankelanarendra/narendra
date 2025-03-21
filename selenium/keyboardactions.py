from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
import time
driver=webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.implicitly_wait(10)
driver.maximize_window()

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input1.send_keys("welcome to selenium")
# time.sleep(5)
act=ActionChains(driver)

# input-->1 ctrl+C select  the text
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#input--> ctrl+c copy text
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()
# act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#press Tab key  to navigate  to input2
# act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.TAB)
act.perform()
time.sleep(10)
#input2--> ctrl+v past text
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()
# act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(10)