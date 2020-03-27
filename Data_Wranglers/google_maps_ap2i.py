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

small_pan = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel.csv')

try:
    small_pan['schools'] = small_pan['schools'].str[2:-2].str.split("', '")
    small_pan['Distance_min'] = small_pan['Distance_min'].str[2:-2].str.split("', '")
    small_pan['Distance_miles'] = small_pan['Distance_miles'].str[2:-2].str.split("', '")
except AttributeError:
    print('n/a')

a = list(small_pan['Distance_min'].dropna().values)
b = list(small_pan['Distance_miles'].dropna().values)

for i in range(182,955):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver', options = options)
    driver.get('https://www.google.com/maps/dir/?api=1&origin='+small_pan['Location'][0]+'&destination='+small_pan['Location'][0]+'&travelmode=driving')
    c = []
    d = []
    k = 0
    for j in small_pan['schools'][i]:
        k += 1
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
                time.sleep(2)
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
                    c.append('error')
                    d.append('error')
                #should it record something about an error being flagged?
        if (k%20 == 0)&(k>0):
            print('restarting driver')
            driver.close()
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver', options = options)
            driver.get('https://www.google.com/maps/dir/?api=1&origin='+small_pan['Location'][0]+'&destination='+small_pan['Location'][0]+'&travelmode=driving')
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



## may need for adjacent districts

dist_data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Texas_School_GIS/AdjacentDistrict.csv', dtype = str)
