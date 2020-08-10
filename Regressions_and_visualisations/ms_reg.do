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

xtset campus year

###      math      ###



eststo clear

#delimit ;

quietly reg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience gr5_class_size;

#delimit cr

estadd local fe No

eststo




#delimit ;

quietly xtreg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience gr5_class_size, fe ;

#delimit cr

estadd local fe Yes

eststo




#delimit ;

quietly xtreg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience gr5_class_size i.year, fe ;

#delimit cr

estadd local fe Yes

eststo




#delimit ;

quietly xtreg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience gr5_class_size i.year if var3, fe ;

#delimit cr

estadd local fe Yes

eststo



#delimit ;

quietly xtreg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience gr5_class_size i.year if var4, fe ;

#delimit cr

estadd local fe Yes

eststo


#delimit ;

quietly xtreg taks_math_gr5 taks_math_gr4_lag1 taks_math_gr3_lag2  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience gr5_class_size i.year if var7, fe ;

#delimit cr

estadd local fe Yes

eststo

###


#delimit ;


esttab using math_gr5.tex, nodepvars mlabels(none) ar2 indicate("year fe = *year") nonotes addnotes(
"(1),(2),(3) - Whole Sample"
"(4) - Suburban Areas, Major Cities"
"(5) - Urban Areas, Major Cities"
"(6) - Rural Areas")

title("Dependent Variable - Gr5 Math Score")
coef(taks_math_gr5 "Gr5 Math Score"  taks_math_gr4_lag1   "Gr9 Math Lag" taks_math_gr3_lag2   "Gr3 Math Lag2"
per_pupil_exp "Per Pupil Exp" econ_dis_stu_percent "Perc Econ Disadv"
teacher_avg_salary "T Avg Sal" teacher_experience "T Exp"
gr5_class_size "Class Size" _cons "Constant")

 stats(N  fe, labels("N"))

 ;

#delimit cr


###      english      ###


eststo clear

#delimit ;

quietly reg taks_reading_gr5 taks_reading_gr4_lag1 taks_reading_gr3_lag2  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience gr5_class_size;

#delimit cr

estadd local fe No

eststo




#delimit ;

quietly xtreg taks_reading_gr5 taks_reading_gr4_lag1 taks_reading_gr3_lag2  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience gr5_class_size, fe ;

#delimit cr

estadd local fe Yes

eststo




#delimit ;

quietly xtreg taks_reading_gr5 taks_reading_gr4_lag1 taks_reading_gr3_lag2  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience gr5_class_size i.year, fe ;

#delimit cr

estadd local fe Yes

eststo




#delimit ;

quietly xtreg taks_reading_gr5 taks_reading_gr4_lag1 taks_reading_gr3_lag2  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience gr5_class_size i.year if var3, fe ;

#delimit cr

estadd local fe Yes

eststo



#delimit ;

quietly xtreg taks_reading_gr5 taks_reading_gr4_lag1 taks_reading_gr3_lag2  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience gr5_class_size i.year if var4, fe ;

#delimit cr

estadd local fe Yes

eststo


#delimit ;

quietly xtreg taks_reading_gr5 taks_reading_gr4_lag1 taks_reading_gr3_lag2  
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience gr5_class_size i.year if var7, fe ;

#delimit cr

estadd local fe Yes

eststo

###


#delimit ;


esttab using eng_gr5.tex, nodepvars mlabels(none) ar2 indicate("year fe = *year") nonotes addnotes(
"(1),(2),(3) - Whole Sample"
"(4) - Suburban Areas, Major Cities"
"(5) - Urban Areas, Major Cities"
"(6) - Rural Areas")

title("Dependent Variable - Gr5 English Score")
coef(taks_reading_gr5 "Gr5 English Score"  taks_reading_gr4_lag1   "Gr4 Eng Lag" taks_reading_gr3_lag2   "Gr3 Eng Lag2"
per_pupil_exp "Per Pupil Exp" econ_dis_stu_percent "Perc Econ Disadv"
teacher_avg_salary "T Avg Sal" teacher_experience "T Exp"
gr5_class_size "Class Size" _cons "Constant")

 stats(N fe, labels("N"))

 ;

#delimit cr






