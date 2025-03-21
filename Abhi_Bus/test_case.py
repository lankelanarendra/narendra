from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time


class AbhiBusAutomation:
     def __init__(self):
         self.driver = webdriver.Chrome()

     def open_website(self):
        self.driver.get("https://www.abhibus.com/")
        self.driver.maximize_window()
        time.sleep(3)

     def login_with_otp(self):
        # Click on Login button
        login_button = self.driver.find_element(By.XPATH, "//span[normalize-space()='Login/SignUp']")
        login_button.click()
        time.sleep(5)

        # Enter Mobile Number
        mobile_input = self.driver.find_element(By.XPATH, "//input[@type='number']")
        mobile_input.send_keys("9121554690")
        time.sleep(5)

        # login button
        login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        login_button.click()
        time.sleep(20)

     #Enter the from details
     def from_to_details(self):
        self.driver.find_element(By.XPATH,"//input[@placeholder='From Station']").click()
        from_address = self.driver.find_elements(By.XPATH,"//ul[@class='collection auto-complete-list primary sm false']//div")

        for add in from_address:
            if add.text == "Bangalore":
                print("From address is satisfied",add)
                add.click()
                break
        time.sleep(5)

        # Enter the to details
        self.driver.find_element(By.XPATH,"//input[@placeholder='To Station']").click()
        to_address = self.driver.find_elements(By.XPATH,"//div[@id='search-to']//ul[contains(@class,'collection auto-complete-list primary sm false')]//div")

        for addr in to_address:
            if addr.text =="Kadapa":
                print("TO address is satisfies",addr)
                addr.click()
                break

        time.sleep(5)

        # Select Journey Date
        target_date = (datetime.now() + timedelta(days=3)).day
        self.driver.find_element(By.XPATH, "//input[contains(@placeholder,'Onward Journey Date')]").click()
        dates = self.driver.find_elements(By.XPATH, "//div[@class='container date ']//span[@tabindex='1']")
        print(dates)

        for date in dates:
            if date.text == str(target_date):
            # if date.text == "10":
                print("date is satisfied",date)
                print("dat")
                date.click()
                break
        time.sleep(5)

        # Click Search
        search_button = self.driver.find_element(By.XPATH, "//div[@id='search-button']")
        search_button.click()
        time.sleep(10)

     #Bus Type
     def bus_type(self):
         bus_types = self.driver.find_elements(By.XPATH,"//*[@class='container filter-list ']//a//span[2]")

         for type in bus_types:
             if type.text == "AC":
                 print("AC condition is Satisfied",type)
                 type.click()
                 break
         time.sleep(10)


     #search buses
     def search_bus_partner(self):
        self.driver.find_element(By.XPATH,"//div[contains(text(),'Bus Partner')]").click()
        search_bus = self.driver.find_elements(By.XPATH,"//div[contains(@class,'scrollable-container filter-container primary hide-scrollbar')]//div[contains(@class,'primary')]//div//label")
        # print("prl bus search len",len(search_bus))
        # print("busses list:",search_bus)

        for bus in search_bus:
            if bus.text == "Haritha Travels":
                print("Haritha BUS is SATISFIED:",bus)
                bus.click()
                break
        time.sleep(10)
     #
     # #search seats
     def search_seat(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Select Seats']").click()
        time.sleep(5)
        searching_seats = self.driver.find_elements(By.XPATH,"//*[@id='seat-layout-details']//td//button/span")
        time.sleep(5)


        for seats in searching_seats:
            if seats.text == "U2":
                print("seat condition is satisfied",seats)

                seats.click()
                break
        time.sleep(15)
     #
     # boarding point
     def boarding_point(self):
        boarding=self.driver.find_elements(By.XPATH,"//div[@class='scrollable-container place-container primary ']//div[@class='label']/p[1]")
        time.sleep(5)

        for board in boarding:
            if board.text == "MARTHAHALLI (MULTIPLEX)":
                print("boarding point condition is satisfied",board)
                board.click()
                break
        time.sleep(10)

     def continue_button(self):
        self.driver.find_element(By.XPATH,"//*[@class='container card discount-message-wrapper selected-seat-details  sm ']//button").click()
        time.sleep(10)

     # #passenger_details
     def passenger_details(self):
        name = self.driver.find_element(By.XPATH,"//input[@type='text']")
        time.sleep(5)
        name.send_keys("Narendra")

        age = self.driver.find_element(By.XPATH,"//input[@placeholder='Age']")
        time.sleep(5)
        age.send_keys("22")

        gender = self.driver.find_element(By.XPATH,"//*[@class='btn btn-gender filled primary md inactive button']")
        time.sleep(5)
        gender.click()


        mail = self.driver.find_element(By.XPATH,"//*[@class='container email-input  ']//input")
        time.sleep(5)
        mail.send_keys("nr785849@gmail.com")


        button = self.driver.find_element(By.XPATH,"//*[@class='btn  filled primary md inactive button']")
        time.sleep(10)
        button.click()
        print("continue button is satisfied",button)

     #payment details
     def payments(self):
         payment_type = self.driver.find_elements(By.XPATH,"//*[@class='container paymentOptionList ']//a//span[2]")
         # print("payment is satisfied",payment_type)
         time.sleep(10)

         for payment in payment_type:
             print("list of payments:",payment.text)
             if payment.text == "PhonePe":
                 print("phone pay satisfied",payment)
                 payment.click()
                 break
         time.sleep(10)
     # proceed pay button

     def proceed_button(self):
         proceed_pay = self.driver.find_element(By.XPATH,"//button[@class='btn  filled primary md inactive button']")
         time.sleep(10)
         proceed_pay.click()
         time.sleep(5)

     #
     def close_browser(self):
        self.driver.quit()



abhibus = AbhiBusAutomation()
abhibus.open_website()
abhibus.login_with_otp()
abhibus.from_to_details()
abhibus.bus_type()
abhibus.search_bus_partner()
abhibus.search_seat()
abhibus.boarding_point()
abhibus.continue_button()
abhibus.passenger_details()
abhibus.payments()
abhibus.proceed_button()
abhibus.close_browser()
