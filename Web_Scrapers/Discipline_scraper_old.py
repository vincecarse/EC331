#This scraper uses Selenium to download discipline data at the ISD level
# for the school years 2015-16,2016-17, 2017-18. 2018-19 will be released in
# Spring 2020

#Importing relevant packages

from urllib.request import urlopen
import requests
import numpy as np
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
import glob
import os
import shutil

#Defining links/reference files

links={
'17-18':'https://rptsvr1.tea.texas.gov/adhocrpt/Disciplinary_Data_Products/Download_District_Summaries.html',
'16-17':'https://rptsvr1.tea.texas.gov/adhocrpt/Disciplinary_Data_Products/Download_District_Summaries.html',
'15-16':'https://rptsvr1.tea.texas.gov/adhocrpt/Disciplinary_Data_Products/Download_District_Summaries.html'}

files={'17-18':'/Users/vincentcarse/Desktop/Thesis/Texas_Education/Data/Campus_Academic_Performance/17-18/CREF.dat',
'16-17':'/Users/vincentcarse/Desktop/Thesis/Texas_Education/Data/Campus_Academic_Performance/16-17/CREF.dat',
'15-16':'/Users/vincentcarse/Desktop/Thesis/Texas_Education/Data/Campus_Academic_Performance/15-16/CREF.dat'}


for i in links:
    #getting list of unique ISDs from refrence file for each year
    file=pd.read_csv(files[i])
    ISDs=file['DISTRICT'].values
    ISDs=np.unique(ISDs)
    ISDs=ISDs.astype(str)
    for j in range(len(ISDs)):
        if int(ISDs[j])<10000:
            ISDs[j]='00'+ISDs[j]
        elif int(ISDs[j])<100000:
            ISDs[j]='0'+ISDs[j]
    #creates folder
    folder_name = '/Users/vincentcarse/Downloads/'+i+'/'
    os.makedirs(folder_name)
    options = webdriver.ChromeOptions()
    prefs={"download.default_directory" : folder_name}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver',options=options)
    #launches driver
    driver.get(links[i])
    time.sleep(0.5)
    for k in ISDs:
        menu = Select(driver.find_elements_by_xpath("//select[@name='school_yr']")[0])
        #chooses year
        if i=='17-18':
            menu.select_by_index(1)
        elif i=='16-17':
            menu.select_by_index(2)
        elif i=='15-16':
            menu.select_by_index(3)
        #chooses csv
        button = driver.find_elements_by_xpath("//input[@name='report_type' and @value='txt']")[0]
        button.click()
        time.sleep(0.5)
        #chooses 'select by ISD number'
        button = driver.find_elements_by_xpath("//input[@name='list_by' and @id='By_number']")[0]
        button.click()
        time.sleep(0.5)
        #enters text
        text_box = driver.find_elements_by_xpath("//input[@name='numbfrag' and @type='text']")[0]
        text_box.send_keys(k)
        button = driver.find_elements_by_xpath("//input[@type='submit' and @value='Next']")[0]
        button.click()
        time.sleep(0.5)
        button = driver.find_elements_by_xpath("//input[@type='submit' and @value='Next']")[0]
        button.click()
        driver.back()
    time.sleep(0.5)





#
