import logging

# Step 1: Create and configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('student_data.log')

# Set log level for handlers
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

# Create formatters and add them to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
class Student:
    def __init__(self, boys, girls, passes, fails):
        self.boys = boys
        self.girls = girls
        self.passes = passes
        self.fails = fails
        self.total_students = boys + girls
        logger.debug("Initialized Student data")

    def display_student_info(self):
        logger.info("Displaying student information")
        print(f"Total students: {self.total_students}")
        print(f"Total boys: {self.boys}")
        print(f"Total girls: {self.girls}")
        print(f"Passes: {self.passes}")
        print(f"Fails: {self.fails}")

def student_data(boys, girls, passes, fails):
    student = Student(boys, girls, passes, fails)
    student.display_student_info()
    logger.debug("Displayed student information")

# Creating a student and displaying information
student=student_data(80, 40, 90, 30)
logger.debug("creating student_data object")
print(student)
logger.info("Finished the student_data function")

import requests
import json

class Student:
    def __init__(self, boys, girls, passes, fails):
        self.boys = boys
        self.girls = girls
        self.passes = passes
        self.fails = fails
        self.total_students = boys + girls

    def display_student_info(self):
        print(f"Total students: {self.total_students}")
        print(f"Total boys: {self.boys}")
        print(f"Total girls: {self.girls}")
        print(f"Passes: {self.passes}")
        print(f"Fails: {self.fails}")

    def student_data(self, url):
        payload = {
            "boys": self.boys,
            "girls": self.girls,
            "passes": self.passes,
            "fails": self.fails,
            "total_students": self.total_students
        }
        logger.debug(f"Sending POST request to {url} with payload: {payload}")
        # Send the POST request with JSON payload
        response = requests.post(url, json=payload)

        # Check the response status
        if response.status_code == 200:
            logger.info("Data successfully posted to the API!")
            print("Data successfully posted to the API!")
            logger.debug(f"Response JSON: {response.json()}")
            print(response.json())  # Print the response JSON for verification
        else:
            logger.error(f"Failed to post data. Status code: {response.status_code}")
            logger.debug(f"Response text: {response.text}")
            print(f"Failed to post data. Status code: {response.status_code}")
            print(f"Response: {response.text}")

def student_data(boys, girls, passes, fails):
    student = Student(boys, girls, passes, fails)
    student.display_student_info()
    logger.debug("Displayed student information")
    return student

# Example usage
logger.debug("Starting the student_data function")
student = student_data(80, 40, 90, 30)
url = 'https://httpbin.org/post'# Replace with your actual API URL
logger.debug("Posting student data to the API")
student.student_data(url)

import requests
import csv

class Student:
    def __init__(self, boys, girls, passes, fails):
        self.boys = boys
        self.girls = girls
        self.passes = passes
        self.fails = fails
        self.total_students = boys + girls

def fetch_student_data(url):
    logger.debug(f"Fetching student data from URL: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        logger.info("Data fetched successfully from the API")
        return response.json()  # Assuming the response is JSON format
    else:
        logger.error(f"Failed to fetch data from the API. Status code: {response.status_code}")
        return None

def write_to_csv(data, filename):
    logger.debug(f"Writing data to CSV file: {filename}")
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Boys', 'Girls', 'Passes', 'Fails', 'Total Students'])
        writer.writerow([
            data.get('boys', 80),  # Use data.get() to handle missing keys gracefully
            data.get('girls', 40),
            data.get('passes', 90),
            data.get('fails', 30),
            data.get('total_students',120)
        ])
        logger.info(f"Data has been written to {filename}")
# Example usage
url = 'https://httpbin.org/get'  # Replace with your actual API URL
logger.debug("Starting the data fetching process")
student_data = fetch_student_data(url)
if student_data:
    write_to_csv(student_data, 'students_get.csv')
    logger.debug("Data fetching and writing to CSV process completed")
    print("Data has been written to students_get.csv")
else:
    logger.error("Failed to fetch data from the API")
    print("Failed to fetch data from the API.")


import pandas as pd

class Student:
    def __init__(self, boys, girls, passes, fails):
        self.boys = boys
        self.girls = girls
        self.passes = passes
        self.fails = fails
        self.total_students = boys + girls

    def display_student_info(self):
        print(f"Total students: {self.total_students}")
        print(f"Total boys: {self.boys}")
        print(f"Total girls: {self.girls}")
        print(f"Passes: {self.passes}")
        print(f"Fails: {self.fails}")

def student_data(boys, girls, passes, fails):
    student = Student(boys, girls, passes, fails)
    student.display_student_info()
    return student

# Creating a student and displaying information
student = student_data(80, 40, 90, 30)

# Creating a DataFrame
logger.debug("Creating DataFrame from student data")
data = {
    'Boys': [student.boys],
    'Girls': [student.girls],
    'Passes': [student.passes],
    'Fails': [student.fails],
    'Total Students': [student.total_students]
}
df = pd.DataFrame(data)
logger.info("DataFrame created successfully")
# Save DataFrame to CSV
csv_filename = 'students_data.csv'
logger.debug(f"Saving DataFrame to CSV file: {csv_filename}")
df.to_csv(csv_filename, index=False)
logger.info(f"Data has been written to {csv_filename}")
print("Data has been written to students_data.csv")


import matplotlib.pyplot as plt
import pandas as pd

class Student:
    def __init__(self, boys, girls, passes, fails):
        self.boys = boys
        self.girls = girls
        self.passes = passes
        self.fails = fails
        self.total_students = boys + girls

    def display_student_info(self):
        print(f"Total students: {self.total_students}")
        print(f"Total boys: {self.boys}")
        print(f"Total girls: {self.girls}")
        print(f"Passes: {self.passes}")
        print(f"Fails: {self.fails}")

def student_data(boys, girls, passes, fails):
    student = Student(boys, girls, passes, fails)
    student.display_student_info()
    return student

# Creating a student and displaying information
student = student_data(80, 40, 90, 30)
logger.debug("creating the dataframe")
data = {
    "students": ["total_students","Boys", "Girls", "Passes", "Fails"],
    "results": [student.total_students,student.boys, student.girls, student.passes, student.fails]
}
df = pd.DataFrame(data)
logger.info("dataframe created successfully")

logger.debug("Creating bar plot for student data")
plt.bar(df['students'], df['results'],color=['red','blue','green','pink','orange'])
plt.title('total_Students results')
plt.xlabel('students')
plt.ylabel('results')
plt.show()
logger.info("Bar plot created successfully")

excel_filename = 'student_data.xlsx'
logger.debug(f"Saving DataFrame to Excel file: {excel_filename}")
df.to_excel(excel_filename, index=False)
logger.info(f"Data successfully written to {excel_filename} file!")

print("Data successfully written to student_data.xlsx file!")
