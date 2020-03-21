#11-12 doesn't have many files

import pandas as pd
import numpy as np

files = {}

for i in range(98,100):
    files.update({str(i-1):''})

files.update({'00':''})

for i in range(1,11):
    files.update({str(0)+str(i-1):''})

for i in range(11,14):
    files.update({str(i-1):''})

def academic_importer_early(finish_year):
    file = {}
    for i in ['A','B','C','D','E']:
        file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/CAMPTAS'+str(i)+'.csv', dtype = str)})
    else:
        file.update({'staff_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/CAMPSTAF.csv', dtype = str)})
        file.update({'stud_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/CAMPSTUD.csv', dtype = str)})
        file.update({'ref':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/CAMPREF.csv', dtype = str)})
        file.update({'fin':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/CAMPFIN.csv', dtype = str)})
        file.update({'attend':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/CAMPOTHR.csv', dtype = str)})
    return(file)

def academic_importer_late(finish_year):
    file = {}
    if finish_year in ['03','04','05','06','07','08','09','10']:
        for i in range(1,14):
            file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/ctaks'+str(i)+'.csv', dtype = str)})
    if finish_year in ['11']:
        for i in range(2,14):
            file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/ctaks'+str(i)+'.csv', dtype = str)})
    if finish_year in ['12']:
        for i in range(1,5):
            file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/ctaks'+str(i)+'.csv', dtype = str)})
    file.update({'staff_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/cstaf.csv', dtype = str)})
    file.update({'stud_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/cstud.csv', dtype = str)})
    file.update({'ref':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/cref.csv', dtype = str)})
    file.update({'fin':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/cfin.csv', dtype = str)})
    file.update({'attend':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/cothr.csv', dtype = str)})
    return(file)

def joint_aca_importer(finish_year):
    if finish_year in ['97','98','99','00','01','02']:
        return(academic_importer_early(finish_year))
    else:
        return(academic_importer_late(finish_year))

for i in files:
    files.update({i:joint_aca_importer(i)})

##works up to here


def column_extractor(data,code,name):
    file = data[code].copy()
    file.name = name
    return(file)

def columns_extractor(data,codes,names):
    file = data[codes].copy()
    file.columns = names
    file.index = data['CAMPUS'].values
    return(file)


def early_info(i, data):
    storage = []
    storage.append(columns_extractor(data['stud_info'],['CPETG09C', 'CPETG10C', 'CPETG11C', 'CPETG12C']\
                                        ,['gr9_stu_count', 'gr10_stu_count', 'gr11_stu_count', 'gr12_stu_count']))
    storage.append(columns_extractor(data['stud_info'],['CPETBLAC', 'CPETWHIC', 'CPETHISC', 'CPETALLC']\
                                    ,['black_stu_count', 'white_stu_count', 'his_stu_count', 'all_stud_count']))
    storage.append(columns_extractor(data['stud_info'],['CPETGIFC', 'CPETSPEC', 'CPETECOC']\
                                    ,['gifted_stu_count', 'spec_ed_stu_count', 'econ_dis_stu_count']))
    #if i in ['99','00','01']:
    #    storage.append(columns_extractor(data['staff_info'],['CPCTENGA', 'CPCTMATA', 'CPCTSCIA']\
    #                                    ,['eng_class_size', 'math_class_size', 'sci_class_size']))
    #else:
    #    storage.append(columns_extractor(data['staff_info'],['CPETENGA', 'CPETMATA', 'CPETSCIA']\
    #                                    ,['eng_class_size', 'math_class_size', 'sci_class_size']))
    storage.append(columns_extractor(data['staff_info'],['CPSTTOSA', 'CPSTEXPA','CPSTTENA']\
                                    ,['teacher_avg_salary', 'teacher_experience', 'exp_w_dist']))
    #storage.append(columns_extractor(data['ref'],['DISTNAME','DISTRICT','COUNTY']\
    #                                    ,['dist_name','dist_num','county_num']))
    #torage.append(columns_extractor(data['attend'],['CA0AT'+i+'R']\
    #                                ,['attendance']))
    file = pd.concat(storage,axis=1,join = 'outer')
    data['info'] = file

def later_info(i, data):
    storage = []
    storage.append(columns_extractor(data['stud_info'],['CPETG09C', 'CPETG10C', 'CPETG11C', 'CPETG12C']\
                                        ,['gr9_stu_count', 'gr10_stu_count', 'gr11_stu_count', 'gr12_stu_count']))
    storage.append(columns_extractor(data['stud_info'],['CPETBLAC', 'CPETWHIC', 'CPETHISC', 'CPETALLC']\
                                    ,['black_stu_count', 'white_stu_count', 'his_stu_count', 'all_stud_count']))
    storage.append(columns_extractor(data['stud_info'],['CPETGIFC', 'CPETSPEC', 'CPETECOC']\
                                    ,['gifted_stu_count', 'spec_ed_stu_count', 'econ_dis_stu_count']))
    #if i in ['99','00','01']:
    #    storage.append(columns_extractor(data['staff_info'],['CPCTENGA', 'CPCTMATA', 'CPCTSCIA']\
    #                                    ,['eng_class_size', 'math_class_size', 'sci_class_size']))
    #else:
    #    storage.append(columns_extractor(data['staff_info'],['CPETENGA', 'CPETMATA', 'CPETSCIA']\
    #                                    ,['eng_class_size', 'math_class_size', 'sci_class_size']))
    storage.append(columns_extractor(data['staff_info'],['CPSTTOSA', 'CPSTEXPA','CPSTTENA']\
                                    ,['teacher_avg_salary', 'teacher_experience', 'exp_w_dist']))
    #storage.append(columns_extractor(data['ref'],['DISTNAME','DISTRICT','COUNTY']\
    #                                    ,['dist_name','dist_num','county_num']))
    #torage.append(columns_extractor(data['attend'],['CA0AT'+i+'R']\
    #                                ,['attendance']))
    file = pd.concat(storage,axis=1,join = 'outer')
    data['info'] = file


def joint_info(finish_year,data):
    if finish_year in ['97','98','99','00','01','02']:
        early_info(finish_year, data)
    else:
        later_info(finish_year, data)

for i in files:
    joint_info(i,files[i])


### none below here has been tested







for i in files:
    files[i]['info'].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_dist_academic/info'+i+'.csv')












#finance stuff (esp. oil)
oil = pd.DataFrame()
for i in files:
    oil[str(i)] = files[i]['fin']['DPFVOILT']

def hs_academic(data):
    for i in data:
        storage = []
        storage.append(columns_extractor(data[i]['attend'],['CA0CS'+i+'R', 'CA0CA'+i+'R', 'CA0CT'+i+'R']\
                                        ,['SAT_avg', 'ACT_avg','SAT/ACT_pct']))
        file = pd.concat(storage,axis=1,join = 'outer')
        data[i]['hs_acam'] = file
hs_academic(files)


for i in files:
    for j in ['hs_acam']:
        files[i][j].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_dist_academic/'+i+'_hs_acam'+'.csv')



DA0CA03R

DA0CS03R

DA0CT03R
