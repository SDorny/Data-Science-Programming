#%%
import pandas as pd
import altair as alt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split

# %%
denver = pd.read_csv('https://raw.githubusercontent.com/byuidatascience/data4dwellings/master/data-raw/dwellings_denver/dwellings_denver.csv')
ml_dat = pd.read_csv('https://raw.githubusercontent.com/byuidatascience/data4dwellings/master/data-raw/dwellings_ml/dwellings_ml.csv')

# %%
alt.data_transformers.disable_max_rows()
subset_data = ml_dat.sample(n = 4999)

# %%
subset_data.before1980 = subset_data.before1980.astype('str')

Chart = alt.Chart(subset_data).mark_circle().encode(
    x= alt.X('yrbuilt').axis(title = "Year",format="d").scale(domainMin= 1870),
    y= "totunits",
    color = "before1980"
)
Chart
# %%
