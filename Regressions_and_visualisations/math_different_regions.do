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


esttab using math_gr10.tex, nodepvars mlabels(none) ar2 indicate("year fe = *year") nonotes addnotes(
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


