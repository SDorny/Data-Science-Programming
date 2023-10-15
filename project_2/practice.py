#%%
##########################################
# Import Libraries and JSON
##########################################
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

data = pd.read_json("https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json")


# %%
##########################################
# Look at the data and get our bearings
##########################################
data.head()

# %%
##########################################
# QUESTION 1
# Which airport has the worst delays?
# SAN FRANCISCO
##########################################

worst_airport = data.groupby('airport_name')[['num_of_flights_total', 'num_of_delays_total', 'minutes_delayed_total']].sum()

worst_airport

#%%

# Creating our new column
worst_airport['proportion_delays'] = worst_airport['num_of_delays_total']/worst_airport['num_of_flights_total']

# Average delay time 
worst_airport['avg_delayed_time_hrs'] = worst_airport['minutes_delayed_total']/60

worst_airport

#%%
# Assuming worst_airport is your DataFrame
worst_airport = worst_airport.sort_values('proportion_delays', ascending=False)

# Convert 'proportion_delays' to a percentage
worst_airport['proportion_delays'] = worst_airport['proportion_delays'].apply(lambda x: '{:.2%}'.format(x))

# Convert 'avg_delayed_time_hrs' to a whole number
worst_airport['avg_delayed_time_hrs'] = worst_airport['avg_delayed_time_hrs'].astype(int)

worst_airport

#%%
##########################################
# QUESTION 2
# Best month to fly?
# SAN FRANCISCO
##########################################













# %%
##########################################
# Replace 'n/a' values with NaN
##########################################
data = data.replace('n/a', np.nan)

# Check locations of NaN values
data.isna().sum()

















# %%
####################################################
# Remove any rows that have missing Month data
####################################################
monthdata = data[data['month'].notna()]

# Make sure that worked
monthdata.isna().sum()


# %%
##########################################
# 
##########################################
