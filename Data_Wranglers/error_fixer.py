import pandas as pd

panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel2.csv')

try:
    panel['adj_dist'] = panel['adj_dist'].str[2:-2].str.split("', '")
    a = []
    b = []
    for i in panel.index:
        x = panel['Distance_adj_min'][i][2:-2].replace("'",'').split("], [")
        y = panel['adj_dist_schools'][i][2:-2].replace("'",'').split("], [")
        c = [i.split(', ') for i in x]
        d = [i.split(', ') for i in y]
        a.append(c)
        b.append(d)
    panel['Distance_adj_min'] = a
    panel['adj_dist_schools'] = b
except AttributeError:
    print('n/a')

for i in panel.index:
    try:
        for j in range(len(panel['Distance_adj_min'][i])):
            if panel['Distance_adj_min'][i][j] == ['error']:
                print((i,j,panel['adj_dist_schools'][i][j] == ['']))
    except IndexError:
        print('error')


panel['Distance_adj_min'][950][1] == ['error']:
