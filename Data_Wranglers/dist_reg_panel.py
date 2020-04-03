import pandas as pd

panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/full_panel.csv', index_col = 0)
panel.rename(columns = {'dist_name_x':'dist_name'})

panel['Total_miles_5r'] = panel['Distance_alldist_miles_5r'] + panel['Distance_miles_5r']
panel['Total_min_10r'] = panel['Distance_alldist_min_10r'] + panel['Distance_min_10r']

panel = panel.drop(['Location',
'schools',
'Distance_min',
'Distance_miles',
'Distance_min_clean',
'Distance_miles_clean',
'Distance_min_minimum',
'Distance_min_10r',
'Distance_min_avg',
'Distance_miles_minimum',
'Distance_miles_5r',
'Distance_miles_avg',
'adj_dist',
'adj_dist_schools',
'Distance_adj_min',
'Distance_adj_miles',
'Distance_adj_min_clean',
'Distance_adj_miles_clean',
'dist_name_y','grade_span'],axis=1)

def cleaner(file,column, special = 1):
    try:
        a = []
        for i in file.index:
            x = file[column][i][special:-special].replace("'",'').split(", ")
            a.append(x)
        return(a)
    except AttributeError:
        return('n/a')

panel['adj_dist_total_rev'] = cleaner(panel,'adj_dist_total_rev',2)
panel['Distance_indist_miles_5r'] = cleaner(panel,'Distance_indist_miles_5r')
panel['Distance_indist_min_10r'] = cleaner(panel,'Distance_indist_min_10r')
panel['adj_dist_local_rev'] = cleaner(panel,'adj_dist_local_rev')
panel['adj_dist_state_rev'] = cleaner(panel,'adj_dist_state_rev')
panel['adj_dist_total_val_per_pupil'] = cleaner(panel,'adj_dist_total_val_per_pupil')
panel['adj_dist_total_val'] = cleaner(panel,'adj_dist_total_val')
panel['adj_dist_oil_val'] = cleaner(panel,'adj_dist_oil_val')
panel['adj_dist_wealth_transfers'] = cleaner(panel,'adj_dist_wealth_transfers')
panel['adj_dist_tax_M&O_rate'] = cleaner(panel,'adj_dist_tax_M&O_rate')
panel['adj_dist_total_tax_rate'] = cleaner(panel,'adj_dist_total_tax_rate')

def fun_ction(data,variable):
    a1 = []
    for i in data.index:
        b = []
        for j in range(len(data['Distance_indist_min_10r'][i])):
            if data['Distance_indist_min_10r'][i][j] != '0':
                if data[variable][i][j] != '':
                    b.append(float(data[variable][i][j]))
                else:
                    b.append(0)
        a1.append(b)
    return(a1)

panel['Distance_indist_min_10r'] = fun_ction(panel,'Distance_indist_min_10r')
panel['Distance_indist_miles_5r'] = fun_ction(panel,'Distance_indist_miles_5r')
panel['adj_dist_total_rev'] = fun_ction(panel,'adj_dist_total_rev')
panel['Distance_indist_miles_5r'] = fun_ction(panel,'Distance_indist_miles_5r')
panel['Distance_indist_min_10r'] = fun_ction(panel,'Distance_indist_min_10r')
panel['adj_dist_local_rev'] = fun_ction(panel,'adj_dist_local_rev')
panel['adj_dist_state_rev'] = fun_ction(panel,'adj_dist_state_rev')
panel['adj_dist_total_val_per_pupil'] = fun_ction(panel,'adj_dist_total_val_per_pupil')
panel['adj_dist_total_val'] = fun_ction(panel,'adj_dist_total_val')
panel['adj_dist_oil_val'] = fun_ction(panel,'adj_dist_oil_val')
panel['adj_dist_wealth_transfers'] = fun_ction(panel,'adj_dist_wealth_transfers')
panel['adj_dist_tax_M&O_rate'] = fun_ction(panel,'adj_dist_tax_M&O_rate')
panel['adj_dist_total_tax_rate'] = fun_ction(panel,'adj_dist_total_tax_rate')

def fun_ction1(data,variable,j):
    a = []
    for i in data.index:
        try:
            a.append(data[variable][i][j])
        except IndexError:
            a.append('')
    return(a)

panel['Distance_indist_min_10r_0'] = fun_ction1(panel,'Distance_indist_min_10r',0)
panel['Distance_indist_min_10r_0'] = fun_ction1(panel,'Distance_indist_min_10r',1)
panel['Distance_indist_min_10r_2'] = fun_ction1(panel,'Distance_indist_min_10r',2)

panel['Distance_indist_miles_5r_0'] = fun_ction1(panel,'Distance_indist_miles_5r',0)
panel['Distance_indist_miles_5r_1'] = fun_ction1(panel,'Distance_indist_miles_5r',1)
panel['Distance_indist_miles_5r_2'] = fun_ction1(panel,'Distance_indist_miles_5r',2)

panel['adj_dist_total_rev_0'] = fun_ction1(panel,'adj_dist_total_rev',0)
panel['adj_dist_total_rev_1'] = fun_ction1(panel,'adj_dist_total_rev',1)
panel['adj_dist_total_rev_2'] = fun_ction1(panel,'adj_dist_total_rev',2)

panel['Distance_indist_miles_5r_0'] = fun_ction1(panel,'Distance_indist_miles_5r',0)
panel['Distance_indist_miles_5r_1'] = fun_ction1(panel,'Distance_indist_miles_5r',1)
panel['Distance_indist_miles_5r_2'] = fun_ction1(panel,'Distance_indist_miles_5r',2)

panel['adj_dist_local_rev_0'] = fun_ction1(panel,'adj_dist_local_rev',0)
panel['adj_dist_local_rev_1'] = fun_ction1(panel,'adj_dist_local_rev',1)
panel['adj_dist_local_rev_2'] = fun_ction1(panel,'adj_dist_local_rev',2)

panel['adj_dist_state_rev_0'] = fun_ction1(panel,'adj_dist_state_rev',0)
panel['adj_dist_state_rev_1'] = fun_ction1(panel,'adj_dist_state_rev',1)
panel['adj_dist_state_rev_2'] = fun_ction1(panel,'adj_dist_state_rev',2)

panel['adj_dist_total_val_per_pupil_0'] = fun_ction1(panel,'adj_dist_total_val_per_pupil',0)
panel['adj_dist_total_val_per_pupil_1'] = fun_ction1(panel,'adj_dist_total_val_per_pupil',1)
panel['adj_dist_total_val_per_pupil_2'] = fun_ction1(panel,'adj_dist_total_val_per_pupil',2)

panel['adj_dist_total_val_0'] = fun_ction1(panel,'adj_dist_total_val',0)
panel['adj_dist_total_val_1'] = fun_ction1(panel,'adj_dist_total_val',1)
panel['adj_dist_total_val_2'] = fun_ction1(panel,'adj_dist_total_val',2)

panel['adj_dist_oil_val_0'] = fun_ction1(panel,'adj_dist_oil_val',0)
panel['adj_dist_oil_val_1'] = fun_ction1(panel,'adj_dist_oil_val',1)
panel['adj_dist_oil_val_2'] = fun_ction1(panel,'adj_dist_oil_val',2)

panel['adj_dist_wealth_transfers_0'] = fun_ction1(panel,'adj_dist_wealth_transfers',0)
panel['adj_dist_wealth_transfers_1'] = fun_ction1(panel,'adj_dist_wealth_transfers',1)
panel['adj_dist_wealth_transfers_2'] = fun_ction1(panel,'adj_dist_wealth_transfers',2)

panel['adj_dist_tax_M&O_rate_0'] = fun_ction1(panel,'adj_dist_tax_M&O_rate',0)
panel['adj_dist_tax_M&O_rate_1'] = fun_ction1(panel,'adj_dist_tax_M&O_rate',1)
panel['adj_dist_tax_M&O_rate_2'] = fun_ction1(panel,'adj_dist_tax_M&O_rate',2)

panel = panel.drop(
['Distance_alldist_min_10r','Distance_indist_min_10r',
'Distance_alldist_miles_5r', 'Distance_indist_miles_5r',
'adj_dist_total_rev', 'adj_dist_local_rev', 'adj_dist_state_rev',
'adj_dist_total_val_per_pupil', 'adj_dist_total_val',
'adj_dist_oil_val', 'adj_dist_wealth_transfers',
'adj_dist_tax_M&O_rate', 'adj_dist_total_tax_rate']
,axis=1)

panel.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/full_reg_panel.csv')




#
