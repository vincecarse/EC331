import pandas as pd

panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel2.csv')
small_pan = panel[panel['Distance_adj_miles'].isna()==False]

small_pan['adj_dist']
small_pan['adj_dist_schools']
small_pan['Distance_adj_min']

try:
    small_pan['adj_dist'] = small_pan['adj_dist'].str[2:-2].str.split("', '")
    a = []
    b = []
    c = []
    for i in small_pan.index:
        x = small_pan['Distance_adj_min'][i][2:-2].replace("'",'').split("], [")
        y = small_pan['Distance_adj_miles'][i][2:-2].replace("'",'').split("], [")
        z = small_pan['adj_dist_schools'][i][2:-2].replace("'",'').split("], [")
        d = [i.split(', ') for i in x]
        e = [i.split(', ') for i in y]
        f = [i.split(', ') for i in z]
        a.append(d)
        b.append(e)
        c.append(f)
    small_pan['Distance_adj_min'] = a
    small_pan['Distance_adj_miles'] = b
    small_pan['adj_dist_schools'] = c
except AttributeError:
    print('n/a')


a = []
for i in small_pan.index:
    a.append(len(small_pan['Distance_adj_min'][i])==len(small_pan['adj_dist_schools'][i]))

small_pan['equal_lengths'] = a

a = list(small_pan['Distance_adj_min'][:259].values)
a.append([''])
a.append([''])
a.extend(list(small_pan['Distance_adj_min'][259:].values))

b = list(small_pan['Distance_adj_miles'][:259].values)
b.append([''])
b.append([''])
b.extend(list(small_pan['Distance_adj_miles'][259:].values))

small_pan['Distance_adj_min_test'] = a[:-2]
small_pan['Distance_adj_miles_test'] = b[:-2]
