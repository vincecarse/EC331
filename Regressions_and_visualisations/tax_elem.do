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
gen capped = (recapture)&(dist_tax_mo_rate>=1.5)

#lags
gen taks_math_gr3_lag1 = taks_math_gr3[_n-1]
gen taks_math_gr3_lag2 = taks_math_gr3[_n-2]
gen taks_math_gr4_lag1 = taks_math_gr4[_n-1]
gen taks_reading_gr3_lag1 = taks_reading_gr3[_n-1]
gen taks_reading_gr3_lag2 = taks_reading_gr3[_n-2]
gen taks_reading_gr4_lag1 = taks_reading_gr4[_n-1]





eststo clear


reg taks_math_gr5 total_min_10r if var3
eststo 

reg taks_math_gr5 total_min_10r if var4
eststo 

reg taks_math_gr5 total_min_10r if var7
eststo 



reg taks_reading_gr5 total_min_10r if var3
eststo 

reg taks_reading_gr5 total_min_10r if var4
eststo 

reg taks_reading_gr5 total_min_10r if var7
eststo 



#delimit ;

### 

esttab using prox.tex,  ar2  nonotes  addnotes(
"(1),(4) - Large Suburban"
"(2),(5) - Large Urban"
"(3),(6) - Rural")


title("Proximity Regressions - Independent variable: Number of elementary schools in 10 minute (driving) radius")


 ;


eststo clear
reg taks_math_gr5 per_pupil_exp if capped
eststo 
reg taks_reading_gr5 per_pupil_exp if capped
eststo 

#delimit ;

###using capped.tex

esttab ,  ar2  nonotes  addnotes(
"(1),(2) - First stages"
"(3) - Relevance"
"(4),(5) - IV")


title("IV Regressions - Instrument: dist_oil_val_per_pupil")


 ;



