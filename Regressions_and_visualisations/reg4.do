clear
import delimited /Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/full_reg_panel.csv 

#missing values
recode adj_dist_wealth_transfers_0 (missing=0), gen(new_adj_dist_wealth_transfers_0)
recode adj_dist_oil_val_0 (missing=0), gen(new_adj_dist_oil_val_0)


#dummy variables
tabulate description, gen(var)
gen adj_dist_wealth_transfers_dum = (new_adj_dist_oil_val_0>0)
gen adj_dist_oil_val_dum  = (new_adj_dist_oil_val_0>0)
gen recapture  = (dist_wealth_transfers>0)

#lags
gen taks_math_gr3_lag1 = taks_math_gr3[_n-1]
gen taks_math_gr3_lag2 = taks_math_gr3[_n-2]
gen taks_math_gr4_lag1 = taks_math_gr4[_n-1]
gen taks_reading_gr3_lag1 = taks_reading_gr3[_n-1]
gen taks_reading_gr3_lag2 = taks_reading_gr3[_n-2]
gen taks_reading_gr4_lag1 = taks_reading_gr4[_n-1]

#interactions 

gen exp = teacher_experience*exp_w_dist
gen exp_sal = teacher_avg_salary*teacher_experience
gen val_exp = dist_total_val_per_pupil*per_pupil_exp



#units changes 

gen dist_total_rev_per_pupil = dist_total_rev/all_stud_dist
gen dist_local_rev_per_pupil = dist_local_rev/all_stud_dist
gen dist_state_rev_per_pupil = dist_state_rev/all_stud_dist
gen dist_oil_val_per_pupil = dist_oil_val/all_stud_dist
gen dist_wealth_transfers_per_pupil = dist_wealth_transfers/all_stud_dist




###      models      ###

xtset district

#delimit ;

xtreg taks_reading_gr5 taks_reading_gr4_lag1 
taks_reading_gr3_lag2 per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience exp_w_dist  
exp_sal exp gr5_class_size, fe ;

#delimit cr

estimates store random

#delimit ;

xtreg taks_reading_gr5 taks_reading_gr4_lag1 
taks_reading_gr3_lag2 per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience exp_w_dist  
exp_sal exp gr5_class_size, fe ;

#delimit cr

estimates store fixed



hausman fixed random

#delimit ;

xtreg taks_math_gr5 taks_math_gr4_lag1 
taks_math_gr3_lag2 per_pupil_exp dist_total_val_per_pupil val_exp 
econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist  
exp_sal exp gr5_class_size i.year, fe ;

#delimit cr



#delimit ;

xtreg taks_reading_gr5 taks_reading_gr4_lag1 
taks_reading_gr3_lag2 per_pupil_exp  dist_total_val_per_pupil val_exp 
econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist  
exp_sal exp gr5_class_size i.year, fe ;

#delimit cr



#delimit ;

reg taks_reading_gr5 taks_reading_gr4_lag1 
taks_reading_gr3_lag2 per_pupil_exp  dist_total_val_per_pupil val_exp 
econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist  
exp_sal exp gr5_class_size i.district i.year ;

#delimit cr

