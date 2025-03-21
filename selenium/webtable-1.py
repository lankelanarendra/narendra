# 1)count the number of row & columns
# 2) Read specific row & column data
# 3) Read all the rows & column data
# 4)Read data based on condition(list books name whose author  is mukesh)

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1)count the number of row & columns
noofrows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noofcolumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
print(noofrows) #7
print(noofcolumns) #4

# # 2) Read specific row & column data
data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[4]/td[3]").text
# print(data)

# 3) Read all the rows & column data
print("printing all the rows and columns............................")
# for r in range(2,noofrows+1):
#     for c in range(1,noofcolumns+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data)
#     print()

# 4)Read data based on condition(list books name whose author  is mukesh)
for r in range(2,noofrows+1):
    authorname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorname=="Mukesh":
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookname,"        ",authorname,"       ",price)

driver.close()