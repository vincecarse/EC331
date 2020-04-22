## New Features
 - District expenditure items (teacher pensions?)
 - Create charter subset


## Stuff to fix
- Check all data is actually from the correct/same year
- Use percent expenditures (e.g. for oil and gas) and then multiply that by per pupil to get per pupil oil and gas.
- Fix 'alignment' of district distance data by rows (2 row lag from 262)
- big_panel is missing lots of distance data for some reason?
- Could go through and try to recalculate the 'error' distances again
  - Only have to do this for districts with schools (['']'s call errors)

## General to do
- Create variables for whether a district is at its revenue threshold
  - Create 'gap' variables, like how difference between two bordering districts' wealth/spending levels changes
  - Also consider comparing 'macro' differences in student/teacher characteristics
- Link district info to distance
  - Requires using 'dist_info_file' and 'big_panel2'
- Could go back to '96/'97 and get info from then too (won't have as good school data though)
- Trace through district-level changes on school-level changes
  - E.g. tax rates/property wealth etc. on funding
  - Then consider different 'bundles' of school choices (class sizes, teacher salaries etc)
- Could look at:
  - Property booms
  - Tax rate shifts
  - Oil/Gas shocks
  - Redistribution
- Test pooled vs fe regression significances
- Look at using GLS for a fixed-effects specification
- Start writing

## Thoughts
- Look at non-linearities in teacher experience
- District fixed effects
  - Use different specifications
  - Potentially look at IO papers for ideas
- Oil shocks
- Use distances data for each campus better
- Consider robustness checks
- Could do a DiD estimate for hitting revenue thresholds, or being around a district which does
  - Could use variation in proximity to neighbouring districts?
  - Could compare teacher years of experience or student numbers
  - Could just be a robustness check
- Could test border effects at the school level
  -  Use number of nearby substitute schools as a measure of 'exposure' to changes in other districts' policies
  - Then could compare this with changes in schools in other parts of the district which weren't exposed
- How to deal with having school-substitutes being correlated with being in an urban area?
  - Could confine study to urban areas
  - Breakdown would be urban vs. suburban
- Weighted average for campuses with adjacent districts
  - Or other measures
- Look at first differences of oil values and funding
- Variation of funding effects
  - Poor/rich neighbourhood or rural/urban
- Set t=1 observations as missing
- Need to test for serial correlation in errors
- Think about using GLS to deal with serial correlation
   - Try and estimate the 'theta' parameter
- Simultaneous equation for funding?
- Include simple equations which build to more complex ones
- Include interaction terms as mean-differenced?
- Are there other variables I can include to reduce the standard errors of my estimates?

## Questions
- How to resolve funding not being significant when including interactions but being so without them?
 - Do I need to find instruments for the interaction variables?
 - Do I need to provide a model for interaction terms?
    - What about in a production function estimate?
    - (instruments can only control for time-varying endogeneity)
- Three-level panels/fixed-effects
  - Campus within a district over time
- What is hierarchical modelling and should I use it?
   - Are there tests for which level to cluster at?
   - Could use Mundlak's test?
- Which time-invariant effects are likely to be correlated over time?
- ECMs
   - For within-cluster variation
   - Which kind of assumptions about dependence and distribution seem reasonable?
   - Dynamic models
- Standard errors for DiD
   - Bertrand et al '04
   - Are the assumptions going to hold?
- Anticipation effects?
- EHW vs LZ standard errors?
- Regularity conditions?
- Lag model vs. differencing
- Woolridge test for serial correlation?
  - Breusch-Pagan or LM tests for heteroskedasticity?
     - Can heteroskedasticity be dealt with by using logs?
- Between estimator?
- Could I estimate a limited dependent variable model?
  - Quasi-linear MLE
  - All usual NLLS exhibits heteroskedasticity
     - Poisson for large-valued count data?
- Test for unit roots
  - Dickey-Fuller
- How to test for cointegration in the presence of multiple regressors?
- Leads and lags estimators
- How to model funding?
- Deal with 'proportionality' of gains (easier for worse performing schools to do better)
- How to include spatial correlation?
- How to model parameter heterogeneity
- Do I need to account for time-effects with such a short panel?


## Puzzles

- Why is district revenue per pupil so much lower than expenditure?
- Why do wealth transfers have an insignificant coefficient in funding?
