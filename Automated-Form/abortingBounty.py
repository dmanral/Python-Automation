# Selenium imports.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Other imports.
import time
import csv
import random

# My custom data imports (its just a python file with a big list).
from q1Data import q1_answers
from q2Data import q2_answers
from q3Data import q3_answers

# Geography.
class Location:
    def __init__(self, zip, type, decommissioned, primary_city, acceptable_cities, 
                 unacceptable_cities, state, county, timezone, area_codes, world_region, 
                 country, latitude, longitude, irs_estimated_population):
        self.zip = zip
        self.type = type
        self.decommissioned = decommissioned
        self.primary_city = primary_city
        self.acceptable_cities = acceptable_cities
        self.unacceptable_cities = unacceptable_cities
        self.state = state
        self.county = county
        self.timezone = timezone
        self.area_codes = area_codes
        self.world_region = world_region
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.irs_estimated_population = irs_estimated_population

# Reading the csv file with geography items needed in the form.
fileName = "cityZipCounty.csv"
with open(fileName, 'r') as csvfile:
    csvreader = list(csv.reader(csvfile))
lengthOfCsv = len(csvreader)
# Randomly select a row in the csv.
position = random.randrange(0, lengthOfCsv)
geo = Location(*csvreader[position])

# Selenium stuff.
webForm = webdriver.Chrome()
webForm.get('https://prolifewhistleblower.com/anonymous-form/')     # The form we are filling out.
time.sleep(3)

# How do you think the law has been violated?
firstQuestion = webForm.find_element_by_xpath('//*[@id="forminator-field-textarea-1"]')     # Location of question 1.
firstAnswer = random.choice(q1_answers)                                                     # Answer for question 1.
firstQuestion.send_keys(firstAnswer)                                                        # Auto fill question 1.

# How did you obtain this evidence?
secondQuestion = webForm.find_element_by_xpath('//*[@id="forminator-field-text-1"]')
secondAnswer = random.choice(q2_answers)
secondQuestion.send_keys(secondAnswer)


# Clinic or Doctor this evidence relates to:
thirdQuestion = webForm.find_element_by_xpath('//*[@id="forminator-field-text-6"]')
thirdAnswer = random.choice(q3_answers)
thirdQuestion.send_keys(thirdAnswer)

# City
fourthQuestion = webForm.find_element_by_xpath('//*[@id="forminator-field-text-2"]')
city = geo.primary_city
fourthQuestion.send_keys(city)


# State
fifthQuestion = webForm.find_element_by_xpath('//*[@id="forminator-field-text-3"]')
state = "Texas"
fifthQuestion.send_keys(state)

# Zip
sixthQuestion = webForm.find_element_by_xpath('//*[@id="forminator-field-text-4"]')
zip = geo.zip
sixthQuestion.send_keys(zip)

# County
seventhQuestion = webForm.find_element_by_xpath('//*[@id="forminator-field-text-5"]')
county = geo.county
seventhQuestion.send_keys(county)

# Are you currently elected to public office?
eighthQuestion = webForm.find_element_by_xpath('//*[@id="checkbox-1"]/div/label[2]/span[1]')
eighthQuestion.click()