from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
checkboxs=driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#1)select specific day
# driver.find_element(By.XPATH,"//label[normalize-space()='Saturday']").click()
time.sleep(10)
#2) select all the days
checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxs)) #7

# for checkbox in checkboxs:
    # checkbox.click()

#3)select multiple checkboxes by choice
# for checkbox in checkboxs:
#     weekname=checkbox.get_attribute("id")
#     if weekname=='sunday' or weekname=='monday':
#         checkbox.click()

#4)select the last two checkboxes
# for i in range(len(checkboxs)-2,len(checkboxs)):
#     checkboxs[i].click()


#5)select the first two checkboxes
# for i in range(len(checkboxs)):
    # if i<2:
        # checkboxs[i].click()
time.sleep(10)
#6) clearing the all checkboxes True or False
for checkbox in checkboxs:
    if checkbox.is_displayed():
        checkbox.click()



