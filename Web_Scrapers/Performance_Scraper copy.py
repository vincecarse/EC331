#This scraper uses Selenium to download performance data at the campus level
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
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import glob
import os
import shutil

#Defining links

links={
#'01-02':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2002/xplore/setdists.sas&year4=2002&_program=perfrept.perfmast.sas&sumlev=D&steps=2',
#'00-01':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2001/xplore/setdists.sas&year4=2001&_program=perfrept.perfmast.sas&sumlev=D&steps=2',
#'99-00':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2000/xplore/setdists.sas&year4=2000&_program=perfrept.perfmast.sas&sumlev=D&steps=2',
'98-99':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=1999/xplore/setdists.sas&year4=1999&_program=perfrept.perfmast.sas&sumlev=D&steps=2',
'97-98':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=1998/xplore/setdists.sas&year4=1998&_program=perfrept.perfmast.sas&sumlev=D&steps=2',
'96-97':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=1997/xplore/setdists.sas&year4=1997&_program=perfrept.perfmast.sas&sumlev=D&steps=2',
'95-96':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=1996/xplore/setdists.sas&year4=1996&_program=perfrept.perfmast.sas&sumlev=D&steps=2',
'94-95':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=1995/xplore/setdists.sas&year4=1995&_program=perfrept.perfmast.sas&sumlev=D&steps=2',
'93-94':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=1994/xplore/setdists.sas&year4=1994&_program=perfrept.perfmast.sas&sumlev=D&steps=2',

}

for i in links:
    folder_name = '/Users/vincentcarse/Downloads/'+i+'/'
    os.makedirs(folder_name)
    options = webdriver.ChromeOptions()
    prefs={"download.default_directory" : folder_name}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver',options=options)
    driver.get(links[i])
    #first 'continue' button (gets us onto SAS database)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @value='Continue']")))
    button1 = driver.find_elements_by_xpath("//input[@type='submit' and @value='Continue']")[0]
    button1.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='dsname']")))
    menu = Select(driver.find_elements_by_xpath("//select[@name='dsname']")[0])
    num_options = int(str(len(menu.options)))
    #gets number of options in list of categories
    for k in range(num_options):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='dsname']")))
        menu = Select(driver.find_elements_by_xpath("//select[@name='dsname']")[0])
        menu.select_by_index(k)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @value='Continue']")))
        button1 = driver.find_elements_by_xpath("//input[@type='submit' and @value='Continue']")[0]
        button1.click()
        #clicks each category
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='Button' and @name='selall']")))
        button2 = driver.find_elements_by_xpath("//input[@type='Button' and @name='selall']")[0]
        button2.click()
        #clicks 'select all'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='datafmt']")))
        menu = Select(driver.find_elements_by_xpath("//select[@name='datafmt']")[0])
        menu.select_by_index(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @value='Download']")))
        button3 = driver.find_elements_by_xpath("//input[@type='submit' and @value='Download']")[0]
        button3.send_keys(Keys.RETURN)
        #downloads csvs
        #go back page
        driver.back()
        time.sleep(1)
    time.sleep(10)
    driver.close()









#May need to be able to save files by name

list_of_files = glob.glob(folder_name+'*')
latest_file = max(list_of_files, key=os.path.getctime)
new_name = cat_names_list[k]+'.xls'
os.rename(latest_file,new_name)





#used driver.find_elements_by_xpath("//input[@type='submit' and @value='Continue']")[0]  as well
