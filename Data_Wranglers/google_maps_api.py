import time

import pandas as pd
import selenium
from selenium import webdriver

school_data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Nutrition_Reimbursement/2017-18/School_Nutrition_Programs___Contact_Information_and_Site-Level_Program_Participation___Program_Year_2017-2018.csv')
school_locations = x['SiteName'].str.replace(' ','+')+'+'+x['CEName'].str.replace(' ','+')

dist_data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Texas_School_GIS/AdjacentDistrict.csv')

info_file['Campus'].unique()

dist_data['ad_name_1']

for i in school_locations:
    driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver')
    driver.get('https://www.google.com/maps/search/?api=1&query='+i)
    time.sleep(1)
    driver.close()


##
## What do i want to find?
## Distance to other schools?
##  specific type?
##  elementary only?

school_data[(school_data['Grade3']=='Y')&(school_data['Grade4']=='Y')&(school_data['Grade5']=='Y')]


https://www.google.com/maps/search/?api=1&query=centurylink+field
https://www.google.com/maps/dir/?api=1&origin=RONALD+REAGAN+MS+TX&destination=Rodriguez+Middle+School+TX&travelmode=driving
