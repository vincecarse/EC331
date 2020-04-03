import pandas as pd
import time
import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

adj_pan = pd.read_csv('/Users/vincentcarse/Github/EC331/Regression_data/VAM_reg/new_balanced_panel2.csv')

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

#why not 955??

a = list(adj_pan['Distance_adj_min'].dropna().values)
a1 = a[:208]
a2 = a[261:]
b = list(adj_pan['Distance_adj_miles'].dropna().values)
b1 = b[:208]
b2 = b[261:]

for i in range(208,261):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver', options = options)
    driver.get('https://www.google.com/maps/dir/?api=1&origin='+adj_pan['Location'][i]+'&destination='+adj_pan['Location'][i]+'&travelmode=driving')
    c = []
    d = []
    for district in adj_pan['adj_dist_schools'][i]:
        k = 0
        e = []
        f = []
        for school in district:
            k += 1
            print((adj_pan['Location'][i],school))
            if not (adj_pan['Location'][i] == school):
                try:
                    try:
                        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='directions-searchbox-1']")))
                        driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[1].clear()
                        driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[1].send_keys(school+Keys.ENTER)
                        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='section-directions-trip-numbers']")))
                        x = driver.find_elements_by_xpath("//div[@class='section-directions-trip-numbers']")[0].text
                        y = x.split('\n')[0].split(' ')[0]
                        if x.split('\n')[0].split(' ')[1] == 'h':
                            y = str(int(x.split('\n')[0].split(' ')[0])*60+int(x.split('\n')[0].split(' ')[2]))
                        z = x.split('\n')[1].split(' ')[0]
                        e.append(y)
                        f.append(z)
                        print(y,z)
                    except (IndexError, TimeoutException):
                        time.sleep(2)
                        try:
                            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='directions-searchbox-1']")))
                            driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[1].clear()
                            driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[1].send_keys(school+Keys.ENTER)
                            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='section-directions-trip-numbers']")))
                            x = driver.find_elements_by_xpath("//div[@class='section-directions-trip-numbers']")[0].text
                            y = x.split('\n')[0].split(' ')[0]
                            if x.split('\n')[0].split(' ')[1] == 'h':
                                y = str(int(x.split('\n')[0].split(' ')[0])*60+int(x.split('\n')[0].split(' ')[2]))
                            z = x.split('\n')[1].split(' ')[0]
                            e.append(y)
                            f.append(z)
                            print(y,z)
                        except (IndexError, TimeoutException):
                            e.append('error')
                            f.append('error')
                    if (k%20 == 0)&(k>0):
                        driver.close()
                        options = webdriver.ChromeOptions()
                        options.add_argument("--headless")
                        driver = webdriver.Chrome(executable_path='/Users/vincentcarse/Python/chromedriver', options = options)

                        driver.get('https://www.google.com/maps/dir/?api=1&origin='+adj_pan['Location'][i]+'&destination='+adj_pan['Location'][i]+'&travelmode=driving')
                        try:
                                    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='directions-searchbox-1']")))
                                    driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[1].clear()
                                    driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[1].send_keys(school+Keys.ENTER)
                                    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='section-directions-trip-numbers']")))
                                    x = driver.find_elements_by_xpath("//div[@class='section-directions-trip-numbers']")[0].text
                                    y = x.split('\n')[0].split(' ')[0]
                                    if x.split('\n')[0].split(' ')[1] == 'h':
                                        y = str(int(x.split('\n')[0].split(' ')[0])*60+int(x.split('\n')[0].split(' ')[2]))
                                    z = x.split('\n')[1].split(' ')[0]
                                    e.append(y)
                                    f.append(z)
                                    print(y,z)
                        except (IndexError, TimeoutException):
                            time.sleep(2)
                            try:
                                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='directions-searchbox-1']")))
                                driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[1].clear()
                                driver.find_elements_by_xpath("//input[@class='tactile-searchbox-input']")[1].send_keys(school+Keys.ENTER)
                                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='section-directions-trip-numbers']")))
                                x = driver.find_elements_by_xpath("//div[@class='section-directions-trip-numbers']")[0].text
                                y = x.split('\n')[0].split(' ')[0]
                                if x.split('\n')[0].split(' ')[1] == 'h':
                                    y = str(int(x.split('\n')[0].split(' ')[0])*60+int(x.split('\n')[0].split(' ')[2]))
                                z = x.split('\n')[1].split(' ')[0]
                                e.append(y)
                                f.append(z)
                            except (IndexError, TimeoutException):
                                e.append('error')
                                f.append('error')
                except StaleElementReferenceException:
                    e.append('error')
                    f.append('error')
        c.append(e)
        d.append(f)
    a1.append(c)
    b1.append(d)
    adj_pan['Distance_adj_min'] = pd.Series(a1+[['']]*(260-i)+a2)
    adj_pan['Distance_adj_miles'] = pd.Series(b1+[['']]*(260-i)+b2)
    adj_pan.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel2.csv')
    driver.close()
