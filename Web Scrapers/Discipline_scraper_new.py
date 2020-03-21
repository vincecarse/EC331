#Much faster/easier scraper for discipline data


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
'17-18a':'https://rptsvr1.tea.texas.gov/adhocrpt/Disciplinary_Data_Products/Download_Region_Districts.html',
'16-17a':'https://rptsvr1.tea.texas.gov/adhocrpt/Disciplinary_Data_Products/Download_Region_Districts.html',
'15-16a':'https://rptsvr1.tea.texas.gov/adhocrpt/Disciplinary_Data_Products/Download_Region_Districts.html'}

files={'17-18a':'/Users/vincentcarse/Desktop/Thesis/Texas_Education/Data/Campus_Academic_Performance/17-18/CREF.dat',
'16-17a':'/Users/vincentcarse/Desktop/Thesis/Texas_Education/Data/Campus_Academic_Performance/16-17/CREF.dat',
'15-16a':'/Users/vincentcarse/Desktop/Thesis/Texas_Education/Data/Campus_Academic_Performance/15-16/CREF.dat'}


for i in links:
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
    menu = Select(driver.find_elements_by_xpath("//select[@name='school_yr']")[0])
    #chooses year
    if i=='17-18a':
        menu.select_by_index(1)
    elif i=='16-17a':
        menu.select_by_index(2)
    elif i=='15-16a':
        menu.select_by_index(3)
    #chooses csv
    button = driver.find_elements_by_xpath("//input[@name='report_type' and @id='Select_District_Summary_CSV']")[0]
    button.click()
    time.sleep(0.5)
    menu1 = Select(driver.find_elements_by_xpath("//select[@name='region']")[0])
    num_options = int(str(len(menu1.options)))
    for l in range(num_options):
        menu1.select_by_index(l)
        button = driver.find_elements_by_xpath("//input[@name='Download_District_Summaries_Regn']")[0]
        button.click()
        time.sleep(0.5)
    time.sleep(0.5)
    driver.close()
