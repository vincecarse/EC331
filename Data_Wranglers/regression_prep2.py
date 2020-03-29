import pandas as pd

index_panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel.csv')
panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel.csv')

new_cols = list(index_panel.columns[~index_panel.columns.isin(panel.columns)])
new_cols = [i for i in new_cols if (i != 'dist_name_x')&(i != 'dist_name_y')]
new_cols.append('Campus')
index_panel = index_panel[new_cols]
test_panel = pd.merge(panel,index_panel,on = 'Campus')
test_panel = test_panel.drop(['Unnamed: 0'], axis = 1)

test_panel.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/big_panel.csv')




#deleted
#index_panel = index_panel.drop(['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.1.1','Unnamed: 0.1.1.1','Unnamed: 0.1.1.1.1','Unnamed: 0.1.1.1.1.1','Unnamed: 0.1.1.1.1.1.1'], axis = 1)
