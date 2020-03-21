import pandas as pd
import numpy as np

colnames = ['DISTRICT','FUND','FUNCTION','OBJECT','FIN_UNIT','PROGRAM_INTENT','FUNDYEAR','ACTAMT','DTUPDATE']
actual = {}

for i in range(7,19):
    if i<10:
        actual.update({i:'/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/ISD_Financial_Reports/Actual/Actual'+str(0)+str(i)+'/ACTUAL_'+str(200)+str(i)+'F.TXT'})
    else:
        actual.update({i:'/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/ISD_Financial_Reports/Actual/Actual'+str(i)+'/ACTUAL_'+str(20)+str(i)+'F.TXT'})

for i in actual:
    actual[i] = pd.read_csv(actual[i], names = colnames, dtype = str)
    actual[i]['CAMPUS'] = (actual[i]['DISTRICT']+actual[i]['FIN_UNIT'])
    print(str(i)+' is done importing.')

def spending_extractor(file, object, prog_intent,columns):
    df = file[(file['OBJECT']==str(object))&(file['PROGRAM_INTENT']==str(prog_intent))][columns]
    df.index = range(len(df.index))
    return(df)

def spending_extractor_simple(file, object,columns):
    df = file[file['OBJECT']==str(object)][columns]
    df.index = range(len(df.index))
    return(df)

def group_duplicates(data,col1,col2):
    df = pd.DataFrame()
    file=data.copy()
    file[col2] = file[col2].astype(int)
    df[col2] = file.groupby(col1)[col2].sum()
    df[col1] = file.groupby(col1)[col2].sum().index
    df[col2] = df[col2].astype(int)
    df.index = range(len(df[col2].values))
    return(df)

def add_finances(data1, data2, name):
    data2.index = data2['CAMPUS'].values
    data1[name] = data2['ACTAMT']
    return(data1)

def dict_updater(data1,data2,name,obj,prog_intent,simple=False):
    if simple:
        data1.update({name:spending_extractor_simple(data2,obj,['ACTAMT','CAMPUS'])})
        data1.update({name:group_duplicates(data1[name],'CAMPUS','ACTAMT')})
    else:
        data1.update({name:spending_extractor(data2,obj,prog_intent,['ACTAMT','CAMPUS'])})
        data1.update({name:group_duplicates(data1[name],'CAMPUS','ACTAMT')})

def finance_creator(source):
    finances = pd.DataFrame()
    files = {}
    dict_updater(files,source,'general_wages',6119,11)
    dict_updater(files,source,'athletics_wages',6119,91)
    dict_updater(files,source,'gifted_wages',6119,21)
    dict_updater(files,source,'accelerated_wages',6119,24)
    dict_updater(files,source,'disability_wages',6119,23)
    dict_updater(files,source,'billingual_wages',6119,25)
    dict_updater(files,source,'bond_interest',6521,11,True)
    dict_updater(files,source,'debt_interest',6523,91,True)
    dict_updater(files,source,'rent',5743,21,True)
    dict_updater(files,source,'athletics',5752,24,True)
    dict_updater(files,source,'per_capita_ASF',5811,23,True)
    dict_updater(files,source,'foundational_school',5812,25,True)
    dict_updater(files,source,'school_lunch',5922,11,True)
    dict_updater(files,source,'bond_principal',6511,91,True)
    dict_updater(files,source,'prof_services',6219,21,True)
    dict_updater(files,source,'utilities',6259,24,True)
    dict_updater(files,source,'USDA_donations',6344,23,True)
    dict_updater(files,source,'overtime',6121,25,True)
    dict_updater(files,source,'land_purchase',6619,25,True)
    for i in files:
        add_finances(finances,files[i],i)
    return(finances)

cleaned_actual = {}
for i in actual:
    cleaned_actual[i] = finance_creator(actual[i])
    print(str(i)+' is done formatting.')

for i in cleaned_actual:
    cleaned_actual[i].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_actual/actual'+str(i)+'.csv')

actual_total = pd.DataFrame()
for i in cleaned_actual:
    for j in cleaned_actual[i]:
        actual_total[str(j)+str(i)] = cleaned_actual[i][j]
actual_total.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_actual/actual_total.csv')


#
files = {}
source = actual[7]
dict_updater(files,source,'general_wages',6119,11)
dict_updater(files,source,'accelerated_wages',6119,24)
dict_updater(files,source,'disability_wages',6119,23)
dict_updater(files,source,'bond_interest',6521,11,True)
dict_updater(files,source,'debt_interest',6523,91,True)
dict_updater(files,source,'rent',5743,21,True)
dict_updater(files,source,'athletics',5752,24,True)
dict_updater(files,source,'per_capita_ASF',5811,23,True)
dict_updater(files,source,'foundational_school',5812,25,True)
dict_updater(files,source,'school_lunch',5922,11,True)

test = finance_creator(actual[12])


#not storing all the entries, only those with the same campus ID as 2007 general_wages


#
