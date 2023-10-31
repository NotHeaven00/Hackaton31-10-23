import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

planetes=pd.read_csv('PS_2023.10.31_06.12.26.csv',skiprows=96)
planetes.drop_duplicates(inplace=True)

planetes_groups = planetes.groupby(by='disc_year')

X=planetes_groups.size().keys()

Y=planetes_groups.size()
Ylisse=Y.rolling(window=3,center=True).mean()

plt.plot(X,Y.values,color='green')
plt.xlabel('Année')
plt.ylabel('Nombre de découvertes')

plt.plot(X,Ylisse.values,color='red')
plt.xlabel('Année')
plt.ylabel('Nombre de découvertes (courbe lissée)')

planetes_groups2=planetes.groupby(by='disc_facility')

labels=planetes_groups2.size().keys()
données=planetes_groups2.size().values
plt.pie(données,labels=labels)
