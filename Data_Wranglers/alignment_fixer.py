import pandas as pd

panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel2.csv')
a = list(panel['Distance_adj_min'][:259].values)
a.append([''])
a.append([''])
a.extend(list(panel['Distance_adj_min'][259:].values))

b = list(panel['Distance_adj_miles'][:259].values)
b.append([''])
b.append([''])
b.extend(list(panel['Distance_adj_miles'][259:].values))

panel['Distance_adj_min'] = a[:-2]
panel['Distance_adj_miles'] = b[:-2]
panel = panel.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1', 'Unnamed: 0.1.1.1',
'Unnamed: 0.1.1.1.1', 'Unnamed: 0.1.1.1.1.1', 'Unnamed: 0.1.1.1.1.1.1',
'Unnamed: 0.1.1.1.1.1.1.1', 'Unnamed: 0.1.1.1.1.1.1.1.1',
'Unnamed: 0.1.1.1.1.1.1.1.1.1', 'Unnamed: 0.1.1.1.1.1.1.1.1.1.1'],axis=1)
panel = panel.rename(columns = {'dist_name_x':'dist_name'})
panel.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel2.csv')
