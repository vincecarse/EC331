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

esttab using new_math_gr10.tex, stats(fe, labels("fe")) indicate("year fe = *year") 
coef(taks_math_gr10 "Grade 10 Math Score" taks_math_gr9_lag1 "Grade 9 Math Score Lagged"
per_pupil_exp "Per Pupil Expenditure" econ_dis_stu_percent "Percent Economically Disadvantaged"
teacher_avg_salary "Teacher Average Salary" teacher_experience "Teacher Years Expereince"
math_class_size "Math Class Size" _cons "Constant"

) ;

#delimit cr


eststo clear


#delimit ;

quietly reg taks_ela_gr10 taks_reading_gr9_lag1 
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience eng_class_size;

#delimit cr

estadd local fe No

eststo

#delimit ;

quietly xtreg taks_ela_gr10 taks_reading_gr9_lag1 
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience eng_class_size, fe ;

#delimit cr

estadd local fe Yes

eststo

#delimit ;

quietly xtreg taks_ela_gr10 taks_reading_gr9_lag1 
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience eng_class_size i.year, fe ;

#delimit cr

estadd local fe Yes

eststo

#delimit ;

quietly xtreg taks_ela_gr10 taks_reading_gr9_lag1 
per_pupil_exp econ_dis_stu_percent 
teacher_avg_salary teacher_experience eng_class_size i.year if var3, fe ;

#delimit cr

estadd local fe Yes

eststo

#delimit ;

esttab using new_eng_gr10.tex, stats(fe, labels("fe")) indicate("year fe = *year") 

coef(taks_ela_gr10 "Grade 10 Reading Score" taks_reading_gr9_lag1 "Grade 9 Reading Score Lagged"
per_pupil_exp "Per Pupil Expenditure" econ_dis_stu_percent "Percent Economically Disadvantaged"
teacher_avg_salary "Teacher Average Salary" teacher_experience "Teacher Years Expereince"
eng_class_size "English Class Size" _cons "Constant")
 ;

#delimit cr

### depvars drop(*year)
