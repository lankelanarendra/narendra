from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class indeedAutomation:
     def __init__(self):
         self.driver = webdriver.Chrome()
     def open_website(self):
        self.driver.get("https://secure.indeed.com/auth?hl=en_AU&service=my&co=AU&continue=https%3A%2F%2Fau.indeed.com%2F")
        self.driver.maximize_window()
        time.sleep(10)

     def gmail(self):
         self.driver.find_element(By.NAME,"__email").send_keys("narendralankela@gmail.com")
         time.sleep(5)

     def continue_button(self):
         self.driver.find_element(By.XPATH,"//button[@type='submit']//span").click()
         time.sleep(5)

     def continue_with_google(self):
         self.driver.find_element(By.XPATH,"//*[@id='gsuite-login-google-button']//span").click()
         time.sleep(5)

     # def job_titles(self):
     #     job=self.driver.find_element(By.XPATH,"//*[@id='text-input-what']").send_keys("python developer")
     #     print(job)
     #     time.sleep(5)
     #
     # def job_location(self):
     #     self.driver.find_element(By.Xpath,"//*[@id='text-input-where']").send_keys("Bangalore")
     #     time.sleep(5)

     # def find_jobs(self):
     #     self.driver.find_element(By.XPATH,"//*[@class='yosegi-InlineWhatWhere-primaryButton']").click()
     #     time.sleep(5)
     #
     # def work_mode(self):
     #     self.driver.find_element(By.Xpath,"//*[@id='remote_filter_button']").click()
     #     time.sleep(5)
     #     work_type=self.driver.find_elements(By.Xpath,"//*[@aria-labelledby='remote_filter_button']//a")
     #
     #     for work in work_type:
     #         if work.text == "Hybrid work":
     #             work.click()
     #             break
     #     time.sleep(10)
     #
     # def date_posted(self):
     #     self.driver.find_element(By.Xpath,"//*[@id='fromAge_filter_button']").click()
     #     time.sleep(10)
     #     date_hours=self.driver.find_elements(By.Xpath,"//*[@aria-labelledby='fromAge_filter_button']//a")
     #
     #     for date in date_hours:
     #         if date.text == "Last 24 hours":
     #             date.click()
     #             break
     #     time.sleep(10)
     #
     # def payments(self):
     #     self.driver.find_element(By.Xpath,"//*[@id='salaryType_filter_button']").click()
     #     time.sleep(5)
     #     pay=self.driver.find_elements(By.Xpath,"//*[@aria-labelledby='salaryType_filter_button']//a")
     #
     #     for pays in pay:
     #         if pay.text == "₹ 57,500.00+/month":
     #             pay.click()
     #             break
     #     time.sleep(10)
     #
     # def walk_distance(self):
     #     self.driver.find_element(By.Xpath,"//*[@id='filter-radius']").click()
     #     time.sleep(5)
     #     distance=self.driver.find_elements(By.Xpath,"//*[@class='yosegi-FilterPill-dropdownList']//li//a")
     #
     #     for dis in distance:
     #         if dis.text == "Within 5 kilometres":
     #             dis.click()
     #             break
     #     time.sleep(10)
     #
     # def job_type(self):
     #     self.driver.find_element(By.Xpath,"//*[@id='filter-jobtype1']").click()
     #     jobs=self.driver.find_elements(By.Xpath,"//*[@id='filter-jobtype1-menu']//label//span")
     #
     #     for job in jobs:
     #         if job.text == "Permanent":
     #             job.click()
     #             break
     #     time.sleep(10)
     #     self.driver.find_element(By.Xpath,"//*[@class='css-1vts50e e8ju0x50']").click()
     #     time.sleep(5)
     #
     # def companies(self):
     #     self.driver.find_element(By.Xpath, "//*[@id='filter-jobtype1']").click()
     #     company = self.driver.find_elements(By.Xpath, "//*[@id='menu--4']//a")
     #
     #     for com in company:
     #         if com.text == "Wipro":
     #             com.click()
     #             break
     #     time.sleep(10)
     #
     # def job_languages(self):
     #     self.driver.find_element(By.Xpath, "//*[@id='filter-lang']").click()
     #     languages = self.driver.find_elements(By.Xpath, "//*[@id='filter-lang-menu']//li//a")
     #
     #     for lang in languages:
     #         if lang.text == "English":
     #             lang.click()
     #             break
     #     time.sleep(10)
     #
     # def programing_languages(self):
     #     self.driver.find_element(By.Xpath, "//*[@id='filter-taxo1']").click()
     #     programs = self.driver.find_elements(By.Xpath, "//*[@id='filter-taxo1-menu']//label//span")
     #
     #     for language in programs:
     #         if language.text == "Python":
     #             language.click()
     #             break
     #     time.sleep(10)
     #
     #     self.driver.find_element(By.Xpath,"//*[@form='filter-taxo1-menu']")
     #     time.sleep(5)
     #
     # def education_levels(self):
     #     self.driver.find_element(By.Xpath, "//*[@id='filter-taxo2']").click()
     #     educations = self.driver.find_elements(By.Xpath, "//*[@id='filter-taxo2-menu']//label//span")
     #
     #     for education in educations:
     #         if education.text == "Master's degree":
     #             education.click()
     #             break
     #     time.sleep(10)



indeed=indeedAutomation()
indeed.open_website()
indeed.gmail()
indeed.continue_button()
indeed.continue_with_google()
# indeed.job_titles()
# indeed.job_location()
# indeed.find_jobs()
# indeed.work_mode()
# indeed.date_posted()
# indeed.payments()
# indeed.walk_distance()
# indeed.job_type()
# indeed.companies()
# indeed.job_languages()
# indeed.programing_languages()
# indeed.education_levels()