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
sarah_over_time = (names
                 .filter(['name', 'year', 'Total'])
                 .query('name == "Sarah"'))
count = sarah_over_time['Total'].sum()

sarah_over_time



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
