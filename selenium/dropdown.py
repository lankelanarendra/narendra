from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.maximize_window()
# time.sleep(10)

drpcountry = Select(driver.find_element(By.XPATH, "//*[@id='post-2646']/div[2]/div/div/div/p/select"))
time.sleep(10)
# select from the dropdown
drpcountry.select_by_visible_text("India")
# drpcountry.select_by_value("AUS")
# drpcountry.select_by_index(1)
# capture the all options and print them

# alloptions=drpcountry.options
# print("total number of options:",len(alloptions))
# for opt in alloptions:
#     print(opt.text)
#
# # select option from the dropdown without using built-in method
#
# for opt in alloptions:
#     if opt.text=="India":
#         opt.click()
#         break


time.sleep(10)



//*[@id="post-2646"]/div[2]/div/div/div/p/select
