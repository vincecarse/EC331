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
'11-12':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2012/xplore/setcamps.sas&year4=2012&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'10-11':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2011/xplore/setcamps.sas&year4=2011&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'09-10':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2010/xplore/setcamps.sas&year4=2010&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'08-09':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2009/xplore/setcamps.sas&year4=2009&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'07-08':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2008/xplore/setcamps.sas&year4=2008&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'06-07':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2007/xplore/setcamps.sas&year4=2007&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'05-06':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2006/xplore/setcamps.sas&year4=2006&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'04-05':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2005/xplore/setcamps.sas&year4=2005&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'03-04':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2004/xplore/setcamps.sas&year4=2004&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'02-03':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2003/xplore/setcamps.sas&year4=2003&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'01-02':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2002/xplore/setcamps.sas&year4=2002&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'00-01':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2001/xplore/setcamps.sas&year4=2001&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'99-00':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=2000/xplore/setcamps.sas&year4=2000&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'98-99':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=1999/xplore/setcamps.sas&year4=1999&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'97-98':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=1998/xplore/setcamps.sas&year4=1998&_program=perfrept.perfmast.sas&sumlev=C&steps=2',
'96-97':'https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&prgopt=1997/xplore/setcamps.sas&year4=1997&_program=perfrept.perfmast.sas&sumlev=C&steps=2',

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
    docs = os.listdir(folder_name)
    for j in docs:
        os.rename(folder_name+j,
        folder_name+j[:-3]+'csv')
    driver.close()








#May need to be able to save files by name

list_of_files = glob.glob(folder_name+'*')
latest_file = max(list_of_files, key=os.path.getctime)
new_name = cat_names_list[k]+'.xls'
os.rename(latest_file,new_name)





#used driver.find_elements_by_xpath("//input[@type='submit' and @value='Continue']")[0]  as well
