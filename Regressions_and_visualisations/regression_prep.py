import pandas as pd
import numpy as np
from numpy import mean

panel = pd.read_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel.csv')

try:
    panel['schools'] = panel['schools'].str[2:-2].str.split("', '")
    panel['Distance_min'] = panel['Distance_min'].str[2:-2].str.split("', '")
    panel['Distance_miles'] = panel['Distance_miles'].str[2:-2].str.split("', '")
except AttributeError:
    print('n/a')

a = panel['Distance_min'].values
b = panel['Distance_miles'].values
c = []
d = []

for i in a:
    c.append([float(j) for j in i if (j!='error')&(j!='')])

for i in b:
    d.append([float(j) for j in i if (j!='error')&(j!='')])

panel['Distance_min_clean'] = c
panel['Distance_miles_clean'] = d

a = panel['Distance_min_clean'].values
b = panel['Distance_miles_clean'].values
c = []
d = []
e = []
f = []
g = []
h = []

for i in a:
    try:
        c.append(min(i))
        d.append(len([j for j in i if j<10]))
        e.append(mean(i))
    except ValueError:
        c.append(0)
        d.append(0)
        e.append(0)

for i in b:
    try:
        f.append(min(i))
        g.append(len([j for j in i if j<5]))
        h.append(mean(i))
    except ValueError:
        f.append(0)
        g.append(0)
        h.append(0)


panel['Distance_min_minimum'] = c
panel['Distance_min_10r'] = d
panel['Distance_min_avg'] = e
panel['Distance_miles_minimum'] = f
panel['Distance_miles_5r'] = g
panel['Distance_miles_avg'] = h

panel.to_csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/new_balanced_panel4.csv')







#
