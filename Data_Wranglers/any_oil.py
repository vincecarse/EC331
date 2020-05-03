import pandas as pd

data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel.csv')
oil_dists = data[data['dist_oil_val']>0]['Campus'].unique()
oil = data[data['Campus'].isin(oil_dists)]
oil.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/oil_camps.csv')


data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel_real2.csv')
oil_dists = data[data['dist_oil_val']>0]['Campus'].unique()
oil = data[data['Campus'].isin(oil_dists)]
oil.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/oil_real_camps.csv')
