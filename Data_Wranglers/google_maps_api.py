import time

import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

school_data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Nutrition_Reimbursement/2017-18/School_Nutrition_Programs___Contact_Information_and_Site-Level_Program_Participation___Program_Year_2017-2018.csv', dtype = str)
school_data = school_data.rename(columns = {'CEName':'dist_name'})
school_data['Location'] = school_data['SiteName'].str.replace(' ','+')+'+'+school_data['dist_name'].str.replace(' ','+')
panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel.csv', dtype = str)
sub_schools = school_data[(school_data['Grade3']=='Y')&(school_data['Grade4']=='Y')&(school_data['Grade5']=='Y')]
sub_schools['Campus'] = sub_schools['CountyDistrictCode'].str[:]+sub_schools['SiteID'].str[1:]
small_pan = panel[panel['Year']=='2005'].sort_values('dist_name')
small_pan = small_pan[small_pan['Campus'].isin(sub_schools['Campus'].values)]
panel = panel[panel['Campus'].isin(small_pan['Campus'].values)]

camps = []
for i in panel['dist_name'].unique():
    camps.append(list(list(sub_schools[sub_schools['dist_name']==i]['Location'].unique())))

camps_in_dists = pd.DataFrame(panel['dist_name'].unique(), columns = ['dist_name'])
camps_in_dists['schools'] = camps
locations = sub_schools[['Campus','dist_name','Location']]
pre_merge = pd.merge(locations, camps_in_dists, on = 'dist_name')
small_pan = pd.merge(small_pan,pre_merge, on = 'Campus')
small_pan['Distance_min'] = np.nan
small_pan['Distance_miles'] = np.nan

a = []
b = []
for i in range(955):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver', options = options)
    driver.get('https://www.google.com/maps/dir/?api=1&origin='+small_pan['Location'][0]+'&destination='+small_pan['Location'][0]+'&travelmode=driving')
    c = []
    d = []
    for j in small_pan['schools'][i]:
        print((small_pan['Location'][i],j))
        if not (small_pan['Location'][i] == j):
            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='directions-searchbox-0']")))
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='directions-searchbox-1']")))
                driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[0].clear()
                driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[1].clear()
                driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[0].send_keys(small_pan['Location'][i]+Keys.ENTER)
                driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[1].send_keys(j+Keys.ENTER)
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='section-directions-trip-numbers']")))
                x = driver.find_elements_by_xpath("//div[@class='section-directions-trip-numbers']")[0]
                y = x.text.split('\n')[0].split(' ')[0]
                z = x.text.split('\n')[1].split(' ')[0]
                c.append(y)
                d.append(z)
            except (IndexError, TimeoutException):
                print('error')
    a.append(c)
    b.append(d)
    small_pan['Distance_min'] = pd.Series(a)
    small_pan['Distance_miles'] = pd.Series(b)
    print(small_pan['Distance_min'])
    print(small_pan['Distance_miles'])
    small_pan.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel.csv')
    driver.close()






    driver.get('https://www.google.com/maps/dir/?api=1&origin='+small_pan['Location'][i]+'&destination='+j+'&travelmode=driving')





## may need for adjacent districts

dist_data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Texas_School_GIS/AdjacentDistrict.csv', dtype = str)
