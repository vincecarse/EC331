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


#logs

gen log_per_pupil_exp = log(per_pupil_exp)
gen log_dist_local_rev_per_pupil = log(dist_local_rev_per_pupil)
gen log_dist_state_rev_per_pupil = log(dist_state_rev_per_pupil)
gen log_dist_total_val_per_pupil = log(dist_total_val_per_pupil)
gen log_taks_math_gr5 = log(taks_math_gr5)

#mean_differences
egen dist_total_val_per_pupil_mean  = mean(dist_total_val_per_pupil)
gen dist_total_val_per_pupil_demean  = dist_total_val_per_pupil - dist_total_val_per_pupil_mean

#powers
gen dist_local_rev_per_pupil_2 = dist_local_rev_per_pupil^2
gen dist_state_rev_per_pupil_2 = dist_state_rev_per_pupil^2
gen dist_other_rev_per_pupil_2 = dist_other_rev_per_pupil^2
gen dist_federal_rev_per_pupil_2 = dist_federal_rev_per_pupil^2
gen dist_total_rev_per_pupil_2 = dist_total_rev_per_pupil^2
gen dist_total_val_per_pupil_2 = dist_total_val_per_pupil^2
gen dist_total_val_per_pupil_3 = dist_total_val_per_pupil^3
gen dist_total_val_per_pupil_dm_2 = dist_total_val_per_pupil_demean^2



###      models      ###

xtset campus year

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

reg d.taks_reading_gr5 d.taks_reading_gr4_lag1 
d.taks_reading_gr3_lag2 d.per_pupil_exp  d.dist_total_val_per_pupil d.val_exp 
d.econ_dis_stu_percent d.teacher_avg_salary d.teacher_experience d.exp_w_dist  
d.exp_sal d.exp d.gr5_class_size i.district ;

#delimit cr


#delimit ;

reg d.taks_math_gr5 d.taks_math_gr4_lag1 
d.taks_math_gr3_lag2 d.per_pupil_exp  d.dist_total_val_per_pupil d.val_exp 
d.econ_dis_stu_percent d.teacher_avg_salary d.teacher_experience d.exp_w_dist  
d.exp_sal d.exp d.gr5_class_size i.district ;

#delimit cr


#delimit ;

xtreg taks_reading_gr5 taks_reading_gr4_lag1 
taks_reading_gr3_lag2 per_pupil_exp 
econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist  
exp_sal exp gr5_class_size i.year, fe ;

#delimit cr

#delimit ;

xtreg taks_math_gr5 taks_math_gr4_lag1 
taks_math_gr3_lag2 per_pupil_exp 
econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist  
exp_sal exp gr5_class_size i.year, fe ;

#delimit cr

#delimit ;

xtreg taks_reading_gr5 taks_reading_gr4_lag1 
taks_reading_gr3_lag2 log_per_pupil_exp 
econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist  
exp_sal exp gr5_class_size i.year, fe ;

#delimit cr

#delimit ;

xtreg taks_math_gr5 taks_math_gr4_lag1 
taks_math_gr3_lag2 per_pupil_exp 
econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist  
exp_sal exp gr5_class_size i.year, fe ;

#delimit cr
