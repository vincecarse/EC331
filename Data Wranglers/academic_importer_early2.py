#11-12 doesn't have many files

import pandas as pd
import numpy as np

files = {}

def academic_importer(finish_year):
    if finish_year>10:
        year_span = str(finish_year-1)+'-'+str(finish_year)
    if finish_year == 10:
        year_span = '09-10'
    if finish_year<10:
        year_span = str(0)+str(finish_year-1)+'-'+str(0)+str(finish_year)
    file = {}
    if finish_year == 11:
        for i in range(2,14):
            file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/ctaks'+str(i)+'.csv', dtype = str)})
    elif finish_year == 12:
        for i in range(1,5):
            file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/ctaks'+str(i)+'.csv', dtype = str)})
    else:
        for i in range(1,14):
            file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/ctaks'+str(i)+'.csv', dtype = str)})
    if finish_year<7:
        file.update({'SAT':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/ccadcomp.csv', dtype = str)})
    else:
        file.update({'SAT':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/ccad.csv', dtype = str)})
    file.update({'staff_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/cstaf.csv', dtype = str)})
    file.update({'stud_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/cstud.csv', dtype = str)})
    file.update({'ref':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/cref.csv', dtype = str)})
    file.update({'attend':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/cothr.csv', dtype = str)})
    return(file)

for i in range(3,12):
    files.update({i:academic_importer(i)})

def school_sorter(data):
    for i in data:
        data[i]['hs'] = data[i]['ref'][data[i]['ref']['GRDSPAN']=='09 - 12']['CAMPUS']
        data[i]['ms'] = data[i]['ref'][data[i]['ref']['GRDSPAN']=='06 - 08']['CAMPUS']
        data[i]['js_pk'] = data[i]['ref'][data[i]['ref']['GRDSPAN']=='PK - 05']['CAMPUS']
        data[i]['js_ee'] = data[i]['ref'][data[i]['ref']['GRDSPAN']=='EE - 05']['CAMPUS']

school_sorter(files)

def column_extractor(data,code,name):
    file = data[code].copy()
    file.name = name
    return(file)

def columns_extractor(data,codes,names):
    file = data[codes].copy()
    file.columns = names
    file.index = data['CAMPUS'].values
    return(file)

#are the storage codes changing over time?
def info(data,school_type):
    for i in data:
        storage = []
        if school_type == 'hs':
            storage.append(columns_extractor(data[i]['stud_info'],['CPETG09C', 'CPETG10C', 'CPETG11C', 'CPETG12C']\
                                            ,['gr9_stu_count', 'gr10_stu_count', 'gr11_stu_count', 'gr12_stu_count']))
        elif school_type == 'ms':
            storage.append(columns_extractor(data[i]['stud_info'],['CPETG06C', 'CPETG07C', 'CPETG08C']\
                                            ,['gr6_stu_count', 'gr7_stu_count', 'gr8_stu_count']))
        elif (school_type == 'js_ee')|(school_type == 'js_pk'):
            storage.append(columns_extractor(data[i]['stud_info'],['CPETG03C', 'CPETG04C', 'CPETG05C']\
                                            ,['gr3_stu_count', 'gr4_stu_count', 'gr5_stu_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['CPETBLAC', 'CPETALLC', 'CPETWHIC']\
                                        ,['black_stu_count', 'all_stu_count', 'white_stu_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['CPETGIFC', 'CPETSPEC', 'CPETECOC']\
                                        ,['gifted_stu_count', 'spec_ed_stu_count', 'econ_dis_stu_count']))
        storage.append(columns_extractor(data[i]['staff_info'],['CPCTENGA', 'CPCTMATA', 'CPCTSCIA']\
                                        ,['eng_class_size', 'math_class_size', 'sci_class_size']))
        storage.append(columns_extractor(data[i]['staff_info'],['CPSTEXPA', 'CPSTTOSA','CPSTTOFC']\
                                        ,['teacher_experience', 'teacher_avg_salary', 'teacher_fte']))
        storage.append(columns_extractor(data[i]['ref'],['COUNTY', 'CFLCHART']\
                                        ,['county_num', 'charter_school']))
        if i<11:
            storage.append(columns_extractor(data[i]['attend'],['CA0AT'+str(0)+str(i-1)+'R']\
                                            ,['attendance']))
        else:
            storage.append(columns_extractor(data[i]['attend'],['CA0AT'+str(i-1)+'R']\
                                            ,['attendance']))
        file = pd.concat(storage,axis=1,join = 'outer')
        file['CAMPUS'] = file.index
        file['DISTRICT'] = file['CAMPUS'].str.slice(0,6)
        if school_type == 'hs':
            file = file[file['CAMPUS'].isin(data[i]['hs'])]
            data[i]['hs_info'] = file
        elif school_type == 'ms':
            file = file[file['CAMPUS'].isin(data[i]['ms'])]
            data[i]['ms_info'] = file
        elif (school_type == 'js_ee'):
            file = file[file['CAMPUS'].isin(data[i]['js_ee'])]
            data[i]['js_ee_info'] = file
        elif (school_type == 'js_pk'):
            file = file[file['CAMPUS'].isin(data[i]['js_pk'])]
            data[i]['js_pk_info'] = file

info(files,'hs')
info(files,'ms')
info(files,'js_ee')
info(files,'js_pk')

for i in range(3,12):
    for j in ['hs_info', 'ms_info', 'js_ee_info', 'js_pk_info']:
        if i<10:
            files[i][j].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_academic/'+str(j)+str(0)+str(i)+'.csv')
        else:
            files[i][j].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_academic/'+str(j)+str(i)+'.csv')

def hs_academic(data):
    for i in data:
        storage = []
        if i<11:
            storage.append(columns_extractor(data[i]['SAT'],['CA0CS'+str(0)+str(i-1)+'R', 'CA0CA'+str(0)+str(i-1)+'R']\
                                            ,['SAT_avg', 'ACT_avg']))
        else:
            storage.append(columns_extractor(data[i]['SAT'],['CA0CS'+str(i-1)+'R', 'CA0CA'+str(i-1)+'R']\
                                            ,['SAT_avg', 'ACT_avg']))
        file = pd.concat(storage,axis=1,join = 'outer')
        file['CAMPUS'] = file.index
        file = file[file['CAMPUS'].isin(data[i]['hs'])]
        file['DISTRICT'] = file['CAMPUS'].str.slice(0,6)
        data[i]['hs_acam'] = file
hs_academic(files)

for i in range(3,12):
    for j in ['hs_acam']:
        files[i][j].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_academic/'+str(j)+str(i)+'.csv')


#also need english and algebra averages
