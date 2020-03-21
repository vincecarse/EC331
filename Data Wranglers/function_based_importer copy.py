import pandas as pd
import numpy as np

#importing financial report data, academic performance data and school info data
colnames = ['DISTRICT','FUND','FUNCTION','OBJECT','FIN_UNIT','PROGRAM_INTENT','FUNDYEAR','ACTAMT','DTUPDATE']
student_info = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/16-17/CSTUD.csv', dtype =str)
spending = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/ISD_Financial_Reports/Actual/Actual17/ACTUAL_2017F.TXT', names = colnames, dtype = str)
performance = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/16-17/CSTAAR2.csv', dtype =str)
reference = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/16-17/CREF.csv', dtype = str)
spending['CAMPUS'] = (spending['DISTRICT']+spending['FIN_UNIT'])

def spending_extractor(file, object, prog_intent,columns):
    df = file[(file['OBJECT']==str(object))&(file['PROGRAM_INTENT']==str(prog_intent))][columns]
    df.index = range(len(df.index))
    return(df)

def cross_checker(file1,file2,column1,column2,condition):
    df = file1[file1[column1].isin(file2[condition][column2].values)]
    df.index = range(len(df.index))
    return(df)

def performance_cleaner(data):
    data = data.replace('.',np.nan)
    data = data.replace('-1',np.nan)
    data = data.dropna()
    data = data.astype(int)
    data.index = range(len(data.values))
    return(data)

def group_duplicates(data,col1,col2):
    df = pd.DataFrame()
    file=data.copy()
    file[col2] = file[col2].astype(int)
    df[col2] = file.groupby(col1)[col2].sum()
    df[col1] = file.groupby(col1)[col2].sum().index
    df[col2] = df[col2].astype(int)
    df.index = range(len(df[col2].values))
    return(df)

#finding spending and academic performance of campuses spanning grades 6-8
#then the three STAAR measures
middle_schools = cross_checker(spending,reference,'CAMPUS','CAMPUS',reference['GRDSPAN']=='06 - 08')
edex = spending_extractor(middle_schools,6119,11,['ACTAMT','CAMPUS'])
edex['ACTAMT'] = edex['ACTAMT'].astype(int)
df = group_duplicates(edex,'CAMPUS','ACTAMT')
data = cross_checker(performance,reference,'CAMPUS','CAMPUS',reference['GRDSPAN']=='06 - 08')
perform = data[['CAMPUS','CA06AMA1S17R', 'CA07AMA1S17R', 'CA08AMA1S17R']]

#finding the campuses for which there is financial and academic data
#then creating a dataframe containing all the relevant info
#also adding in data on number of students per school
reg_data = cross_checker(perform,df,'CAMPUS','CAMPUS',df['ACTAMT']>1)
reg_data['teacher_spend'] = df['ACTAMT']
students = cross_checker(student_info,reference,'CAMPUS','CAMPUS',reference['GRDSPAN']=='06 - 08')
students = cross_checker(students,df,'CAMPUS','CAMPUS',df['ACTAMT']>1)
students = students[['CAMPUS','CPETALLC']]
reg_data['students'] = students['CPETALLC']
reg_data = performance_cleaner(reg_data)
reg_data.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/reg_data_test.csv')
