# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

exop=pd.read_csv('PS_2023.10.31_06.12.26.csv', sep=',', skiprows=96)
exop.head()

exop.columns
plt.scatter(exop['st_mass'],exop['sy_pnum'])
plt.title("nombre de planètes en fonction de la masse de l'étoile")
plt.ylabel(f' x Msolaire')

# +

by_disc=exop.groupby(exop['discoverymethod'])
by_disc.size()
va=[]
for (group,subdf) in by_disc:
    
    
    va.append(subdf.size)
la=[None]*11
la[9]='Transit'
la[8]='vitesse radiale'
la[4]='micro lentilles'
la[1]='autres'
plt.title("répartition des méthodes de découverte",)
plt.pie(va, labels=la,labeldistance=2)
exop.columns

# +
by_discf=exop.groupby(exop['disc_facility'])
by_discf.size()
va=[]
la=[]
for (group,subdf) in by_discf:
    
    la.append(group)
    va.append(subdf.size)

plt.title("répartition des lieux de découverte",)
plt.pie(va, labels=la,labeldistance=2)
# -

exop.columns
plt.title("rayon maximal en fonction de l'année de découverte")
by_year=exop.groupby(exop['disc_year'])
x=[]
y=[]
for (group,subdf) in by_year:
    x.append(group)
    y.append(subdf['pl_orbsmax'].mean())
plt.plot(x,y)


