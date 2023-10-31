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
<<<<<<< HEAD
# Notebook de Thomas

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('PS_2023.10.31_06.12.26.csv',skiprows=96)
df.head()

# %%
df['Rayon (*rayon Terre)'] = df['pl_rade']
df['Masse (*masse Terre)'] = df['pl_bmasse']

plt.plot(df['Rayon (*rayon Terre)'],df['Masse (*masse Terre)'],'o',label = 'données')
plt.xlabel('Rayon (en rayons terrestres)')
plt.ylabel('Masse (en masses terrestres)')
plt.title('Données brutes sur les exoplanètes')

# %%
df['Rayon']=df['pl_rade'][np.logical_and((df['pl_rade']<30) , (df['pl_bmasse'] < 5000))]
df['Masse']=df['pl_bmasse'][np.logical_and((df['pl_rade']<30) , (df['pl_bmasse'] < 5000))]

# %%

plt.plot(df['Masse'],df['Rayon'],'o',label='données')
plt.ylabel('Rayon (en rayons terrestres)')
plt.xlabel('Masse (en masses terrestres)')
plt.xscale('log')

n = df['Masse'].shape[0]
x = np.linspace(0.1,10000,n)
y = np.linspace(1,20,n)
plt.plot(x,y,label = 'Rayon/masse Terrestre')
plt.legend()
plt.title('données restreintes aux faibles rayons et masses, avec comparaison par rapport à la Terre')

# %%
df.columns

# %%
df['Rayon solaire'] = df['st_rad']
df['Masse solaire'] = df['st_mass']
df['ratio de fusion'] = df['st_metratio']

métaux = ['[Fe/H]','[M/H]','[m/H ]','[Me/H]','[Fe/H[']


# %%
for m in métaux :
    df[m] = df['Masse solaire'][df['ratio de fusion'] == m]
    plt.plot(df['Rayon solaire'],df[m],'o',label = m)
plt.legend()
plt.title('Rapport masse-rayon en fonction du ratio de fusion de l étoile')
plt.xlabel('Rayon (en rayon du Soleil)')
plt.ylabel('Masse (en masse du Soleil)')
plt.yscale('log')
plt.xscale('log')

# %%
plt.plot(df['pl_eqt'],df['Rayon (*rayon Terre)'],'o',label='données')
plt.ylabel('Rayon (en rayons terrestres)')
plt.xlabel('température équilibre')
plt.yscale('log')

plt.title('Rayon de la planète en fonction de sa température équilibre')

# %%
plt.plot(df['Rayon solaire'],df['st_teff'],'o',label='données')
plt.ylabel('température effective')
plt.xlabel('rayon étoile')
plt.xscale('logit')
plt.yscale('log')

plt.title('Température étoile fonction du rayon')

# %%
plt.plot(df['Masse solaire'],df['st_teff'],'o',label='données')
plt.ylabel('température effective')
plt.xlabel('Masse solaire')
plt.yscale('log')

plt.title('Température étoile fonction de sa masse (en Soleils)')
=======
# # un notebook vierge
#
# sauvé en Python

# %%
def foo():
    print("hello world")
>>>>>>> 3edc6c6792bb44eb268e12bb4499d94ad7990e80
