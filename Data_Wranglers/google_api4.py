import pandas as pd
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

adj_pan = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel2.csv')

try:
    adj_pan['adj_dist'] = adj_pan['adj_dist'].str[2:-2].str.split("', '")
    a = []
    for i in adj_pan.index:
        x = adj_pan['adj_dist_schools'][i][2:-2].replace("'",'').split("], [")
        b = [i.split(', ') for i in x]
        a.append(b)
    adj_pan['adj_dist_schools'] = a
except AttributeError:
    print('n/a')


for i in range(955):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver', options = options)
    driver.get('https://www.google.com/maps/dir/?api=1&origin='+adj_pan['Location'][0]+'&destination='+adj_pan['Location'][0]+'&travelmode=driving')
    c = []
    d = []
    k = 0
    for j in adj_pan['schools'][i]:
        k += 1
        print((adj_pan['Location'][i],j))
        if not (adj_pan['Location'][i] == j):
            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='directions-searchbox-0']")))
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='directions-searchbox-1']")))
                driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[0].clear()
                driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[1].clear()
                driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[0].send_keys(adj_pan['Location'][i]+Keys.ENTER)
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
                    driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[0].send_keys(adj_pan['Location'][i]+Keys.ENTER)
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
            driver.get('https://www.google.com/maps/dir/?api=1&origin='+adj_pan['Location'][0]+'&destination='+adj_pan['Location'][0]+'&travelmode=driving')
            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='directions-searchbox-0']")))
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='directions-searchbox-1']")))
                driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[0].clear()
                driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[1].clear()
                driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[0].send_keys(adj_pan['Location'][i]+Keys.ENTER)
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
    adj_pan['Distance_min'] = pd.Series(a)
    adj_pan['Distance_miles'] = pd.Series(b)
    print(adj_pan['Distance_min'])
    print(adj_pan['Distance_miles'])
    adj_pan.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel.csv')
    driver.close()
