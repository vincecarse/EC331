import pandas as pd


panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel2.csv')
small_pan = panel[panel['Distance_adj_miles'].isna()==False]
small_pan[['Distance_adj_min','Distance_adj_miles']]
fin_file = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/fin_file.csv')

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

a = set()
for i in small_pan['adj_dist'].values:
    for j in i:
        if not '"' in j:
            a.add(j.upper())

adj_dists = list(a)
small_fin_file = fin_file[fin_file['dist_name'].isin(adj_dists)]
small_fin_file = small_fin_file[['dist_name','DISTRICT','Year','dist_tax_M&O_rate','dist_total_tax_rate', 'dist_total_rev', 'dist_local_rev',
'dist_state_rev', 'dist_total_val_per_pupil', 'dist_total_val',
'dist_oil_val', 'dist_wealth_transfers']]
small_fin_file = small_fin_file.drop_duplicates()

def dist_extractor(data_file,finance_file,variable,year):
    a = []
    for i in data_file.index:
        b = []
        for j in data_file['adj_dist'][i]:
            try:
                b.append(finance_file[(finance_file['dist_name']==j.upper())&(finance_file['Year']==year)][variable].values[0])
            except IndexError:
                b.append('')
        a.append(b)
    return(a)

def year_merger(file,year):
    data = file[['Campus','dist_name']].copy()
    data['Year'] = year
    data['adj_dist_total_rev'] = dist_extractor(small_pan,fin_file,'dist_total_rev',year)
    data['adj_dist_local_rev'] = dist_extractor(small_pan,fin_file,'dist_local_rev',year)
    data['adj_dist_state_rev'] = dist_extractor(small_pan,fin_file,'dist_state_rev',year)
    data['adj_dist_total_val_per_pupil'] = dist_extractor(small_pan,fin_file,'dist_total_val_per_pupil',year)
    data['adj_dist_total_val'] = dist_extractor(small_pan,fin_file,'dist_total_val',year)
    data['adj_dist_oil_val'] = dist_extractor(small_pan,fin_file,'dist_oil_val',year)
    data['adj_dist_wealth_transfers'] = dist_extractor(small_pan,fin_file,'dist_wealth_transfers',year)
    data['adj_dist_tax_M&O_rate'] = dist_extractor(small_pan,fin_file,'dist_tax_M&O_rate',year)
    data['adj_dist_total_tax_rate'] = dist_extractor(small_pan,fin_file,'dist_total_tax_rate',year)
    return(data.astype(str))

x = year_merger(small_pan,2003)
y = year_merger(small_pan,2004)
test = pd.merge(x,y,on =['Campus','dist_name','Year', 'adj_dist_total_rev', 'adj_dist_local_rev',
'adj_dist_state_rev', 'adj_dist_total_val_per_pupil', 'adj_dist_total_val','adj_dist_oil_val','adj_dist_wealth_transfers','adj_dist_tax_M&O_rate','adj_dist_total_tax_rate'],how = 'outer')

for i in fin_file.Year.unique():
    test = pd.merge(test,year_merger(small_pan,i),on =['Campus','dist_name','Year', 'adj_dist_total_rev', 'adj_dist_local_rev',
    'adj_dist_state_rev', 'adj_dist_total_val_per_pupil', 'adj_dist_total_val','adj_dist_oil_val','adj_dist_wealth_transfers','adj_dist_tax_M&O_rate','adj_dist_total_tax_rate'],how = 'outer')
    print(str(i))

test.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/dist_data_panel.csv')










####


x = year_merger(small_pan,2003)
y = year_merger(small_pan,2004)
test = pd.merge(x,y,on =['Campus','dist_name','Year','adj_dist_total_rev'], how ='outer')

for i in fin_file.Year.unique():
    test = pd.merge(test,year_merger(small_pan,i),on =['Campus','dist_name','Year','adj_dist_total_rev'], how ='outer')

small_pan.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/dist_panel.csv')


#
