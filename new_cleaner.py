import pandas as pd


school_data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Formatted_Data/Campus_Nutrition_Reimbursement/2017-18/School_Nutrition_Programs___Contact_Information_and_Site-Level_Program_Participation___Program_Year_2017-2018.csv', dtype = str)
school_data = school_data.rename(columns = {'CEName':'dist_name'})
school_data['Location'] = school_data['SiteName'].str.replace(' ','+')+'+'+school_data['dist_name'].str.replace(' ','+')
panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel.csv', dtype = str)
sub_schools = school_data[(school_data['Grade3']=='Y')&(school_data['Grade4']=='Y')&(school_data['Grade5']=='Y')]
sub_schools['Campus'] = sub_schools['CountyDistrictCode'].str[:]+sub_schools['SiteID'].str[1:]
small_pan = panel[panel['Year']=='2005'].sort_values('dist_name')
small_pan = small_pan[small_pan['Campus'].isin(sub_schools['Campus'].values)]
panel = panel[panel['Campus'].isin(small_pan['Campus'].values)]

adj_pan = pd.read_csv('/Users/vincentcarse/Github/EC331/Regression_data/VAM_reg/new_balanced_panel2.csv')
