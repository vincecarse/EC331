import pandas as pd


panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel2.csv')
#panel = panel.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1', 'Unnamed: 0.1.1.1',
#'Unnamed: 0.1.1.1.1', 'Unnamed: 0.1.1.1.1.1', 'Unnamed: 0.1.1.1.1.1.1',
#'Unnamed: 0.1.1.1.1.1.1.1', 'Unnamed: 0.1.1.1.1.1.1.1.1',
#'Unnamed: 0.1.1.1.1.1.1.1.1.1', 'Unnamed: 0.1.1.1.1.1.1.1.1.1.1'],axis=1)
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

a = []
b = []

for row in small_pan.index:
    e = []
    f = []
    for dist in small_pan['Distance_adj_min'][row]:
        e.append([float(i) for i in dist if (i!='error')&(i!='')])
    a.append(e)
    for dist in small_pan['Distance_adj_miles'][row]:
        f.append([float(i) for i in dist if (i!='error')&(i!='')])
    b.append(f)

small_pan['Distance_adj_min_clean'] = a
small_pan['Distance_adj_miles_clean'] = b

a1 = []
b1 = []
a2 = []
b2 = []
for row in small_pan.index:
    c1 = []
    d1 = []
    c2 = []
    d2 = []
    for dist in small_pan['Distance_adj_min_clean'][row]:
        for i in dist:
            c1.append(i)
        c2.append(len([i for i in dist if i<10]))
    a1.append(len([i for i in c1 if i<10]))
    a2.append(c2)
    for dist in small_pan['Distance_adj_miles_clean'][row]:
        for i in dist:
            d1.append(i)
        d2.append(len([i for i in dist if i<5]))
    b1.append(len([i for i in d1 if i<5]))
    b2.append(d2)


small_pan['Distance_alldist_min_10r'] = a1
small_pan['Distance_indist_min_10r'] = a2
small_pan['Distance_alldist_miles_5r'] = b1
small_pan['Distance_indist_miles_5r'] = b2

small_pan.to_csv('/Users/vincentcarse/Github/EC331/Regression_data/VAM_reg/new_balanced_panel5.csv')




###   Other
#(stata) create variable for whether tax rate is at the maximum
