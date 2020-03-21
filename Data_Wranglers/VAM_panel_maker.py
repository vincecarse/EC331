import pandas as pd
import numpy as np


aca_file = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/aca_file.csv')
fin_file = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/fin_file.csv')
info_file = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/info_file.csv')
panel = pd.merge(aca_file, fin_file, how = 'outer',on = ['Campus','Year'])
panel = pd.merge(panel, info_file, how = 'outer',on = ['Campus','Year'])
panel = panel.drop(['Unnamed: 0_x','Unnamed: 0_y','Unnamed: 0','DISTRICT_y'], axis=1)
panel = panel.rename(columns = {'DISTRICT_x':'District'})
dist_type = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus&District_Type/district0708.csv',header = 2)
dist_type = dist_type[['District','Description']]
panel = pd.merge(panel,dist_type, on = 'District')

panel = panel.sort_values(['Campus','Year'])
panel = panel.replace('-1',np.nan)
panel.charter = panel.charter.replace('N',0)
panel.charter = panel.charter.replace('Y',1)
panel = panel.replace('-4',np.nan)
panel = panel.replace('.',np.nan)

panel.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/panel.csv')

#dropping missing value schools

bal = []
for i in panel['Campus'].unique():
    if (panel[panel['Campus'] == i].isna().sum().sum() == 0)&(len(panel[panel['Campus'] == i]) == 9):
        bal.append(i)

balanced_panel = panel[panel['Campus'].isin(bal)]
balanced_panel.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel.csv')







##deprecated




elem = elem.replace('-1',np.nan)
elem = elem.replace('-4',np.nan)
elem = elem.replace('.',np.nan)
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
