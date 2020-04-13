clear
import delimited /Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel.csv 



#dummy variables
tabulate description, gen(var)
gen recapture  = (dist_wealth_transfers>0)

#lags
gen taks_math_gr3_lag1 = taks_math_gr3[_n-1]
gen taks_math_gr3_lag2 = taks_math_gr3[_n-2]
gen taks_math_gr4_lag1 = taks_math_gr4[_n-1]
gen taks_reading_gr3_lag1 = taks_reading_gr3[_n-1]
gen taks_reading_gr3_lag2 = taks_reading_gr3[_n-2]
gen taks_reading_gr4_lag1 = taks_reading_gr4[_n-1]

#units changes 

gen dist_total_rev_per_pupil = dist_total_rev/all_stud_dist
gen dist_local_rev_per_pupil = dist_local_rev/all_stud_dist
gen dist_state_rev_per_pupil = dist_state_rev/all_stud_dist
gen dist_other_rev_per_pupil = dist_other_rev/all_stud_dist
gen dist_federal_rev_per_pupil = dist_federal_rev/all_stud_dist
gen dist_oil_val_per_pupil = dist_oil_val/all_stud_dist
gen dist_wealth_transfers_per_pupil = dist_wealth_transfers/all_stud_dist

#interactions 

gen exp = teacher_experience*exp_w_dist
gen exp_sal = teacher_avg_salary*teacher_experience
gen val_exp = dist_total_val_per_pupil*per_pupil_exp
gen dist_local_rev_per_pupil_x_val = dist_local_rev_per_pupil*dist_total_val_per_pupil
gen dist_state_rev_per_pupil_x_val = dist_state_rev_per_pupil*dist_total_val_per_pupil
gen dist_other_rev_per_pupil_x_val = dist_other_rev_per_pupil*dist_total_val_per_pupil
gen dist_federal_rev_per_pupil_x_val = dist_federal_rev_per_pupil*dist_total_val_per_pupil
gen dist_local_rev_per_pupil_2 = dist_local_rev_per_pupil^2
gen dist_state_rev_per_pupil_2 = dist_state_rev_per_pupil^2
gen dist_other_rev_per_pupil_2 = dist_other_rev_per_pupil^2
gen dist_federal_rev_per_pupil_2 = dist_federal_rev_per_pupil^2

###      regressions      ###

xtset district 

#delimit ;

reg per_pupil_exp  
black_stu_percent spec_ed_stu_percent econ_dis_stu_percent
dist_local_rev_per_pupil
dist_state_rev_per_pupil dist_federal_rev_per_pupil 
dist_other_rev_per_pupil dist_total_val_per_pupil
dist_wealth_transfers dist_total_tax_rate
i.year;

#delimit cr

