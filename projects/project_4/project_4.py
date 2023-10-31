#%%
import pandas as pd
import altair as alt
import numpy as np
import seaborn as sns

# %%
denver = pd.read_csv('https://raw.githubusercontent.com/byuidatascience/data4dwellings/master/data-raw/dwellings_denver/dwellings_denver.csv')
ml_dat = pd.read_csv('https://raw.githubusercontent.com/byuidatascience/data4dwellings/master/data-raw/dwellings_ml/dwellings_ml.csv')

# %%
print(denver.shape)
print(ml_dat.shape)

# %%
print(ml_dat.columns)

# %%
alt.Chart(data= denver).mark_point().encode(
    x = alt.X('yrbuilt'),
    y = 'livearea'
)