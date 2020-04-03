import pandas as pd



big_panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/campus_panel.csv')

dist_data = dist_panel[['Campus','Location', 'schools', 'Distance_min',
'Distance_miles', 'Distance_min_clean', 'Distance_miles_clean',
'Distance_min_minimum', 'Distance_min_10r', 'Distance_min_avg',
'Distance_miles_minimum', 'Distance_miles_5r', 'Distance_miles_avg',
'adj_dist', 'adj_dist_schools', 'Distance_adj_min',
'Distance_adj_miles', 'Distance_adj_min_clean',
'Distance_adj_miles_clean', 'Distance_alldist_min_10r',
'Distance_indist_min_10r', 'Distance_alldist_miles_5r',
'Distance_indist_miles_5r']]


merged_files = pd.merge(big_panel,dist_data,on='Campus')

merged_files.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/left_panel.csv')
