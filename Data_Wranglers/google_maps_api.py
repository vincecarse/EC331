import time

import pandas as pd
import selenium
from selenium import webdriver

school_data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Nutrition_Reimbursement/2017-18/School_Nutrition_Programs___Contact_Information_and_Site-Level_Program_Participation___Program_Year_2017-2018.csv', dtype = str)
school_data = school_data.rename(columns = {'CEName':'dist_name'})
school_data['locations'] = school_data['SiteName'].str.replace(' ','+')+'+'+school_data['dist_name'].str.replace(' ','+')
dist_data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Texas_School_GIS/AdjacentDistrict.csv')
panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel.csv')

for i in school_data['locations']:
    driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver')
    driver.get('https://www.google.com/maps/search/?api=1&query='+i)
    time.sleep(1)
    driver.close()


##
## What do i want to find?
## Distance to other schools?
##  specific type?
##  elementary only?


## want a list of all the schools in each district
##
a = []
for i in panel['dist_name'].unique():
    a.append(list(list(school_data[school_data['dist_name']==i]['locations'].unique())))

for i in x['dist_name'].unique():
    x.set_value(i,'schools',list(school_data[school_data['dist_name']==i]['locations'].unique()))



for i in x['dist_name'].unique():
    x.at[i,'schools'] = school_data[school_data['dist_name']==i]['locations'].unique()


for i in x['dist_name'].unique():
    x.at[i,'schools'] = [1]



x = pd.DataFrame(panel['dist_name'].unique(), columns = ['dist_name'])
x.index = x.dist_name
x['schools'] = 0



panel['Campus'].unique()

dist_data['ad_name_1'][4]


school_data[(school_data['Grade3']=='Y')&(school_data['Grade4']=='Y')&(school_data['Grade5']=='Y')]

school_data[school_data['CEName'].isin(panel.dist_name.unique())]

pd.merge(school_data,panel,how = 'inner', on = 'dist_name')



panel[panel['dist_name'] == 'EDGEWOOD ISD']


panel[panel['dist_name'] == dist_data['ad_name_1'][48].upper()]


dist_data['ad_name_1'][4].upper()









https://www.google.com/maps/search/?api=1&query=centurylink+field
https://www.google.com/maps/dir/?api=1&origin=RONALD+REAGAN+MS+TX&destination=Rodriguez+Middle+School+TX&travelmode=driving
