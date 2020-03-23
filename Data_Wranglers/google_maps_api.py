#google_maps_API
import pandas as pd
import selenium
from selenium import webdriver
import time

https://www.google.com/maps/search/?api=1&query=centurylink+field
https://www.google.com/maps/dir/?api=1&origin=RONALD+REAGAN+MS+TX&destination=Rodriguez+Middle+School+TX&travelmode=driving


x = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Nutrition_Reimbursement/2017-18/School_Nutrition_Programs___Contact_Information_and_Site-Level_Program_Participation___Program_Year_2017-2018.csv')
y = x['SiteName'].str.replace(' ','+')
z = x['CEName'].str.replace(' ','+')
a= y+'+'+z

for i in a:

    driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver')
    driver.get('https://www.google.com/maps/search/?api=1&query='+i)
    time.sleep(1)
    driver.close()
