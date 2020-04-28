clear
import delimited /Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel.csv 



#dummy variables
tabulate description, gen(var)
gen recapture  = (dist_wealth_transfers>0)
gen oil  = (dist_oil_val>0)

#proportions
gen taks_math_gr5_prop = taks_math_gr5/100
gen taks_math_gr4_prop = taks_math_gr4/100
gen taks_math_gr3_prop = taks_math_gr3/100
gen taks_reading_gr5_prop = taks_reading_gr5/100
gen taks_reading_gr4_prop = taks_reading_gr4/100
gen taks_reading_gr3_prop = taks_reading_gr3/100

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
gen log_taks_reading_gr4 = log(taks_reading_gr4)
gen log_taks_reading_gr3 = log(taks_reading_gr3)

#mean_differences
bysort campus: egen econ_dis_stu_percent_mean  = mean(econ_dis_stu_percent)
gen econ_dis_stu_percent_demean  = econ_dis_stu_percent - econ_dis_stu_percent_mean
bysort campus: egen taks_math_gr5_mean  = mean(taks_math_gr5)
gen taks_math_gr5_demean  = taks_math_gr5 - taks_math_gr5_mean

#powers
gen dist_local_rev_per_pupil_2 = dist_local_rev_per_pupil^2
gen dist_state_rev_per_pupil_2 = dist_state_rev_per_pupil^2
gen dist_other_rev_per_pupil_2 = dist_other_rev_per_pupil^2
gen dist_federal_rev_per_pupil_2 = dist_federal_rev_per_pupil^2
gen dist_total_rev_per_pupil_2 = dist_total_rev_per_pupil^2
gen dist_total_val_per_pupil_2 = dist_total_val_per_pupil^2
gen dist_total_val_per_pupil_3 = dist_total_val_per_pupil^3
gen econ_dis_stu_percent_2 = econ_dis_stu_percent^2



###      models      ###



#delimit ;

reg taks_reading_gr5 taks_reading_gr4_lag1 taks_reading_gr3_lag2  
per_pupil_exp econ_dis_stu_percent
teacher_avg_salary teacher_experience gr5_class_size i.year
if (district  == 57905) ; 

#delimit cr



#delimit ;

reg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2  
per_pupil_exp econ_dis_stu_percent
teacher_avg_salary teacher_experience gr5_class_size i.year
if (district  == 57905); 

#delimit cr


#delimit ;

reg taks_reading_gr5 taks_reading_gr4_lag1 taks_reading_gr3_lag2  
per_pupil_exp econ_dis_stu_percent
teacher_avg_salary teacher_experience gr5_class_size
if (district  == 57905)&(year == 2006) ; 

#delimit cr



#delimit ;

reg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2  
per_pupil_exp econ_dis_stu_percent
teacher_avg_salary teacher_experience gr5_class_size
if (district  == 57905)&(year == 2006) ; 

#delimit cr






