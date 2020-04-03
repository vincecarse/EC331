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
    file.update({'fin':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+finish_year+'/dfin.csv', dtype = str)})
    file.update({'ref':pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/District_Academic_Performance/'+finish_year+'/dref.csv', dtype = str)})
    return(file)

for i in files:
    files.update({i:academic_importer_late(i)})

def column_extractor(data,code,name):
    file = data[code].copy()
    file.name = name
    file.index = data['DISTRICT'].values
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

def finance(i, data):
    storage = []
    storage.append(joint_extractor(data[i]['fin'],['DISTRICT','DISTRICT'],'DISTRICT'))
    storage.append(joint_extractor(data[i]['ref'],['DISTNAME','CPFEOPRK'],'dist_name'))
    storage.append(joint_extractor(data[i]['fin'],['DPFTADPR','DPFTADPR'],'dist_total_tax_rate'))
    storage.append(joint_extractor(data[i]['fin'],['DPFTAMOR','DPFTAMOR'],'dist_tax_M&O_rate'))
    storage.append(joint_extractor(data[i]['fin'],['DPFRALLT','DPFRAALLT'],'dist_total_rev'))
    storage.append(joint_extractor(data[i]['fin'],['DPFRLOCT','DPFRALOCT'],'dist_local_rev'))
    storage.append(joint_extractor(data[i]['fin'],['DPFRSTAT','DPFRASTAT'],'dist_state_rev'))
    storage.append(joint_extractor(data[i]['fin'],['DPFVTOTK','DPFVTOTK'],'dist_total_val_per_pupil'))
    storage.append(joint_extractor(data[i]['fin'],['DPFVTOTT','DPFVTOTT'],'dist_total_val'))
    storage.append(joint_extractor(data[i]['fin'],['DPFVOILT','DPFVOILT'],'dist_oil_val'))
    storage.append(joint_extractor(data[i]['fin'],['DPFXWLHT','DPFXAWLHT'],'dist_wealth_transfers'))
    file = pd.concat(storage,axis=1,join = 'outer', sort= True)
    file['Year'] = '20'+ i
    data[i]['finance'] = file

for i in files:
    finance(i,files)

fin_file = pd.merge(files['03']['finance'],files['04']['finance'],how = 'outer')
for i in files:
    fin_file = pd.merge(fin_file,files[i]['finance'],how = 'outer')

fin_file.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/fin_file2.csv')
