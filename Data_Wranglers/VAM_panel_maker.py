import pandas as pd
import numpy as np


aca_file = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/aca_file.csv')
fin_file = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/fin_file.csv')
info_file = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/info_file.csv')
panel = pd.merge(aca_file, fin_file, how = 'outer',on = ['Campus','Year'])
panel = pd.merge(panel, info_file, how = 'outer',on = ['Campus','Year'])
panel = panel.drop(['Unnamed: 0_x','Unnamed: 0_y','Unnamed: 0','DISTRICT_y'], axis=1)
panel = panel.rename(columns = {'DISTRICT_x':'District'})
elem = panel[panel['grade_span'].isin(['EE - 05','PK - 05','KG - 05'])]
dist_type = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus&District_Type/district0708.csv',header = 2)
dist_type = dist_type[['District','Description']]
elem = pd.merge(elem,dist_type, on = 'District')

elem.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/elem.csv')



elem = panel[panel['grade_span'].isin(['EE - 05','PK - 05','KG - 05'])]
elem = panel[panel['grade_span'].isin(['EE - 05','PK - 05','KG - 05'])]


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
