#%%
# load packages
import pandas as pd
import altair as alt
import numpy as np
alt.data_transformers.enable("vegafusion")

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
chart = alt.Chart(sarah_over_time).mark_area(
    line={'color':'darkgreen'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0),
               alt.GradientStop(color='darkgreen', offset=1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0
    )
).encode(
    alt.X('year'),
    alt.Y('Total')
)


chart

# %%
brit_over_time = (names
                 .filter(['name', 'year', 'Total'])
                 .query('name == "Brittany"'))

brit_over_time


# %%
chart = alt.Chart(brit_over_time).mark_area(
    line={'color':'darkgreen'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0),
               alt.GradientStop(color='darkgreen', offset=1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0
    )
).encode(
    alt.X('year'),
    alt.Y('Total')
)

chart

# %%
filterd_names = (names
                 .filter(['name', 'year', 'Total'])
                 .query('name == "Paul" or name == "Peter" or name == "Martha" or name == "Mary"')
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
leia_over_time = (names
                 .filter(['name', 'year', 'Total'])
                 .query('name == "Leia"'))
count = leia_over_time['Total'].sum()

leia_over_time
# %%
chart = alt.Chart(leia_over_time).mark_line().encode(
    x='year',
    y='Total',
    color='name',
)
chart
# %%
