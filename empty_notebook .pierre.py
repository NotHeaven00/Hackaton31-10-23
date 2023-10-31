# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -rise, -version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
# ---

# %% [markdown]
# # un notebook vierge
#
# sauvé en Python

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
df=pd.read_csv('PS_2023.10.31_06.15.23.csv',sep=',',skiprows=96)
df.head(10)
df.columns


# %%
dfp=df.iloc[:,[11,36]]
dfp.columns=['Orbite','Excentricité']
dfp.head(20)

# %%
dfp=dfp.dropna(axis=0,how='any')
dfp.head(20)

# %%
dfp=dfp[dfp['Orbite']<1000000]

# %%
dfp['intervalle de e'] = pd.cut(dfp['Excentricité'], bins=[-1,0.2,0.4,0.6,0.8,1.1],labels=['0-0,2', '0,2-0,4','0,4-0,6','0,6-0,8','0,8-1'])
dfp.head(20)

# %%
by_e = dfp.groupby(by='intervalle de e')
by_e.Orbite.mean()

# %%
axes=plt.plot(by_e.Orbite.mean())
plt.title('Période orbitale moyenne en fonction de l excentricité')
plt.xlabel('Intervalle excentricité')
plt.ylabel('Période orbitale moyenne')

# %%
ax=plt.scatter(dfp['Excentricité'],dfp['Orbite'])
plt.title('Période orbitale moyenne en fonction de l excentricité')
plt.xlabel('Intervalle excentricité')
plt.ylabel('Période orbitale')

# %%
dfn=df[['discoverymethod', 'disc_year','sy_dist']]
dfn.columns=['Méthode découverte','Année découverte','Distance']
dfn.head(5)
dfn=dfn.dropna(axis=0,how='any')

# %%
dfn.pivot_table(values='Distance',
    index='Année découverte',
    columns='Méthode découverte',)

# %%
#x=dfn['Méthode découverte'].value_counts()
#print(x)
#axes=plt.pie(x,labels=dfn['Méthode découverte'].unique())

# %%
by_a = dfn.groupby(by='Année découverte')
plt.plot(by_a.Distance.mean())
plt.title('Distance moyenne à la Terre des planètes en fonction de leur année de découverte')
plt.xlabel('Année')
plt.ylabel('Distance moyenne à la Terre des planètes découvertes')



# plt.tight_layout()

# %%
by_m = dfn.groupby(by='Méthode découverte')
plt.plot(by_m.Distance.mean())
plt.title('Distance moyenne à la Terre des planètes en fonction de leur méthode de découverte')
plt.xlabel('Méthode découverte')
plt.ylabel('Distance moyenne à la Terre des planètes découvertes')

# %%
