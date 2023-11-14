#%%

import pandas as pd 
import altair as alt
import numpy as np

url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

# Import the data with 'latin1' encoding
data = pd.read_csv(url, encoding='cp1252', skiprows=2, header=None)

columns = pd.read_csv(url, encoding='cp1252', nrows=2, header=None)
# %%
columns.head()

'''
id,
seen_any,
is_fan,
seen_1,
seen_2,
seen_3,
seen_4,
seen_5,
seen_6,



'''