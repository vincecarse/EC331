import pandas as pd
import numpy as np

files = {}

def year_creator(data):

    for i in range(4,11):
        data.update({str(0)+str(i-1):''})
    data.update({'10':''})
    data.update({'11':''})

year_creator(files)


def academic_importer_late(finish_year):
    file = {}
    if finish_year in ['04','05','06','07','08','09','10','11']:
        for i in range(1,14):
            file.update({'edu'+str(i):pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/ctaks'+str(i)+'.csv', dtype = str)})
    if finish_year in ['03']:
        for i in range(1,17):
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
    file.update({'dfin':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+finish_year+'/dfin.csv', dtype = str)})
    file.update({'other':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/'+finish_year+'/cothr.csv', dtype = str)})
    return(file)

for i in files:
    files.update({i:academic_importer_late(i)})

def column_extractor(data,code,name):
    file = data[code].copy()
    file.name = name
    file.index = data['CAMPUS'].values
    return(file)

def columns_extractor(data,codes,names):
    file = data[codes].copy()
    file.columns = names
    file.index = data['DISTRICT'].values
    return(file)

def joint_extractor(data,codes,name):
    try:
        return(column_extractor(data,codes[0],name))
    except KeyError:
        return(column_extractor(data,codes[1],name))

def info(i, data):
    lag_year = i[0] + str(int(i[1])-1)
    if i == '10':
        lag_year = '09'
    storage = []
    storage.append(joint_extractor(data[i]['stud_info'],['CAMPUS','CAMPUS'],'Campus'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETG03C','CPETG09C'],'gr3_stu_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETG04C','CPETG10C'],'gr4_stu_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETG05C','CPETG11C'],'gr5_stu_count'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETBLAP','CPETBLAP'],'black_stu_percent'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETWHIP','CPETWHIP'],'white_stu_percent'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETHISP','CPETHISP'],'his_stu_percent'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETECOP','CPETECOP'],'all_stud_percent'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETGIFP','CPETGIFP'],'gifted_stu_percent'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETSPEP','CPETSPEP'],'spec_ed_stu_percent'))
    storage.append(joint_extractor(data[i]['stud_info'],['CPETECOP','CPETECOP'],'econ_dis_stu_percent'))
    storage.append(joint_extractor(data[i]['staff_info'],['CPSTTOSA','CPSTTOSA'],'teacher_avg_salary'))
    storage.append(joint_extractor(data[i]['staff_info'],['CPSTEXPA','CPSTEXPA'],'teacher_experience'))
    storage.append(joint_extractor(data[i]['staff_info'],['CPSTTENA','CPSTTENA'],'exp_w_dist'))
    storage.append(joint_extractor(data[i]['staff_info'],['CPSTTOFC','CPSTTOFC'],'teacher_count'))
    storage.append(joint_extractor(data[i]['attend'],['CANC4'+lag_year+'R','canc4'+lag_year+'r'],'completion_rate'))
    storage.append(joint_extractor(data[i]['attend'],['CAEC4'+lag_year+'R','caec4'+lag_year+'r'],'recieved_GED'))
    storage.append(joint_extractor(data[i]['attend'],['CAGC4'+lag_year+'R','cagc4'+lag_year+'r'],'graduated'))
    storage.append(joint_extractor(data[i]['ref'],['DISTNAME','CPFEOPRK'],'dist_name'))
    storage.append(joint_extractor(data[i]['ref'],['COUNTY','CPFEOPRK'],'county_num'))
    storage.append(joint_extractor(data[i]['ref'],['CFLCHART','CPFEOPRK'],'charter'))
    storage.append(joint_extractor(data[i]['ref'],['GRDSPAN','CPFEOPRK'],'grade_span'))
    #problem casesGRDTYPE
    try:
        storage.append(joint_extractor(data[i]['staff_info'],['CPCTG03A','CPETG03A'],'gr3_class_size'))
        storage.append(joint_extractor(data[i]['staff_info'],['CPCTG04A','CPETG04A'],'gr4_class_size'))
        storage.append(joint_extractor(data[i]['staff_info'],['CPCTG05A','CPETG05A'],'gr5_class_size'))
    except KeyError:
        print(i)
    file = pd.concat(storage,axis=1,join = 'outer', sort= True)
    file['Year'] = '20'+ i
    file['DISTRICT'] = file['Campus'].str[:-3]
    data[i]['info'] = file

for i in files:
    info(i,files)
    files[i]['fin']['DISTRICT'] = files[i]['fin']['CAMPUS'].str[:-3]

info_file = pd.merge(files['03']['info'],files['04']['info'],how = 'outer')
for i in files:
    info_file = pd.merge(info_file,files[i]['info'],how = 'outer')
    files[i]['fin'] = pd.merge(files[i]['fin'],files[i]['dfin'], on ='DISTRICT')


def finance(i, data):
    storage = []
    storage.append(joint_extractor(data[i]['stud_info'],['CAMPUS','CAMPUS'],'Campus'))
    storage.append(joint_extractor(data[i]['fin'],['CPFEOPRK','CPFEAOPRK'],'per_pupil_exp'))
    storage.append(joint_extractor(data[i]['fin'],['CPFEINRK','CPFEAINSK'],'per_pupil_instruction'))
    storage.append(joint_extractor(data[i]['fin'],['CPFEADSK','CPFEAADIK'],'per_pupil_leadership'))
    try:
        storage.append(joint_extractor(data[i]['fin'],['CPFEOTHK','CPFEAOTHK'],'per_pupil_othr'))
    except KeyError:
        storage.append(joint_extractor(data[i]['fin'],['CPFEOTHK','CPFPAOTHK'],'per_pupil_othr'))
    storage.append(joint_extractor(data[i]['fin'],['DPFTADPR','DPFTADPR'],'dist_total_tax_rate'))
    storage.append(joint_extractor(data[i]['fin'],['DPFTAMOR','DPFTAMOR'],'dist_tax_M&O_rate'))
    storage.append(joint_extractor(data[i]['fin'],['DPFRALLT','DPFRAALLT'],'dist_total_rev'))
    storage.append(joint_extractor(data[i]['fin'],['DPFRLOCT','DPFRALOCT'],'dist_local_rev'))
    storage.append(joint_extractor(data[i]['fin'],['DPFRSTAT','DPFRASTAT'],'dist_state_rev'))
    storage.append(joint_extractor(data[i]['fin'],['DPFVTOTK','DPFVTOTK'],'dist_total_val_per_pupil'))
    storage.append(joint_extractor(data[i]['fin'],['DPFVOILT','DPFVOILT'],'dist_oil_val'))
    storage.append(joint_extractor(data[i]['fin'],['DPFXWLHT','DPFXAWLHT'],'dist_wealth_transfers'))

    #storage.append(joint_extractor(data[i]['dfin'],['CPFEADSK','CPFEAADIK'],'per_pupil_leadership'))
    file = pd.concat(storage,axis=1,join = 'outer', sort= True)
    file['Year'] = '20'+ i
    file['DISTRICT'] = file['Campus'].str[:-3]
    data[i]['finance'] = file

for i in files:
    finance(i,files)
    print(i)

fin_file = pd.merge(files['03']['finance'],files['04']['finance'],how = 'outer')
for i in files:
    fin_file = pd.merge(fin_file,files[i]['finance'],how = 'outer')

def academic(i,data):
    lag_year = i[0] + str(int(i[1])-1)
    if i == '10':
        lag_year = '09'
    storage = []
    storage.append(joint_extractor(data[i]['stud_info'],['CAMPUS','CAMPUS'],'Campus'))
    try:
        storage.append(joint_extractor(data[i]['edu1'],['CA003QM'+i+'R','CA003RM'+i+'R'],'TAKS_math_gr3'))
    except KeyError:
        storage.append(joint_extractor(data[i]['edu1'],['CA003TM'+i+'R','CA003PM'+i+'R'],'TAKS_math_gr3'))
    try:
        storage.append(joint_extractor(data[i]['edu1'],['CA003QR'+i+'R','CA003RR'+i+'R'],'TAKS_reading_gr3'))
    except KeyError:
        storage.append(joint_extractor(data[i]['edu1'],['CA003TR'+i+'R','CA003PR'+i+'R'],'TAKS_reading_gr3'))
    try:
        storage.append(joint_extractor(data[i]['edu2'],['CA004QM'+i+'R','CA004RM'+i+'R'],'TAKS_math_gr4'))
    except KeyError:
        storage.append(joint_extractor(data[i]['edu2'],['CA004TM'+i+'R','CA004PM'+i+'R'],'TAKS_math_gr4'))
    try:
        storage.append(joint_extractor(data[i]['edu2'],['CA004QR'+i+'R','CA004RR'+i+'R'],'TAKS_reading_gr4'))
    except KeyError:
        storage.append(joint_extractor(data[i]['edu2'],['CA004TR'+i+'R','CA004PR'+i+'R'],'TAKS_reading_gr4'))
    try:
        storage.append(joint_extractor(data[i]['edu3'],['CA005QM'+i+'R','CA005RM'+i+'R'],'TAKS_math_gr5'))
    except KeyError:
        storage.append(joint_extractor(data[i]['edu3'],['CA005TM'+i+'R','CA005PM'+i+'R'],'TAKS_math_gr5'))
    try:
        storage.append(joint_extractor(data[i]['edu3'],['CA005QR'+i+'R','CA005RR'+i+'R'],'TAKS_reading_gr5'))
    except KeyError:
        storage.append(joint_extractor(data[i]['edu3'],['CA005TR'+i+'R','CA005PR'+i+'R'],'TAKS_reading_gr5'))
    try:
        storage.append(joint_extractor(data[i]['edu11'],['CATTA'+i+'R','CAIYA'+i+'R'],'TAKS_part'))
    except KeyError:
        try:
            storage.append(joint_extractor(data[i]['edu13'],['CATYA'+i+'R','CPFEOPRK'],'TAKS_part'))
        except KeyError:
            storage.append(joint_extractor(data[i]['edu16'],['CATYA'+i+'R','CPFEOPRK'],'TAKS_part'))
    file = pd.concat(storage,axis=1,join = 'outer')
    file['Year'] = '20'+ i
    data[i]['acam'] = file

for i in files:
    academic(i,files)
    print(i)

aca_file = pd.merge(files['03']['acam'],files['04']['acam'],how = 'outer', sort = True)
for i in files:
    aca_file = pd.merge(aca_file,files[i]['acam'],how = 'outer', sort = True)





aca_file = aca_file.replace('-1',np.nan)
aca_file = aca_file.replace('-4',np.nan)
aca_file = aca_file.replace('.',np.nan)
aca_file = aca_file.dropna()

panel = pd.merge(aca_file, fin_file)
panel = pd.merge(panel, info_file)
panel = panel.replace('-1',np.nan)
panel = panel.replace('-4',np.nan)
panel = panel.replace('-2',np.nan)
panel = panel.replace('.',np.nan)
panel = panel.drop(['completion_rate','recieved_GED', 'graduated'],axis=1)
panel = panel.dropna()



panel[panel['Year']=='2005'][['gr3_stu_count','gr4_stu_count','gr5_stu_count']].astype(int).sum()




panel.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/panel1.csv')
