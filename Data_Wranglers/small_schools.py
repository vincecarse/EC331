import pandas as pd

x = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/05/cstud.csv')
y = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/05/cref.csv')
z = pd.merge(x,y, on ='CAMPUS')


z[z['CPETALLC'].replace('.',1000).astype(int)<100][['CAMPUS','GRDSPAN']]

(z[z['CPETALLC'].replace('.',1000).astype(int)<100]['GRDSPAN'] == '06 - 08').sum()


a = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/05/ctaks5.csv')
b = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Academic_Performance/05/ctaks1.csv')

a['CA007RM05R']
b['CA003RM05R'].replace('.',np.nan).replace('-1',np.nan).dropna().astype(int).mean()


a['CA007RM05R'].replace('.',np.nan).replace('-1',np.nan).dropna().astype(int).max()

CA003RM
CA003TM
CA003PM

#
