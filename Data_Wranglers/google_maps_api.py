import time

import pandas as pd
import selenium
from selenium import webdriver

school_data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Nutrition_Reimbursement/2017-18/School_Nutrition_Programs___Contact_Information_and_Site-Level_Program_Participation___Program_Year_2017-2018.csv', dtype = str)
school_data = school_data.rename(columns = {'CEName':'dist_name'})
school_data['Location'] = school_data['SiteName'].str.replace(' ','+')+'+'+school_data['dist_name'].str.replace(' ','+')
dist_data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Texas_School_GIS/AdjacentDistrict.csv', dtype = str)
panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel.csv', dtype = str)
sub_schools = school_data[(school_data['Grade3']=='Y')&(school_data['Grade4']=='Y')&(school_data['Grade5']=='Y')]
sub_schools['Campus'] = sub_schools['CountyDistrictCode'].str[:]+sub_schools['SiteID'].str[1:]
test = panel[panel['Year']=='2005'].sort_values('dist_name')
test = test[test['Campus'].isin(sub_schools['Campus'].values)]
panel = panel[panel['Campus'].isin(test['Campus'].values)]

camps = []
for i in panel['dist_name'].unique():
    camps.append(list(list(sub_schools[sub_schools['dist_name']==i]['Location'].unique())))

camps_in_dists = pd.DataFrame(panel['dist_name'].unique(), columns = ['dist_name'])
camps_in_dists['schools'] = camps



loc_col = sub_schools[['Campus','dist_name','Location']]


pre_merge = pd.merge(loc_col, camps_in_dists, on = 'dist_name')

merged_dfs = pd.merge(test,pre_merge, on = 'Campus')

merged_dfs




for schools in camps_in_dists['schools']:
    for j in schools:
        driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver')
        driver.get('https://www.google.com/maps/search/?api=1&query='+j)
        time.sleep(1)
        driver.close()



















panel['Campus'].values


sub_schools['CampusID'].dropna().astype(int).sort_values()












test[['Campus','District','dist_name']]

school_data['CountyDistrictCode']

1903101


'220001' in sub_schools['CountyDistrictCode'].str[:]+sub_schools['SiteID'].str[1:]


test[test['District'] == '003906']


https://www.google.com/maps/search/?api=1&query=centurylink+field
https://www.google.com/maps/dir/?api=1&origin=RONALD+REAGAN+MS+TX&destination=Rodriguez+Middle+School+TX&travelmode=driving
