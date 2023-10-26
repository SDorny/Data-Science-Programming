#%%
# load packages
import pandas as pd
import altair as alt
import numpy as np

#%%
# load data
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(url)

# %%
names

 # %%
olivers_in_UT = (names
                 .filter(['name', 'UT', 'year'])
                 .query('name.str.startswith("Oliver") and UT > 0'))
count = olivers_in_UT['UT'].sum()

count


# %%
(names
 .filter(['name', 'year'])
 .sort_values('year')
 .query('name.str.startswith("Felisha")')
 .head(1)
 )
