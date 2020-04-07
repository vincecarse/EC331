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
gen num_adj_sub = total_miles_5r*var2
gen num_adj_urb = total_miles_5r*var3
gen num_adj_oth = total_miles_5r*var6
#gen adj_exp = total_miles_5r*var6

###      models      ###

xtset campus 

#delimit ;

xtreg taks_reading_gr5 taks_reading_gr4_lag1 
taks_reading_gr3_lag2 per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience exp_w_dist  
exp_sal exp gr5_class_size i.year, fe ;

#delimit cr


#delimit ;

xtreg taks_math_gr5 taks_math_gr4_lag1 
taks_math_gr3_lag2 per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience exp_w_dist  
exp_sal exp gr5_class_size i.year, fe ;

#delimit cr




