import pandas as pd

type08 = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus&District_Type/district0708.csv',header = 2)
type09 = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus&District_Type/district0809.csv',header = 2)
type10 = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus&District_Type/district0910.csv',header = 2)
type11 = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus&District_Type/district1011.csv',header = 2)

merge_a = pd.merge(type08,type09,on = 'District')
merge_b = pd.merge(type10,type11,on = 'District')
merge_c = pd.merge(merge_a,merge_b,on = 'District')
merge_c = merge_c[['District','Type_x_x','Type_x_y','Type_y_x','Type_y_y']]
merge_c = merge_c.dropna()
merge_c['Equal'] = (merge_c['Type_x_x'] == merge_c['Type_x_y'])&(merge_c['Type_x_y'] == merge_c['Type_y_x'])&(merge_c['Type_y_x'] == merge_c['Type_y_y'])
