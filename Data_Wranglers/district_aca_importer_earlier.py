#11-12 doesn't have many files

import pandas as pd
import numpy as np

files = {}

def academic_importer(finish_year):
    if finish_year>95:
        year_span = str(finish_year-1)+'-'+str(finish_year)
    if finish_year<95:
        year_span = str(0)+str(finish_year-1)+'-'+str(0)+str(finish_year)
    if finish_year == 0:
        year_span = '99-00'
    file = {}
    for i in ['A','B','C','D','E']:
        file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DISTTAS'+str(i)+'.csv', dtype = str)})
    #    file.update({'SAT':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DISTCOMP.csv', dtype = str)})
    else:
        file.update({'staff_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DISTSTAF.csv', dtype = str)})
        file.update({'stud_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DISTSTUD.csv', dtype = str)})
        file.update({'ref':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DISTREF.csv', dtype = str)})
        file.update({'fin':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DISTFIN.csv', dtype = str)})
        file.update({'attend':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DISTOTHR.csv', dtype = str)})
    return(file)

for i in [97,98,99,0,1,2]:
    if i in [97,98,99]:
        year_num = str(i-1)
    elif i in [1,2]:
        year_num = '0'+str(i-1)
    else:
        year_num = '99'
    files.update({year_num:academic_importer(i)})

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
        storage.append(columns_extractor(data[i]['stud_info'],['DPETG09C', 'DPETG10C', 'DPETG11C', 'DPETG12C']\
                                            ,['gr9_stu_count', 'gr10_stu_count', 'gr11_stu_count', 'gr12_stu_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['DPETBLAC', 'DPETWHIC', 'DPETHISC', 'DPETALLC']\
                                        ,['black_stu_count', 'white_stu_count', 'his_stu_count', 'all_stud_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['DPETGIFC', 'DPETSPEC', 'DPETECOC']\
                                        ,['gifted_stu_count', 'spec_ed_stu_count', 'econ_dis_stu_count']))
        if i in ['99','00','01']:
            storage.append(columns_extractor(data[i]['staff_info'],['DPCTENGA', 'DPCTMATA', 'DPCTSCIA']\
                                            ,['eng_class_size', 'math_class_size', 'sci_class_size']))
        else:
            storage.append(columns_extractor(data[i]['staff_info'],['DPETENGA', 'DPETMATA', 'DPETSCIA']\
                                            ,['eng_class_size', 'math_class_size', 'sci_class_size']))
        storage.append(columns_extractor(data[i]['staff_info'],['DPSTTOSA', 'DPSTEXPA','DPSTTENA']\
                                        ,['teacher_avg_salary', 'teacher_experience', 'exp_w_dist']))

        storage.append(columns_extractor(data[i]['ref'],['DISTNAME','DISTRICT','COUNTY']\
                                            ,['dist_name','dist_num','county_num']))
        storage.append(columns_extractor(data[i]['attend'],['DA0AT'+i+'R']\
                                        ,['attendance']))
        file = pd.concat(storage,axis=1,join = 'outer')
        data[i]['info'] = file
info(files)

for i in files:
    files[i]['info'].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_dist_academic/info'+i+'.csv')

#finance stuff (esp. oil)
oil = pd.DataFrame()
for i in files:
    oil[str(i)] = files[i]['fin']['DPFVOILT']

def hs_academic(data):
    for i in data:
        storage = []
        storage.append(columns_extractor(data[i]['attend'],['DA0CS'+i+'R', 'DA0CA'+i+'R', 'DA0CT'+i+'R']\
                                        ,['SAT_avg', 'ACT_avg','SAT/ACT_pct']))
        file = pd.concat(storage,axis=1,join = 'outer')
        data[i]['hs_acam'] = file
hs_academic(files)

def finance(data):
    for i in data:
        storage = []
        storage.append(columns_extractor(data[i]['fin'],['DPFEALLK', 'DPFVOILT', 'DPFRSTAT']\
                                        ,['exp_per_pupil', 'oil_value','state_rev']))
        file = pd.concat(storage,axis=1,join = 'outer')
        data[i]['finance'] = file
finance(files)

for i in files:
    for j in ['hs_acam']:
        files[i][j].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_dist_academic/'+i+'_hs_acam'+'.csv')



DA0CA03R

DA0CS03R

DA0CT03R
