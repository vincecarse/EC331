import pandas as pd


panel = pd.read_csv('/Users/vincentcarse/Github/EC331/Regression_data/VAM_reg/new_balanced_panel2.csv')
panel = panel.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1', 'Unnamed: 0.1.1.1',
'Unnamed: 0.1.1.1.1', 'Unnamed: 0.1.1.1.1.1', 'Unnamed: 0.1.1.1.1.1.1',
'Unnamed: 0.1.1.1.1.1.1.1', 'Unnamed: 0.1.1.1.1.1.1.1.1',
'Unnamed: 0.1.1.1.1.1.1.1.1.1', 'Unnamed: 0.1.1.1.1.1.1.1.1.1.1'],axis=1)
small_pan = panel[panel['Distance_adj_miles'].isna()==False]
small_pan[['Distance_adj_min','Distance_adj_miles']]

try:
    small_pan['adj_dist'] = small_pan['adj_dist'].str[2:-2].str.split("', '")
    a = []
    b = []
    for i in small_pan.index:
        x = small_pan['Distance_adj_min'][i][2:-2].replace("'",'').split("], [")
        y = small_pan['Distance_adj_miles'][i][2:-2].replace("'",'').split("], [")
        c = [i.split(', ') for i in x]
        d = [i.split(', ') for i in y]
        a.append(c)
        b.append(d)
    small_pan['Distance_adj_min'] = a
    small_pan['Distance_adj_miles'] = b
except AttributeError:
    print('n/a')

a = small_pan['Distance_adj_min'].values
b = small_pan['Distance_adj_miles'].values
c = []
d = []

for row in a:
    e = []
    for dist in row:
        e.append([float(i) for i in dist if (i!='error')&(i!='')])
    c.append(e)

for row in b:
    f = []
    for dist in row:
        f.append([float(i) for i in dist if (i!='error')&(i!='')])
    d.append(f)

small_pan['Distance_adj_min_clean'] = c
small_pan['Distance_adj_miles_clean'] = d




a = panel['Distance_min_clean'].values
b = panel['Distance_miles_clean'].values
c = []
d = []
e = []
f = []
g = []
h = []

for i in a:
    try:
        c.append(min(i))
        d.append(len([j for j in i if j<10]))
        e.append(mean(i))
    except ValueError:
        c.append(np.nan)
        d.append(np.nan)
        e.append(np.nan)

for i in b:
    try:
        f.append(min(i))
        g.append(len([j for j in i if j<5]))
        h.append(mean(i))
    except ValueError:
        f.append(np.nan)
        g.append(np.nan)
        h.append(np.nan)


panel['Distance_min_minimum'] = c
panel['Distance_min_10r'] = d
panel['Distance_min_avg'] = e
panel['Distance_miles_minimum'] = f
panel['Distance_miles_5r'] = g
panel['Distance_miles_avg'] = h



























#first find all the schools in a 10 minute/5 mile radius
#then think about linking district info to distances




###   Other
#(stata) create variable for whether tax rate is at the maximum
