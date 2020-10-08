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


eststo clear

reg taks_ela_gr10 per_pupil_exp
eststo
reg taks_math_gr10 per_pupil_exp
eststo
reg per_pupil_exp dist_oil_val_per_pupil
eststo
ivregress 2sls taks_ela_gr10 (per_pupil_exp = dist_oil_val_per_pupil) 
eststo
ivregress 2sls taks_math_gr10 (per_pupil_exp = dist_oil_val_per_pupil) 
eststo

#delimit ;

###

esttab using iv.tex,  ar2  nonotes  addnotes(
"(1),(2) - First stages"
"(3) - Relevance"
"(4),(5) - IV")


title("IV Regressions - Instrument: dist_oil_val_per_pupil")


 ;



