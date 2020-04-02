import pandas as pd


panel = pd.read_csv('/Users/vincentcarse/Github/EC331/Regression_data/VAM_reg/new_balanced_panel2.csv')
panel = panel.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1', 'Unnamed: 0.1.1.1',
'Unnamed: 0.1.1.1.1', 'Unnamed: 0.1.1.1.1.1', 'Unnamed: 0.1.1.1.1.1.1',
'Unnamed: 0.1.1.1.1.1.1.1', 'Unnamed: 0.1.1.1.1.1.1.1.1',
'Unnamed: 0.1.1.1.1.1.1.1.1.1', 'Unnamed: 0.1.1.1.1.1.1.1.1.1.1'],axis=1)
small_pan = panel[panel['Distance_adj_miles'].isna()==False]
small_pan[['Distance_adj_min','Distance_adj_miles']]

try:
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







#first find all the schools in a 10 minute/5 mile radius
#then think about linking district info to distances




###   Other
#(stata) create variable for whether tax rate is at the maximum
