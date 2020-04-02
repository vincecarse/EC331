## New Features
 - Distance to nearest substitute school (ARCGIS)
     - Could need to use Google Maps API
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
- Link district info to distance

## Thoughts
- Main code is called something like 'VAM'
- Look at non-linearities in teacher experience
- District fixed effects
  - Use different specifications
  - Potentially look at IO papers for ideas
- Oil shocks
- Use distances data for each campus better
- Consider robustness checks
