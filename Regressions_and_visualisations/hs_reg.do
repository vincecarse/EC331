clear
import delimited /Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel_real_hs.csv



#dummy variables
tabulate description, gen(var)
gen recapture  = (dist_wealth_transfers>0)

#lags
gen taks_math_gr9_lag1 = taks_math_gr9[_n-1]
gen taks_reading_gr9_lag1 = taks_reading_gr9[_n-1]

#units changes 

gen dist_total_rev_per_pupil = dist_total_rev/all_stud_dist
gen dist_local_rev_per_pupil = dist_local_rev/all_stud_dist
gen dist_state_rev_per_pupil = dist_state_rev/all_stud_dist
gen dist_other_rev_per_pupil = dist_other_rev/all_stud_dist
gen dist_federal_rev_per_pupil = dist_federal_rev/all_stud_dist
gen dist_oil_val_per_pupil = dist_oil_val/all_stud_dist
gen dist_wealth_transfers_per_pupil = dist_wealth_transfers/all_stud_dist

gen taks_reading_gr10 = taks_ela_gr10


#mean_differences
egen dist_total_val_per_pupil_mean  = mean(dist_total_val_per_pupil)
gen dist_total_val_per_pupil_demean  = dist_total_val_per_pupil - dist_total_val_per_pupil_mean


xtset campus year


###      math      ###



eststo clear

#delimit ;

quietly reg taks_math_gr10 taks_math_gr9_lag1  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience math_class_size;

#delimit cr

estadd local fe No

eststo




#delimit ;

quietly xtreg taks_math_gr10 taks_math_gr9_lag1  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience math_class_size, fe ;

#delimit cr

estadd local fe Yes

eststo




#delimit ;

quietly xtreg taks_math_gr10 taks_math_gr9_lag1  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience math_class_size i.year, fe ;

#delimit cr

estadd local fe Yes

eststo




#delimit ;

quietly xtreg taks_math_gr10 taks_math_gr9_lag1  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience math_class_size i.year if var3, fe ;

#delimit cr

estadd local fe Yes

eststo



#delimit ;

quietly xtreg taks_math_gr10 taks_math_gr9_lag1  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience math_class_size i.year if var4, fe ;

#delimit cr

estadd local fe Yes

eststo


#delimit ;

quietly xtreg taks_math_gr10 taks_math_gr9_lag1  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience math_class_size i.year if var7, fe ;

#delimit cr

estadd local fe Yes

eststo

###


#delimit ;

###using math_gr10.tex

esttab , nodepvars mlabels(none) ar2 indicate("year fe = *year") nonotes addnotes(
"(1),(2),(3) - Whole Sample"
"(4) - Suburban Areas, Major Cities"
"(5) - Urban Areas, Major Cities"
"(6) - Rural Areas")

title("Dependent Variable - Gr10 Math Score")
coef(taks_math_gr10 "Gr10 Math Score"  taks_math_gr9_lag1   "Gr9 Math Lag"
per_pupil_exp "Per Pupil Exp" econ_dis_stu_percent "Perc Econ Disadv"
teacher_avg_salary "T Avg Sal" teacher_experience "T Exp"
math_class_size "Math Class Size" _cons "Constant")

 stats(N  fe, labels("N"))

 ;

#delimit cr


###      english      ###


eststo clear

#delimit ;

quietly reg taks_reading_gr10 taks_reading_gr9_lag1  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience eng_class_size;

#delimit cr

estadd local fe No

eststo




#delimit ;

quietly xtreg taks_reading_gr10 taks_reading_gr9_lag1  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience eng_class_size, fe ;

#delimit cr

estadd local fe Yes

eststo




#delimit ;

quietly xtreg taks_reading_gr10 taks_reading_gr9_lag1  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience eng_class_size i.year, fe ;

#delimit cr

estadd local fe Yes

eststo




#delimit ;

quietly xtreg taks_reading_gr10 taks_reading_gr9_lag1  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience eng_class_size i.year if var3, fe ;

#delimit cr

estadd local fe Yes

eststo



#delimit ;

quietly xtreg taks_reading_gr10 taks_reading_gr9_lag1  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience eng_class_size i.year if var4, fe ;

#delimit cr

estadd local fe Yes

eststo


#delimit ;

quietly xtreg taks_reading_gr10 taks_reading_gr9_lag1  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience eng_class_size i.year if var7, fe ;

#delimit cr

estadd local fe Yes

eststo

###


#delimit ;


esttab , nodepvars mlabels(none) ar2 indicate("year fe = *year") nonotes addnotes(
"(1),(2),(3) - Whole Sample"
"(4) - Suburban Areas, Major Cities"
"(5) - Urban Areas, Major Cities"
"(6) - Rural Areas")

title("Dependent Variable - Gr10 English Score")
coef(taks_reading_gr10 "Gr10 English Score"  taks_reading_gr9_lag1   "Gr9 Eng Lag"
per_pupil_exp "Per Pupil Exp" econ_dis_stu_percent "Perc Econ Disadv"
teacher_avg_salary "T Avg Sal" teacher_experience "T Exp"
eng_class_size "Class Size" _cons "Constant")

 stats(N fe, labels("N"))

 ;

#delimit cr

