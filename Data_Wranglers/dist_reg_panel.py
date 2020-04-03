import pandas as pd


panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/full_panel.csv', index_col = 0)
panel['adj_dist'] = panel['adj_dist'].str[2:-2].str.split("', '")

def cleaner(file,column):
    try:
        a = []
        for i in file.index:
            x = file[column][i][2:-2].replace("'",'').split("], [")
            c = [i.split(', ') for i in x]
            a.append(c)
        return(a)
    except AttributeError:
        return('n/a')

panel['adj_dist_total_rev'] = cleaner(panel,'adj_dist_total_rev')


panel['total_10_min_r']
panel['total_5_mile_r']

panel['Distance_alldist_min_10r']+panel['Distance_min_10r']


panel['Distance_min_10r'] = panel['Distance_min_10r'].replace(np.nan,0)
panel['Distance_miles_5r'] = panel['Distance_miles_5r'].replace(np.nan,0)

panel.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/full_panel.csv')

#
