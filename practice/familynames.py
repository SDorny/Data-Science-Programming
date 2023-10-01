#%%
# load packages
import pandas as pd
import altair as alt
import numpy as np
alt.data_transformers.enable("vegafusion")

#%%
# load data
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(url)

# %%
names


# %%
filterd_names = (names
                 .filter(['name', 'year', 'Total'])
                 .query('name == "Sarah" or name == "Rebecca" or name == "Deborah" or name == "Anna" or name == "Bethany"')
                 )

filterd_names


# %%
chart = alt.Chart(filterd_names).mark_line().encode(
    x='year',
    y='Total',
    color='name',
)

chart
# %%
parent_names = (names
                 .filter(['name', 'year', 'Total'])
                 .query('name == "Janet" or name == "Jared"')
                 )

pchart = alt.Chart(parent_names).mark_line().encode(
    x='year',
    y='Total',
    color='name',
    )

pchart
# %%

final = pchart + chart
final
# %%
