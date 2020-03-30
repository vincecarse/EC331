import pandas as pd

dists = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Texas_School_GIS/AdjacentDistrict.csv')
panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel.csv')

a = []
for i in dists.index:
    b = []
    for j in dists.iloc[i][1:]:
        try:
            b.append(int(j))
        except ValueError:
            1+1
    a.append(b)


dists['adj_dist'] = a
