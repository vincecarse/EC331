#######README######
#This program imports each nutrition contact info dataset and
#creates a Python object of key info from it. The goal is then to
# use this key info to scrape the websites containing useful data on each school
#or ISD

#importing key packages

import pandas as pd
import numpy as np

##defining paths for site-level info

paths={'a':'/Users/vincentcarse/Desktop/Thesis\
/Texas_Education/Data/Campus_Nutrition_Reimbursement\
/2018-19/School_Nutrition_Programs___Contact_Information\
_and_Site-Level_Program_Participation\
___Program_Year_2018-2019.csv',

'b':'/Users/vincentcarse/Desktop/Thesis\
/Texas_Education/Data/Campus_Nutrition_Reimbursement\
/2017-18/School_Nutrition_Programs___Contact_Information\
_and_Site-Level_Program_Participation\
___Program_Year_2017-2018.csv',

'c':'/Users/vincentcarse/Desktop/Thesis\
/Texas_Education/Data/Campus_Nutrition_Reimbursement\
/2016-17/School_Nutrition_Programs___Contact_Information\
_and_Site-Level_Program_Participation\
___Program_Year_2016-2017.csv',

'd':'/Users/vincentcarse/Desktop/Thesis\
/Texas_Education/Data/Campus_Nutrition_Reimbursement\
/2015-16/School_Nutrition_Programs___Contact_Information\
_and_Site-Level_Program_Participation___Program_Year_2015-2016.csv'}

##creating dictionaries to define variables over

years={'a':'test','b':'test','c':'test','d':'test'}
campuses={'a':'test','b':'test','c':'test','d':'test'}
ISDs={'a':'test','b':'test','c':'test','d':'test'}
data={'a':'test','b':'test','c':'test','d':'test'}
counties={'a':'test','b':'test','c':'test','d':'test'}

#defining class to import each file from csv and extract key info

class importdata:
    def __init__(self,filepath):
        self.data=pd.read_csv(filepath)
        self.campuses=self.data['SiteName']
        self.ISDs=self.data['CEName']
        self.counties=self.data['CECounty']

#writing key info into above variables (and alphabetising the resulting arrays)

for i in years:
    years[i]=importdata(paths[i])
    data[i]=years[i].data
    campuses[i]=years[i].campuses.unique()
    campuses[i].sort()
    ISDs[i]=years[i].ISDs.unique()
    ISDs[i].sort()
    counties[i]=years[i].counties.unique()
    counties[i].sort()

##
