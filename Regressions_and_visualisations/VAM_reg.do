import delimited /Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/big_panel.csv 

#dummy variables
tabulate description, gen(var)
gen recapture  = (dist_wealth_transfers>0)
gen small_school  = (all_stud_count<300)
gen small_gr3  = (gr3_class_size<20)
gen small_gr4  = (gr4_class_size<20)
gen small_gr5  = (gr5_class_size<20)


#lags
gen taks_math_gr3_lag1 = taks_math_gr3[_n-1]
gen taks_math_gr3_lag2 = taks_math_gr3[_n-2]
gen taks_math_gr4_lag1 = taks_math_gr4[_n-1]
gen taks_reading_gr3_lag1 = taks_reading_gr3[_n-1]
gen taks_reading_gr3_lag2 = taks_reading_gr3[_n-2]
gen taks_reading_gr4_lag1 = taks_reading_gr4[_n-1]

#interactions 



###      models      ###

xtset year

#base
xtreg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2 per_pupil_exp econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist gr5_class_size, fe
xtreg taks_reading_gr5 taks_reading_gr4_lag1 taks_reading_gr3_lag2 per_pupil_exp econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist gr5_class_size, fe

#suburban
xtreg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2 per_pupil_exp econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist gr5_class_size, fe, if var3
xtreg taks_reading_gr5 taks_reading_gr4_lag1 taks_reading_gr3_lag2 per_pupil_exp econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist gr5_class_size, fe, if var3

#urban
xtreg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2 per_pupil_exp econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist gr5_class_size, fe, if var4
xtreg taks_reading_gr5 taks_reading_gr4_lag1 taks_reading_gr3_lag2 per_pupil_exp econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist gr5_class_size, fe, if var3

#close substitutes
xtreg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2 per_pupil_exp econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist gr5_class_size, fe, if distance_min_10r > 20
xtreg taks_reading_gr5 taks_reading_gr4_lag1 taks_reading_gr3_lag2 per_pupil_exp econ_dis_stu_percent teacher_avg_salary teacher_experience exp_w_dist gr5_class_size, fe, if distance_min_10r > 20














