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

links2 = {}

folder_name = '/Users/vincentcarse/Downloads/adam/'
options = webdriver.ChromeOptions()
prefs={"download.default_directory" : folder_name}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver',options=options)
driver.get('https://commons.wikimedia.org/wiki/Category:Official_United_Kingdom_Parliamentary_photographs_2017')
#first 'continue' button (gets us onto SAS database)
for  i in range(25):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='galleryfilename galleryfilename-truncate']")))
    tiles = driver.find_elements_by_xpath("//a[@class='galleryfilename galleryfilename-truncate']")
    length = len(tiles)
    for i in range(len(tiles)):
        driver.find_elements_by_xpath("//a[@class='galleryfilename galleryfilename-truncate']")[i].click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='internal']")))
        links2.update({driver.find_elements_by_xpath("//a[@class='internal']")[0].get_attribute('title'):driver.find_elements_by_xpath("//a[@class='internal']")[0].get_attribute('href')})
        time.sleep(1)
        driver.back()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='galleryfilename galleryfilename-truncate']")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'next page')]")))
    driver.find_elements_by_xpath("//*[contains(text(), 'next page')]")[0].click()
driver.close()

#need to find next page...




#used driver.find_elements_by_xpath("//input[@type='submit' and @value='Continue']")[0]  as well
