
# coding: utf-8

#  
# 
# # Deliverables:
# 
# Scrape list of doctors at Kaiser Permanente, Northern California Region within the 
# 
# Redwood City Office.
# https://healthy.kaiserpermanente.org/northern-california/doctors-locations#/search-result
# 
#  
# 
# 
# # Description:
# 
# Please write a scraper with which you can scrape the following details. Get at least 50 Physician with following details. Show the code and implementation details.
# 
# Physician Name: Stella Sarang Abhyankar, MD
# 
# Physician Specialty: Hospital Medicine
# 
# Practicing Address:
# 
#     Redwood City Medical Center
#     1150 Veterans Blvd 
#     Redwood City, CA 94063
#     
# Phone: 650-299-2000
#  
#  
#  


get_ipython().system('pip install splinter')



# Dependencies

# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
from selenium import webdriver
from splinter import Browser
from bs4 import BeautifulSoup  
import requests
import tweepy
import yaml
import pandas as pd
import time
import re
import pymongo



#driver = webdriver.Chrome('/path/to/chromedriver') 
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)



# Scrape the Kaiser Redwood city office site in northern california. 
kaiser_url = "https://healthy.kaiserpermanente.org/northern-california/doctors-locations#/search-form"  
response = requests.get(kaiser_url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

# To understand the data before collecting from the web.
print(soup.prettify())
 

# Visit website using Splinter
browser.visit(kaiser_url)


# Select California - Northern from dropdown menu
browser.select("Region", "NCA")

# Select Redwood City from City dropdown
browser.select("city-dropdown-li", "Redwood City")

 

# Select doctors at Kaiser Permanente, Northern California Region within the Redwood City Office 
browser.click_link_by_id('searchButton')


# list of physicians dictionary
list_of_physicians = {} 
 
#loop through all the physicians 20 * 3 to get the 60 doctors. 20 from each page.

browser.visit(url)
for x in range(3):

    #loop through all the 20 Physicians from each pagination.
    #results = soup.find_all('div', class_='tab content')
    results = soup.find_all("div")
    print(results)

    Practicing_Address = []
    for r in results:
        el = r.find_all("div", class_="result-list")
        each_dr = el.find("div", class_="detail-data") #each dr info

        # Create BeautifulSoup object; parse with 'html.parser'
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        Physician Name = soup.find("a", class_="bold-font doctorTitle").get_text()

        Physician Specialty = soup.find("div", class_="specialtyMarginlineSpacing").strip()

        medical_location = soup.find("span")[0].text
        street_address = soup.find("span")[1].text
        city = soup.find("span")[2].text
        state = soup.find("span")[3].text
        zipcode = soup.find("span")[4].text

        # Keep a dictionary for each hemisphere. The dictionary contains the title and the feature image.
        Practicing_Adress.append({"medical_location": medical_location, 
                                  "street_address": street_address,
                                  "city": city,
                                  "state": state,
                                  "zipcode": zipcode})

        Phone = soup.find("div", class_"doctorPhone")[none].text()
        

       # Add  all the data collected to list_of_physicians dictionary
       list_of_physicians["Physician Name"] = Physician Name
       list_of_physicians["Physician Specialty"] = Physician Specialty
       list_of_physicians["Practicing_Adress"] = Practicing_Adress
       list_of_physicians["Phone"] = Phone
       
       # Click and go to next page for scraping the  20 pysicians 
       browser.click_link_by_text(`a' 'pagination')

# Print the list of all the doctors.
list_of_physicians



