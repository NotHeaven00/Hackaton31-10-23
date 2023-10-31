import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

planetes=pd.read_csv('PS_2023.10.31_06.12.26.csv',skiprows=96)
planetes.drop_duplicates(inplace=True)

planetes_groups = planetes.groupby(by='disc_year')

planetes_groups.size()

X=planetes_groups.size().keys()

Y=planetes_groups.size().values

plt.plot(X,Y)
plt.xlabel('Année')
plt.ylabel('Nombre de découvertes')
