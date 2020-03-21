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

folder_name = '/Users/vincentcarse/Downloads/adam/'
options = webdriver.ChromeOptions()
prefs={"download.default_directory" : folder_name}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver',options=options)
driver.get('https://commons.wikimedia.org/wiki/Category:Official_United_Kingdom_Parliamentary_photographs_2017')
#first 'continue' button (gets us onto SAS database)
for i in range(25):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='galleryfilename galleryfilename-truncate']")))
    tiles = driver.find_elements_by_xpath("//a[@class='galleryfilename galleryfilename-truncate']")
    length = len(tiles)
    for j in range(len(tiles)):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='galleryfilename galleryfilename-truncate']")))
        driver.find_elements_by_xpath("//a[@class='galleryfilename galleryfilename-truncate']")[j].click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='internal']")))
        links.update({driver.find_elements_by_xpath("//a[@class='internal']")[0].get_attribute('title'):driver.find_elements_by_xpath("//a[@class='internal']")[0].get_attribute('href')})
        driver.back()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'next page')]")))
        driver.find_elements_by_xpath("//*[contains(text(), 'next page')]")[0].click()
    except ValueError:
        print('p')


https://commons.wikimedia.org/w/index.php?title=Category:Official_United_Kingdom_Parliamentary_photographs_2017&from=A

links3 = links


for i in links:
    urllib.request.urlretrieve(links[i], '/Users/vincentcarse/Downloads/adam/'+i)

#####
https://commons.wikimedia.org/wiki/Category:Official_United_Kingdom_Parliamentary_photographs_2017

https://commons.wikimedia.org/w/index.php?title=Category:Official_United_Kingdom_Parliamentary_photographs_2017&from=W
#####

        links.update({tiles[j].get_attribute('title'):tiles[j].get_attribute('href')})
    driver.find_elements_by_xpath("//*[contains(text(), 'next page')]")[0].click()
driver.close()


for i in links:
    driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver',options=options)
    driver.get(links[i])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='internal']")))
    link = driver.find_elements_by_xpath("//a[@class='internal']")[0]
    links2.update({link.get_attribute('title'):link.get_attribute('href')})
    driver.close()




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
