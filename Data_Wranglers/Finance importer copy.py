import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#importing financial report data, academic performance data and school info data
colnames = ['DISTRICT','FUND','FUNCTION',\
'OBJECT','FIN_UNIT','PROGRAM_INTENT','FUNDYEAR','ACTAMT','DTUPDATE',]
a = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/16-17/CSTUD.csv', dtype =str)
x = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/ISD_Financial_Reports/Actual/Actual17/ACTUAL_2017F.TXT', names = colnames, dtype = str)
y = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/16-17/CSTAAR2.csv', dtype =str)
z = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/16-17/CREF.csv', dtype = str)
x['CAMPUS'] = (x['DISTRICT']+x['FIN_UNIT'])

#general financial info for schools in grades 6-8
#then spending on a specific program (Obj 6119 is wages for teachers, prg intent 11 is basic education)
ms = x[x['CAMPUS'].isin(z[z['GRDSPAN']=='06 - 08']['CAMPUS'].values)]
edex = ms[(ms['OBJECT']==str(6119))&(ms['PROGRAM_INTENT']==str(11))][['ACTAMT','CAMPUS']]
edex['ACTAMT'] = edex['ACTAMT'].astype(int)
edex.index = range(len(edex.index))

#summming all entries for specific program spending
df = pd.DataFrame()
df['ACTAMT'] = edex.groupby('CAMPUS')['ACTAMT'].sum()
df['CAMPUS'] = edex.groupby('CAMPUS')['ACTAMT'].sum().index
df.index = range(len(df['ACTAMT'].values))

#academic performance of campuses spanning grades 6-8
#then the three STAAR measures
data = y[y['CAMPUS'].isin(z[z['GRDSPAN']=='06 - 08']['CAMPUS'].values)]
perform = data[['CAMPUS','CA06AMA1S17R', 'CA07AMA1S17R', 'CA08AMA1S17R']]

#finding the campuses for which there is financial and academic data
#then creating a dataframe containing all the relevant info
#also adding in data on number of students per school
reg_data = perform[perform['CAMPUS'].isin(df['CAMPUS'])]
reg_data.index = range(len(reg_data['CAMPUS'].values))
reg_data['teacher_spend'] = df['ACTAMT']
students = a[a['CAMPUS'].isin(z[z['GRDSPAN']=='06 - 08']['CAMPUS'].values)][['CAMPUS','CPETALLC']]
students = students[students['CAMPUS'].isin(df['CAMPUS'])]
students.index = range(len(students['CAMPUS'].values))
reg_data['students'] = students[students['CAMPUS'].isin(df['CAMPUS'])]['CPETALLC']
reg_data[['teacher_spend','students']] = reg_data[['teacher_spend','students']].astype(int)

#cleaning data
reg_data = reg_data.replace('.',np.nan)
reg_data = reg_data.replace('-1',np.nan)
reg_data = reg_data.dropna()


reg_data.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/reg_data.csv')

#Want to create classes to extract different variables
#Start with spending by code


def spending_extractor(file, object, prog_intent):
    df = file[(file['OBJECT']==str(object))&(file['PROGRAM_INTENT']==str(prog_intent))]
    return(df)

#get the rows from one dataframe which satisfy a condition on another??
#reindex?
def cross_checker(file1,file2,column1,column2,condition):
    df = file1[file1[column1].isin(file2[condition][column2].values)]
    return(df)
        
def performance_cleaner(data):
    data = data.replace('.',np.nan)
    data = data.replace('-1',np.nan)
    data = data.dropna()
    return(data)

def group_duplicates(data,col1,col2):
    df = pd.DataFrame()
    df[col1] = data.groupby(col1)[col2].sum()
    df[col2] = data.groupby(col1)[col2].sum().index
    df.index = range(len(df[col2].values))
    return(df)

#
