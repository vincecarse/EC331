## New Features
 - District expenditure items (teacher pensions?)
 - Create charter subset


## Stuff to fix
- Check all data is actually from the correct/same year
- Use percent expenditures (e.g. for oil and gas) and then multiply that by per pupil to get per pupil oil and gas.

## General to do
- Write scraper and wrangler for adjacent district distances
- Link this to recapture data
- Split districts by 'type'
- Fix 'alignment' of district distance data by rows (2 row lag from 262)
- Create 'info table' for all adjacent districts (tax rates etc)
- Create variables for whether a district is at its revenue threshold
  - Create 'gap' variables, like how difference between two bordering districts' wealth/spending levels changes
  - Also consider comparing 'macro' differences in student/teacher characteristics
- Link district info to distance
  - Requires using 'dist_info_file' and 'big_panel2'
- Could go back to '96/'97 and get info from then too (won't have as good school data though)

## Thoughts
- Main code is called something like 'VAM'
- Look at non-linearities in teacher experience
- District fixed effects
  - Use different specifications
  - Potentially look at IO papers for ideas
- Oil shocks
- Use distances data for each campus better
- Consider robustness checks
