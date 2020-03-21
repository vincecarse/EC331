import pandas as pd
import numpy as np

files = {}

def academic_importer(finish_year):
    year_span = str(finish_year-1)+'-'+str(finish_year)
    file = {}
    for i in range(1,8):
        file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DSTAAR'+str(i)+'.csv', dtype = str)})
    file.update({'SAT':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DCAD.csv', dtype = str)})
    file.update({'staff_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DSTAF.csv', dtype = str)})
    file.update({'stud_info':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DSTUD.csv', dtype = str)})
    file.update({'ref':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DREF.csv', dtype = str)})
    file.update({'fin':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/ISD_Financial_Reports/Districts/'+year_span+'.csv', dtype = str)})
    file.update({'attend':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+year_span+'/DOTHR.csv', dtype = str)})
    return(file)

for i in range(13,18):
    files.update({i:academic_importer(i)})

#there are also other types of schools

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
def info(data):
    for i in data:
        storage = []
        storage.append(columns_extractor(data[i]['stud_info'],['DPETG03C', 'DPETG04C', 'DPETG05C']\
                                            ,['gr3_stu_count', 'gr4_stu_count', 'gr5_stu_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['DPETG06C', 'DPETG07C', 'DPETG08C']\
                                            ,['gr6_stu_count', 'gr7_stu_count', 'gr8_stu_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['DPETG09C', 'DPETG10C', 'DPETG11C', 'DPETG12C']\
                                            ,['gr9_stu_count', 'gr10_stu_count', 'gr11_stu_count', 'gr12_stu_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['DPETBLAC', 'DPETALLC', 'DPETASIC', 'DPETWHIC']\
                                        ,['black_stu_count', 'all_stu_count', 'asian_stu_count', 'white_stu_count']))
        storage.append(columns_extractor(data[i]['stud_info'],['DPETGIFC', 'DPETSPEC', 'DPETECOC']\
                                        ,['gifted_stu_count', 'spec_ed_stu_count', 'econ_dis_stu_count']))
        storage.append(columns_extractor(data[i]['staff_info'],['DPCTG03A', 'DPCTG04A', 'DPCTG05A','DPCTG06A']\
                                        ,['gr3_class_size', 'gr4_class_size', 'gr5_class_size', 'gr6_class_size']))
        storage.append(columns_extractor(data[i]['staff_info'],['DPCTENGA', 'DPCTMATA', 'DPCTSCIA']\
                                        ,['eng_class_size', 'math_class_size', 'sci_class_size']))
        storage.append(columns_extractor(data[i]['staff_info'],['DPSTEXPA', 'DPSTTOSA','DPSTTOFC']\
                                        ,['teacher_experience', 'teacher_avg_salary', 'teacher_fte']))
        storage.append(columns_extractor(data[i]['ref'],['COUNTY', 'DFLCHART']\
                                        ,['county_num', 'charter_district']))
        storage.append(columns_extractor(data[i]['attend'],['DA0AT'+str(i-1)+'R']\
                                        ,['attendance']))
        file = pd.concat(storage,axis=1,join = 'outer')
        data[i]['info'] = file

info(files)


for i in range(13,18):
    files[i]['info'].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_dist_academic/info'+str(i)+'.csv')

def hs_academic(data):
    for i in data:
        storage = []
        storage.append(columns_extractor(data[i]['SAT'],['DA0CSA'+str(i-1)+'R', 'DA0CAA'+str(i-1)+'R', 'DA0CT'+str(i-1)+'R']\
                                        ,['SAT_avg', 'ACT_avg','SAT/ACT_pct']))
        if i==13:
            storage.append(columns_extractor(data[i]['edu3'],['DA00AA115'+str(i)+'R', 'DA00AR115'+str(i)+'R', 'DA00AUS15'+str(i)+'R']\
                                            ,['EOC_alg1_avg', 'EOC_eng1_avg', 'EOC_his_avg']))
        else:
            storage.append(columns_extractor(data[i]['edu3'],['DA00AA11S'+str(i)+'R', 'DA00AR11S'+str(i)+'R', 'DA00AUS1S'+str(i)+'R']\
                                            ,['EOC_alg1_avg', 'EOC_eng1_avg', 'EOC_his_avg']))
        file = pd.concat(storage,axis=1,join = 'outer')
        file['DISTRICT'] = file.index
        data[i]['hs_acam'] = file
hs_academic(files)
files[16]['hs_acam']


for i in range(13,18):
    for j in ['hs_acam']:
        files[i][j].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_dist_academic/'+str(j)+str(i)+'.csv')





#Deal w later




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
        file['DISTRICT'] = file.index
        file = file[file['DISTRICT'].isin(data[i]['ms'])]
        file['DISTRICT'] = file['DISTRICT'].str.slice(0,6)
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
        file['DISTRICT'] = file.index
        file1 = file[file['DISTRICT'].isin(data[i]['js_ee'])]
        data[i]['js_ee_acam'] = file1
        file2 = file[file['DISTRICT'].isin(data[i]['js_pk'])]
        data[i]['js_pk_acam'] = file2
        file1['DISTRICT'] = file1['DISTRICT'].str.slice(0,6)
        file2['DISTRICT'] = file2['DISTRICT'].str.slice(0,6)
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
