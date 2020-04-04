clear
import delimited /Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/big_panel.csv 

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

#interactions 

gen exp = teacher_experience*exp_w_dist
gen exp_sal = teacher_avg_salary*teacher_experience


###      models      ###

xtset year

#delimit ;

xtreg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2 per_pupil_exp 
econ_dis_stu_percent teacher_avg_salary teacher_experience 
exp_w_dist gr5_class_size, fe ;


#delimit cr




xtreg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2 per_pupil_exp econ_dis_stu_percent teacher_avg_salary teacher_experience exp_sal exp_w_dist exp gr5_class_size, fe 



xtreg taks_math_gr5 per_pupil_exp
