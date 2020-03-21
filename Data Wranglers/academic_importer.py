import pandas as pd
import numpy as np

files = {}

def academic_importer(finish_year):
    year_span = str(finish_year-1)+'-'+str(finish_year)
    file = {}
    for i in range(1,8):
        file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/CSTAAR'+str(i)+'.csv', dtype = str)})
    file.update({'SAT':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/CCAD.csv', dtype = str)})
    file.update({'staff_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/CSTAF.csv', dtype = str)})
    file.update({'stud_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/CSTUD.csv', dtype = str)})
    file.update({'ref':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/CREF.csv', dtype = str)})
    file.update({'attend':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+year_span+'/COTHR.csv', dtype = str)})
    return(file)

for i in range(13,18):
    files.update({i:academic_importer(i)})

#there are also other types of schools
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
        storage.append(columns_extractor(data[i]['stud_info'],['CPETBLAC', 'CPETALLC', 'CPETASIC', 'CPETWHIC']\
                                        ,['black_stu_count', 'all_stu_count', 'asian_stu_count', 'white_stu_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['CPETGIFC', 'CPETSPEC', 'CPETECOC']\
                                        ,['gifted_stu_count', 'spec_ed_stu_count', 'econ_dis_stu_count']))
        storage.append(columns_extractor(data[i]['staff_info'],['CPCTENGA', 'CPCTMATA', 'CPCTSCIA']\
                                        ,['eng_class_size', 'math_class_size', 'sci_class_size']))
        storage.append(columns_extractor(data[i]['staff_info'],['CPSTEXPA', 'CPSTTOSA','CPSTTOFC']\
                                        ,['teacher_experience', 'teacher_avg_salary', 'teacher_fte']))
        storage.append(columns_extractor(data[i]['ref'],['COUNTY', 'CFLCHART']\
                                        ,['county_num', 'charter_school']))
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

for i in range(13,18):
    for j in ['hs_info', 'ms_info', 'js_ee_info', 'js_pk_info']:
        files[i][j].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_academic/'+str(j)+str(i)+'.csv')

def hs_academic(data):
    for i in data:
        storage = []
        storage.append(columns_extractor(data[i]['SAT'],['CA0CSA'+str(i-1)+'R', 'CA0CAA'+str(i-1)+'R']\
                                        ,['SAT_avg', 'ACT_avg']))
        if i==13:
            storage.append(columns_extractor(data[i]['edu3'],['CA00AA115'+str(i)+'R', 'CA00AR115'+str(i)+'R', 'CA00AUS15'+str(i)+'R']\
                                            ,['EOC_alg1_avg', 'EOC_eng1_avg', 'EOC_his_avg']))
        else:
            storage.append(columns_extractor(data[i]['edu3'],['CA00AA11S'+str(i)+'R', 'CA00AR11S'+str(i)+'R', 'CA00AUS1S'+str(i)+'R']\
                                            ,['EOC_alg1_avg', 'EOC_eng1_avg', 'EOC_his_avg']))
        file = pd.concat(storage,axis=1,join = 'outer')
        file['CAMPUS'] = file.index
        file = file[file['CAMPUS'].isin(data[i]['hs'])]
        file['DISTRICT'] = file['CAMPUS'].str.slice(0,6)
        data[i]['hs_acam'] = file
hs_academic(files)
files[16]['hs_acam']

#no math data for 2014-15??

def ms_academic(data):
    for i in data:
        storage = []
        if i==13:
            storage.append(columns_extractor(data[i]['edu2'],['CA06AMA15'+str(i)+'R', 'CA06ARE15'+str(i)+'R', 'CA07AMA15'+str(i)+'R', 'CA07ARE15'+str(i)+'R']\
                                            ,['gr6_math_avg', 'gr6_ela_avg', 'gr7_math_avg', 'gr7_ela_avg']))
            storage.append(columns_extractor(data[i]['edu2'],['CA07AWR15'+str(i)+'R', 'CA08AMAS5'+str(i)+'R', 'CA08ARES5'+str(i)+'R', 'CA08ASC15'+str(i)+'R']\
                                            ,['gr7_writ_avg', 'gr8_math_avg', 'gr8_ela_avg', 'gr8_sci_avg']))
        elif i==15:
            storage.append(columns_extractor(data[i]['edu2'],['CA06ARE1S'+str(i)+'R', 'CA07ARE1S'+str(i)+'R']\
                                            ,['gr6_ela_avg', 'gr7_ela_avg']))
            storage.append(columns_extractor(data[i]['edu2'],['CA07AWR1S'+str(i)+'R', 'CA08ARE1S'+str(i)+'R', 'CA08ASC1S'+str(i)+'R']\
                                            ,['gr7_writ_avg', 'gr8_ela_avg', 'gr8_sci_avg']))
        else:
            storage.append(columns_extractor(data[i]['edu2'],['CA06AMA1S'+str(i)+'R', 'CA06ARE1S'+str(i)+'R', 'CA07AMA1S'+str(i)+'R', 'CA07ARE1S'+str(i)+'R']\
                                            ,['gr6_math_avg', 'gr6_ela_avg', 'gr7_math_avg', 'gr7_ela_avg']))
            storage.append(columns_extractor(data[i]['edu2'],['CA07AWR1S'+str(i)+'R', 'CA08AMA1S'+str(i)+'R', 'CA08ARE1S'+str(i)+'R', 'CA08ASC1S'+str(i)+'R']\
                                            ,['gr7_writ_avg', 'gr8_math_avg', 'gr8_ela_avg', 'gr8_sci_avg']))
        file = pd.concat(storage,axis=1,join = 'outer')
        file['CAMPUS'] = file.index
        file = file[file['CAMPUS'].isin(data[i]['ms'])]
        file['DISTRICT'] = file['CAMPUS'].str.slice(0,6)
        data[i]['ms_acam'] = file
ms_academic(files)
files[16]['ms_acam']

def js_academic(data):
    for i in data:
        storage = []
        if i==13:
            storage.append(columns_extractor(data[i]['edu1'],['CA03AMA15'+str(i)+'R', 'CA03ARE15'+str(i)+'R', 'CA04AMA15'+str(i)+'R', 'CA04ARE15'+str(i)+'R']\
                                            ,['gr3_math_avg', 'gr3_ela_avg', 'gr4_math_avg', 'gr4_ela_avg']))
            storage.append(columns_extractor(data[i]['edu1'],['CA04AWR15'+str(i)+'R', 'CA05AMAS5'+str(i)+'R', 'CA05ARES5'+str(i)+'R', 'CA05ASC15'+str(i)+'R']\
                                            ,['gr4_writ_avg', 'gr5_math_avg', 'gr5_ela_avg', 'gr5_sci_avg']))
        elif i==15:
            storage.append(columns_extractor(data[i]['edu1'], ['CA03ARE1S'+str(i)+'R', 'CA04ARE1S'+str(i)+'R']\
                                            ,['gr3_ela_avg', 'gr4_ela_avg']))
            storage.append(columns_extractor(data[i]['edu1'],['CA04AWR1S'+str(i)+'R', 'CA05ARE1S'+str(i)+'R', 'CA05ASC1S'+str(i)+'R']\
                                            ,['gr4_writ_avg', 'gr5_ela_avg', 'gr5_sci_avg']))
        else:
            storage.append(columns_extractor(data[i]['edu1'],['CA03AMA1S'+str(i)+'R', 'CA03ARE1S'+str(i)+'R', 'CA04AMA1S'+str(i)+'R', 'CA04ARE1S'+str(i)+'R']\
                                            ,['gr3_math_avg', 'gr3_ela_avg', 'gr4_math_avg', 'gr4_ela_avg']))
            storage.append(columns_extractor(data[i]['edu1'],['CA04AWR1S'+str(i)+'R', 'CA05AMA1S'+str(i)+'R', 'CA05ARE1S'+str(i)+'R', 'CA05ASC1S'+str(i)+'R']\
                                            ,['gr4_writ_avg', 'gr5_math_avg', 'gr5_ela_avg', 'gr5_sci_avg']))
        file = pd.concat(storage,axis=1,join = 'outer')
        file['CAMPUS'] = file.index
        file1 = file[file['CAMPUS'].isin(data[i]['js_ee'])]
        data[i]['js_ee_acam'] = file1
        file2 = file[file['CAMPUS'].isin(data[i]['js_pk'])]
        data[i]['js_pk_acam'] = file2
        file1['DISTRICT'] = file1['CAMPUS'].str.slice(0,6)
        file2['DISTRICT'] = file2['CAMPUS'].str.slice(0,6)
js_academic(files)
files[16]['js_ee_acam']
files[16]['js_pk_acam']


for i in range(13,18):
    for j in ['hs_acam', 'ms_acam', 'js_ee_acam', 'js_pk_acam']:
        files[i][j].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_academic/'+str(j)+str(i)+'.csv')




#had to drop Math/English SATs
#'CA0CSM'+str(i-1)+'R', 'CA0CSE'+str(i-1)+'R',
#'SAT_math_avg', 'SAT_ela_avg',
#        storage.append(columns_extractor(data[i]['SAT'],['CA0CAM'+str(i-1)+'R', 'CA0CAE'+str(i-1)+'R', 'CA0CAC'+str(i-1)+'R']\
#                                        ,['ACT_math_avg', 'ACT_ELA_avg', 'ACT_sci_avg']))

# need to deal with 17-18 seperately


#for i in range(3,9):
#    files17_18.update({i:'/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/17-18/CSTAAR_GR'+str(i)+'.csv'})
#
#files17_18.update({'SAT':'/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/17-18/CCAD.csv'})
#files17_18.update({'staff_info':'/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/17-18/CSTAF.csv'})
#files17_18.update({'stud_info':'/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/17-18/CSTUD.csv'})

#
