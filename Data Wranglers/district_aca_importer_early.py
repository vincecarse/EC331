#11-12 doesn't have many files

import pandas as pd
import numpy as np

files = {}

def academic_importer(finish_year):
    if finish_year == 0:
        year_span = '99-00'
    if finish_year>10:
        year_span = str(finish_year-1)+'-'+str(finish_year)
    if finish_year == 10:
        year_span = '09-10'
    if finish_year<10:
        year_span = str(0)+str(finish_year-1)+'-'+str(0)+str(finish_year)
    file = {}
    if finish_year == 11:
        for i in range(2,14):
            file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/dtaks'+str(i)+'.csv', dtype = str)})
    elif finish_year == 12:
        for i in range(1,5):
            file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/dtaks'+str(i)+'.csv', dtype = str)})
    else:
        for i in range(1,14):
            file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/dtaks'+str(i)+'.csv', dtype = str)})
    if finish_year<7:
        file.update({'SAT':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/dcadcomp.csv', dtype = str)})
    else:
        file.update({'SAT':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/dcad.csv', dtype = str)})
    file.update({'staff_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/dstaf.csv', dtype = str)})
    file.update({'stud_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/dstud.csv', dtype = str)})
    file.update({'ref':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/dref.csv', dtype = str)})
    file.update({'fin':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/ISD_Financial_Reports/Districts/'+year_span+'.csv', dtype = str)})
    file.update({'attend':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/dothr.csv', dtype = str)})
    return(file)

for i in range(3,13):
    files.update({i:academic_importer(i)})



def column_extractor(data,code,name):
    file = data[code].copy()
    file.name = name
    return(file)

def columns_extractor(data,codes,names):
    file = data[codes].copy()
    file.columns = names
    file.index = data['DISTRICT'].values
    return(file)

#are the storage codes changing over time?
#are the storage codes changing over time?
def info(data):
    for i in data:
        storage = []
        storage.append(columns_extractor(data[i]['stud_info'],['DPETG03C', 'DPETG04C', 'DPETG05C']\
                                            ,['gr3_stu_count', 'gr4_stu_count', 'gr5_stu_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['DPETG06C', 'DPETG07C', 'DPETG08C']\
                                            ,['gr6_stu_count', 'gr7_stu_count', 'gr8_stu_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['DPETG09C', 'DPETG10C', 'DPETG11C', 'DPETG12C']\
                                            ,['gr9_stu_count', 'gr10_stu_count', 'gr11_stu_count', 'gr12_stu_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['DPETBLAC', 'DPETALLC', 'DPETWHIC']\
                                        ,['black_stu_count', 'all_stu_count', 'white_stu_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['DPETGIFC', 'DPETSPEC', 'DPETECOC']\
                                        ,['gifted_stu_count', 'spec_ed_stu_count', 'econ_dis_stu_count']))
        storage.append(columns_extractor(data[i]['staff_info'],['DPCTG03A', 'DPCTG04A', 'DPCTG05A','DPCTG06A']\
                                        ,['gr3_class_size', 'gr4_class_size', 'gr5_class_size', 'gr6_class_size']))
        storage.append(columns_extractor(data[i]['staff_info'],['DPCTENGA', 'DPCTMATA', 'DPCTSCIA']\
                                        ,['eng_class_size', 'math_class_size', 'sci_class_size']))
        storage.append(columns_extractor(data[i]['staff_info'],['DPSTEXPA', 'DPSTTOSA','DPSTTOFC']\
                                        ,['teacher_experience', 'teacher_avg_salary', 'teacher_fte']))
        if i == 3:
            storage.append(columns_extractor(data[i]['ref'],['COUNTY']\
                                            ,['county_num']))
        else:
            storage.append(columns_extractor(data[i]['ref'],['COUNTY', 'DFLCHART']\
                                            ,['county_num', 'chater_ditrict']))
        if i<11:
            storage.append(columns_extractor(data[i]['attend'],['DA0AT'+str(0)+str(i-1)+'R']\
                                            ,['attendance']))
        else:
            storage.append(columns_extractor(data[i]['attend'],['DA0AT'+str(i-1)+'R']\
                                            ,['attendance']))
        file = pd.concat(storage,axis=1,join = 'outer')
        data[i]['info'] = file
info(files)

for i in range(3,13):
    if i<10:
        files[i]['info'].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_dist_academic/info'+str(0)+str(i)+'.csv')
    else:
        files[i]['info'].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_dist_academic/info'+str(i)+'.csv')


def hs_academic(data):
    for i in data:
        storage = []
        if i<11:
            storage.append(columns_extractor(data[i]['SAT'],['DA0CS'+str(0)+str(i-1)+'R', 'DA0CA'+str(0)+str(i-1)+'R', 'DA0CT'+str(0)+str(i-1)+'R']\
                                            ,['SAT_avg', 'ACT_avg','SAT/ACT_pct']))
        else:
            storage.append(columns_extractor(data[i]['SAT'],['DA0CS'+str(i-1)+'R', 'DA0CA'+str(i-1)+'R', 'DA0CT'+str(i-1)+'R']\
                                            ,['SAT_avg', 'ACT_avg','SAT/ACT_pct']))
        file = pd.concat(storage,axis=1,join = 'outer')
        data[i]['hs_acam'] = file
hs_academic(files)


for i in range(3,13):
    for j in ['hs_acam']:
        files[i][j].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_dist_academic/'+str(j)+str(i)+'.csv')



DA0CA03R

DA0CS03R

DA0CT03R
