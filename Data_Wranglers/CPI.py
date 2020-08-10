import pandas as pd

CPI = [1,
1.025380711,
1.062041737,
1.098138748,
1.130067682,
1.176993796,
1.172278624,
1.191979695,
1.233040045]

Years = [2003,
2004,
2005,
2006,
2007,
2008,
2009,
2010,
2011]

#from BLS, 2003-2011 normalised

data = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel_hs.csv')


a = []
for i in data['Year'].values:
    for j in range(len(Years)):
        if Years[j] == i:
            a.append(CPI[j])

data['CPI'] = a

money_vars = ['per_pupil_exp', 'per_pupil_instruction', 'per_pupil_leadership',
'per_pupil_othr', 'teacher_avg_salary',
'dist_total_rev', 'dist_other_rev', 'dist_federal_rev',
'dist_local_rev', 'dist_state_rev', 'dist_total_val_per_pupil',
'dist_total_val', 'dist_oil_val', 'dist_wealth_transfers']

for i in money_vars:
    name = i+'_real'
    vals = data[i]/data['CPI']
    data[i] = vals

data.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel_real_hs.csv')
