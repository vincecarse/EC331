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
import urllib
import glob
import os
import shutil

#Defining links

links = {}
links2 = {}

folder_name = '/Users/vincentcarse/Downloads/adam1/'
options = webdriver.ChromeOptions()
prefs={"download.default_directory" : folder_name}
options.add_experimental_option('prefs', prefs)
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver',options=options)
driver.get('https://commons.wikimedia.org/wiki/Category:Official_United_Kingdom_Parliamentary_photographs_2017')
#first 'continue' button (gets us onto SAS database)
for i in range(25):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='galleryfilename galleryfilename-truncate']")))
    tiles = driver.find_elements_by_xpath("//a[@class='galleryfilename galleryfilename-truncate']")
    length = len(tiles)
    for j in range(len(tiles)):
        links.update({tiles[j].get_attribute('title'):tiles[j].get_attribute('href')})
        print('first url number  '+str(200*i+j))
    driver.find_elements_by_xpath("//*[contains(text(), 'next page')]")[0].click()
driver.close()


for i in list(links.keys())[3999:]:
    driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver',options=options)
    driver.get(links[i])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='internal']")))
    link = driver.find_elements_by_xpath("//a[@class='internal']")[0]
    links2.update({link.get_attribute('title'):link.get_attribute('href')})
    print('second url number '+str(i))
    driver.close()



for i in links2:
    urllib.request.urlretrieve(links2[i], '/Users/vincentcarse/Downloads/adam/'+i)
    print('img number'+str(i))




#up to  'Official portrait of Suella Fernandes crop 1.jpg': 'https://upload.wikimedia.org/wikipedia/commons/2/21/Official_portrait_of_Suella_Fernandes_crop_1.jpg'

    urllib.request.urlretrieve(links[i], '/Users/vincentcarse/Downloads/adam/'+i+'.jpg')

urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/2/25/Official_portrait_of_Drew_Hendry_crop_1.jpg", "/Users/vincentcarse/Downloads/adam/02000001.jpg")

https://commons.wikimedia.org/wiki/File:Official_portrait_of_Ms_Diane_Abbott_crop_2.jpg

links[list(links.keys())[1]]

https://upload.wikimedia.org/wikipedia/commons/d/db/Official_portrait_of_Steve_Brine_crop_2.jpg
https://upload.wikimedia.org/wikipedia/commons/d/db/Official_portrait_of_Steve_Brine_crop_2.jpg
https://upload.wikimedia.org/wikipedia/commons/d/db/Official_portrait_of_Steve_Brine_crop_2.jpg

https://upload.wikimedia.org/wikipedia/commons/4/48/Official_portrait_of_Andrew_Bridgen_crop_3.jpg
#need to find next page...
        driver.find_elements_by_xpath("//a[@class='galleryfilename galleryfilename-truncate']")[i].click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='internal']")))
        links.update({driver.find_elements_by_xpath("//a[@class='internal']")[0].get_attribute('title'):driver.find_elements_by_xpath("//a[@class='internal']")[0].get_attribute('href')})
        time.sleep(1)
        driver.back()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='galleryfilename galleryfilename-truncate']")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'next page')]")))



#used driver.find_elements_by_xpath("//input[@type='submit' and @value='Continue']")[0]  as well
