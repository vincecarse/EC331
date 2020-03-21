#11-12 doesn't have many files
#importing is still very messy
#try and get graduation rates for each school

import pandas as pd
import numpy as np

files = {}
def year_creator(data):
    for i in range(98,101):
        data.update({str(i-1):''})

    data.update({'00':''})

    for i in range(1,11):
        data.update({str(0)+str(i-1):''})

    for i in range(11,14):
        data.update({str(i-1):''})

year_creator(files)

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
    if finish_year in ['00','01','02']:
        file.update({'attend':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/CAMPCOMP.csv', dtype = str)})
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
    try:
        file.update({'SAT':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/ccadcomp.csv', dtype = str)})
    except FileNotFoundError:
        file.update({'SAT':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/ccad.csv', dtype = str)})
    try:
        file.update({'attend':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/ccomp.csv', dtype = str)})
    except FileNotFoundError:
        file.update({'attend':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/ccadcomp.csv', dtype = str)})
    file.update({'fin':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/cfin.csv', dtype = str)})
    file.update({'other':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/cothr.csv', dtype = str)})
    return(file)


def joint_aca_importer(finish_year):
    if finish_year in ['97','98','99','00','01','02']:
        return(academic_importer_early(finish_year))
    else:
        return(academic_importer_late(finish_year))

for i in files:
    files.update({i:joint_aca_importer(i)})

def column_extractor(data,code,name):
    file = data[code].copy()
    file.name = name
    file.index = data['CAMPUS'].values
    return(file)

def joint_extractor(data,codes,name):
    try:
        return(column_extractor(data,codes[0],name))
    except KeyError:
        return(column_extractor(data,codes[1],name))

def info(i, data):
    lag_year = i[0] + str(int(i[1])-1)
    if i == '00':
        lag_year = '99'
    if i == '10':
        lag_year = '09'
    storage = []
    storage = []
    storage.append(joint_extractor(data[i]['stud_info'],['CPETG09C','CPETG09C'],'gr9_stu_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETG10C','CPETG10C'],'gr10_stu_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETG11C','CPETG11C'],'gr11_stu_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETG12C','CPETG12C'],'gr12_stu_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETBLAC','CPETBLAC'],'black_stu_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETWHIC','CPETWHIC'],'white_stu_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETHISC','CPETHISC'],'his_stu_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETECOC','CPETECOC'],'all_stud_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETGIFC','CPETGIFC'],'gifted_stu_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETSPEC','CPETSPEC'],'spec_ed_stu_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETECOC','CPETECOC'],'econ_dis_stu_count'))
    storage.append(joint_extractor(data[i]['staff_info'],['CPSTTOSA','CPSTTOSA'],'teacher_avg_salary'))
    storage.append(joint_extractor(data[i]['staff_info'],['CPSTEXPA','CPSTEXPA'],'teacher_experience'))
    storage.append(joint_extractor(data[i]['staff_info'],['CPSTTENA','CPSTTENA'],'exp_w_dist'))
    if i in ['97','98','99']:
            print('not relevant')
    else:
        storage.append(joint_extractor(data[i]['attend'],['CANC4'+lag_year+'R','canc4'+lag_year+'r'],'completion_rate'))
        storage.append(joint_extractor(data[i]['attend'],['CAEC4'+lag_year+'R','caec4'+lag_year+'r'],'recieved_GED'))
        storage.append(joint_extractor(data[i]['attend'],['CAGC4'+lag_year+'R','cagc4'+lag_year+'r'],'graduated'))
    storage.append(joint_extractor(data[i]['ref'],['DISTNAME','CPFEOPRK'],'dist_name'))
    storage.append(joint_extractor(data[i]['ref'],['COUNTY','CPFEOPRK'],'county_num'))
    storage.append(joint_extractor(data[i]['ref'],['CFLCHART','CPFEOPRK'],'charter'))
    storage.append(joint_extractor(data[i]['ref'],['GRDSPAN','CPFEOPRK'],'grade_span'))

    #problem casesGRDTYPE
    try:
        storage.append(joint_extractor(data[i]['staff_info'],['CPCTENGA','CPETENGA'],'eng_class_size'))
        storage.append(joint_extractor(data[i]['staff_info'],['CPCTMATA','CPETMATA'],'math_class_size'))
        storage.append(joint_extractor(data[i]['staff_info'],['CPCTSCIA','CPETSCIA'],'sci_class_size'))
    except KeyError:
        print(i)
    file = pd.concat(storage,axis=1,join = 'outer', sort= True)
    data[i]['info'] = file

for i in files:
    info(i,files)

def finance(i, data):
    storage = []
    storage.append(joint_extractor(data[i]['fin'],['CPFEOPRK','CPFEAOPRK'],'per_pupil_exp'))
    storage.append(joint_extractor(data[i]['fin'],['CPFEINRK','CPFEAINSK'],'per_pupil_instruction'))
    storage.append(joint_extractor(data[i]['fin'],['CPFEADSK','CPFEAADIK'],'per_pupil_leadership'))
    file = pd.concat(storage,axis=1,join = 'outer', sort= True)
    data[i]['finance'] = file

for i in files:
    finance(i,files)

###\/###
def performance_early(i, data):
    lag_year = i[0] + str(int(i[1])-1)
    if i == '00':
        lag_year = '99'
    storage = []
    storage.append(joint_extractor(data[i]['attend'],['CA0CS'+lag_year+'R','CPFEAOPRK'],'sat'))
    storage.append(joint_extractor(data[i]['attend'],['CA0CA'+lag_year+'R','CPFEAINSK'],'act'))
    storage.append(joint_extractor(data[i]['attend'],['CA0CT'+lag_year+'R','CPFEAADIK'],'act_pct'))
    file = pd.concat(storage,axis=1,join = 'outer', sort= True)
    data[i]['performance'] = file

def performance_later(i, data):
    lag_year = i[0] + str(int(i[1])-1)
    if i == '10':
        lag_year = '09'
    storage = []
    try:
        storage.append(joint_extractor(data[i]['edu6'],['CA009PA'+i+'R','CA009TA'+i+'R'],'gr9_all_tests'))
    except KeyError:
        storage.append(joint_extractor(data[i]['edu6'],['CA009RA'+i+'R','CA009QA'+i+'R'],'gr9_all_tests'))
    try:
        storage.append(joint_extractor(data[i]['edu6'],['CA009PM'+i+'R','CA009TM'+i+'R'],'gr9_maths'))
    except KeyError:
        storage.append(joint_extractor(data[i]['edu6'],['CA009RM'+i+'R','CA009QM'+i+'R'],'gr9_maths'))
    try:
        storage.append(joint_extractor(data[i]['edu6'],['CA009PR'+i+'R','CA009TR'+i+'R'],'gr9_reading'))
    except KeyError:
        storage.append(joint_extractor(data[i]['edu6'],['CA009RR'+i+'R','CA009QR'+i+'R'],'gr9_reading'))
    storage.append(joint_extractor(data[i]['SAT'],['CA0CS'+lag_year+'R','CA009TR'+i+'R'],'sat'))
    storage.append(joint_extractor(data[i]['SAT'],['CA0CA'+lag_year+'R','CA009TR'+i+'R'],'act'))
    storage.append(joint_extractor(data[i]['SAT'],['CA0CT'+lag_year+'R','CA009TR'+i+'R'],'sat/act_pct'))
    file = pd.concat(storage,axis=1,join = 'outer', sort= True)
    data[i]['performance'] = file

def joint_performance(finish_year, data):
    try:
        performance_early(finish_year, data)
    except KeyError:
        performance_later(finish_year, data)

for i in files:
    joint_performance(i,files)
    print(i)

for i in files:
    for j in ['info']:
        files[i][j].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/campus_reg/'+j+i+'.csv')
