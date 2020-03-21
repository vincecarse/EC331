import pandas as pd

fin = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/ISD_Financial_Reports/2000-2018_Summarized_Financial_Data.csv')
files = {}

def format(file, store):
    file['DISTRICT NUMBER'] = file['DISTRICT NUMBER'].str[1:]
    for i in fin['YEAR'].unique():
        file = fin[fin['YEAR'] == i]
        file = file.drop('YEAR', axis = 1)
        file.index = file['DISTRICT NUMBER'].values
        store.update({i:file})
    return(file, store)

fin, files = format(fin, files)

for i in files:
    if i == 2000:
        year_span = '99-00'
    elif i<2010:
        year_span = str(0)+str(i-2001)+'-'+str(0)+str(i-2000)
    elif i == 2011:
        year_span = '09-10'
    else:
        year_span = str(i-2001)+'-'+str(i-2000)
    files[i].to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/formatted_dist_finance/'+year_span+'.csv')





#
