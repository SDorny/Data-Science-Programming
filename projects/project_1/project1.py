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
##########################################
# BASIC TABLE OF THE DATA
##########################################
names


 # %%
##########################################
# QUESTION 1 - QUERY
##########################################


sarah_over_time = (names
                 .filter(['name', 'year', 'Total'])
                 .query('name == "Sarah"'))
count = sarah_over_time['Total'].sum()

sarah_over_time


# %%
##########################################
# QUESTION 1 - CHART
##########################################
# Data for reference line and annotation
ref_data = pd.DataFrame({'year': [1999], 'Total': [sarah_over_time['Total'].max()], 'text': ['My Birth Year']})

# Main chart
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
    x=alt.X('year', axis= alt.Axis(format = 'd'), title='Year'),
    y=alt.Y('Total', title='# of Births')
).properties(title= "The Name 'Sarah' Spikes in Popularity")

# Reference line and text annotation
annotations = alt.Chart(ref_data).mark_rule(color='red').encode(x='year:Q') + \
              alt.Chart(ref_data).mark_text(align='left', baseline='middle', dx=2).encode(
                  x='year:Q',
                  y='Total:Q',
                  text='text'
              )

# Combine chart and annotations
sarah_chart = chart + annotations

sarah_chart


# %%
##########################################
# QUESTION 2 - QUERY
##########################################
brit_over_time = (names
                 .filter(['name', 'year', 'Total'])
                 .query('name == "Brittany"'))

brit_over_time


# %%
##########################################
# QUESTION 2 - CHART
##########################################
chart = alt.Chart(brit_over_time).mark_area(
    line={'color':'blue'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0),
               alt.GradientStop(color='blue', offset=1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0
    )
).encode(
    x=alt.X('year', axis= alt.Axis(format = 'd'), title='Year'),
    y=alt.Y('Total', title='# of Births')
).properties(title= "'Brittany', a Name Belonging to the 80's and 90's Kids")

# Data for reference lines (without text annotations)
ref_data = pd.DataFrame({'year': [1980, 2000]})

# Reference lines
reference_lines = alt.Chart(ref_data).mark_rule(color='orange').encode(x='year:Q')

# Combine chart and reference lines
brit_chart = chart + reference_lines

brit_chart



# %%
##########################################
# QUESTION 3 - QUERY
##########################################
filterd_names = (names
                 .filter(['name', 'year', 'Total'])
                 .query('name == "Paul" or name == "Peter" or name == "Martha" or name == "Mary"')
                 .query('1920 <= year <= 2000')  # Add only the dates we need
                 )


# %%
##########################################
# QUESTION 3 - CHART
##########################################
chart = alt.Chart(filterd_names).mark_line().encode(
    x=alt.X('year', axis= alt.Axis(format = 'd'), title='Year'),
    y=alt.Y('Total', title='# of Births'),
    color=alt.Color('name').title("Names"),
).properties(title= "Huge Decline in Top 4 Gospel Names in the 60's")
chart



# %%
##########################################
# QUESTION 4 - QUERY
##########################################
leia_over_time = (names
                 .filter(['name', 'year', 'Total'])
                 .query('name == "Leia"'))

##########################################
# QUESTION 4 - CHART
##########################################
chart = alt.Chart(leia_over_time).mark_line().encode(
    x=alt.X('year', axis= alt.Axis(format = 'd')),
    y='Total',
    color=alt.Color('name').title("Name"),
)

# Data for annotations and reference lines
annotations_data = pd.DataFrame({
    'year': [1977, 1999, 2015],
    'Total': [120, 120, 50],  # My Annotations location on the y-axis
    'text': ["'A New Hope' comes out", "Prequels come out", "'The Force Awakens' comes out"]
})

# Annotations
annotations = alt.Chart(annotations_data).mark_text(
    align='left',
    baseline='middle',
    dx=1,  # Nudges text to right so it doesn't appear on top of the bar
    dy=-5,  # Nudges text upward so it appears above the bar
    angle=270  # Rotates text 270 degrees
).encode(
    x='year:Q',
    y='Total:Q',  # Use the y values specified in annotations_data
    text='text'
).properties(title= "With Each Star Wars Movie, Leia Becomes a More Popular Name")

# Reference lines
reference_lines = alt.Chart(annotations_data).mark_rule(color='orange').encode(x='year:Q')

# Combine chart, annotations, and reference lines
leia_chart = chart + annotations + reference_lines

leia_chart

# %%
