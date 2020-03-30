import pandas as pd

dists = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Texas_School_GIS/AdjacentDistrict.csv')
dists = dists.rename(columns = {'District Number':'District','District Name':'dist_name'})
panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel.csv')
panel = panel.rename(columns = {'dist_name_y':'dist_name'})

a = []
for i in dists.index:
    b = []
    for j in dists.iloc[i][2:]:
        b.append(j)
        b = [i for i in b if (str(i) != 'nan')&(str(i)[-3:]=='ISD')]
    a.append(b)

dists['adj_dist'] = a
dists['adj_dist'] = dists['adj_dist'].astype(str)
merge_dists = dists[['District','adj_dist']]
panel = pd.merge(panel,merge_dists, on ='District')
test = panel[['dist_name','adj_dist']]
test1 = test.drop_duplicates()

#


school_data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Nutrition_Reimbursement/2017-18/School_Nutrition_Programs___Contact_Information_and_Site-Level_Program_Participation___Program_Year_2017-2018.csv', dtype = str)
school_data = school_data.rename(columns = {'CEName':'dist_name'})
school_data['Location'] = school_data['SiteName'].str.replace(' ','+')+'+'+school_data['dist_name'].str.replace(' ','+')
sub_schools = school_data[(school_data['Grade3']=='Y')&(school_data['Grade4']=='Y')&(school_data['Grade5']=='Y')]
camps = []

for i in sub_schools['dist_name'].unique():
    camps.append(list(list(sub_schools[sub_schools['dist_name']==i]['Location'].unique())))

camps_in_dists = pd.DataFrame(sub_schools['dist_name'].unique(), columns = ['dist_name'])
camps_in_dists['schools'] = camps

try:
    test1['adj_dist']= test1['adj_dist'].str[2:-2].str.split("', '")
except AttributeError:
    print('n/a')

w = []
for i in test1.index:
    v = []
    for j in test1['adj_dist'][i]:
        try:
            v.append(list(camps_in_dists[camps_in_dists['dist_name'] == j.upper()]['schools'])[0])
        except IndexError:
            v.append([''])
    w.append(v)

test1['adj_dist_schools'] = w
test1['adj_dist_schools'] = test1['adj_dist_schools'].replace("], [","],  [")
test2 = test1[['dist_name','adj_dist_schools']]
panel = pd.merge(panel,test2, how = 'outer',on = 'dist_name')
panel.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel2.csv')


panel['adj_dist_schools'][20]


#
