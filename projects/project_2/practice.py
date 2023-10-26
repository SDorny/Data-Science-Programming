#%%
##########################################
# Import Libraries and JSON
##########################################
import pandas as pd
import altair as alt
import numpy as np
import json 

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

data = pd.read_json("https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json")


# %%
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

##########################################
# Replace 'n/a' values with NaN
##########################################
data = data.replace('n/a', np.nan)

# Check locations of NaN values
data.isna().sum()


####################################################
# Remove any rows that have missing Month data
####################################################
monthdata = data[data['month'].notna()]

# Make sure that worked
monthdata.isna().sum()




#%%
# Create another group by, this time by month
best_month = data.groupby('month')[['num_of_flights_total', 'num_of_delays_total']].sum()

best_month

#%%
# Creating our new column
best_month['proportion_delays'] = best_month['num_of_delays_total']/best_month['num_of_flights_total']

# Assuming worst_airport is your DataFrame
best_month = best_month.sort_values('proportion_delays', ascending=False)

# Convert 'proportion_delays' to a percentage
best_month['proportion_delays'] = best_month['proportion_delays'].apply(lambda x: '{:.2%}'.format(x))

best_month



#%%
##########################################
# QUESTION 
# Weather
# 
##########################################

data = data.replace(-999, np.nan)
data = data.replace(+1500, 1500)

# Replace missing values in 'Late-Arriving' column with the mean
data['num_of_delays_late_aircraft'] = data['num_of_delays_late_aircraft'].fillna(data['num_of_delays_late_aircraft'].mean())

# # Create a new column 'total_weather_delays'
# data['total_weather_delays'] = data.apply(
#     lambda row: row['num_of_delays_weather'] + 0.3*row['Late-Arriving'] + row['num_of_delays_nas']*np.where(
#         row['month'].isin(['April', 'May', 'June', 'July', 'August']), 0.4, 0.65), axis=1)

data['num_weather_delays_late_aircraft'] = (data.apply(lambda row: 0.4 * row['num_of_delays_late_aircraft'] if row['month'] in ['April', 'May', 'June', 'July', 'August'] else 0.65 * row['num_of_delays_late_aircraft'], axis=1)).astype(int)
data['num_weather_delays_nas'] = (data['num_of_delays_nas']*.3).astype(int)
data['total_flights_delayed_by_weather'] = data['num_weather_delays_late_aircraft'] + data['num_weather_delays_nas'] + data['num_of_delays_weather']

data['total_flights_delayed_by_weather'] = data['total_flights_delayed_by_weather'].astype(int)
data.head()


# # Creating our new column
# worst_airport['proportion_delays'] = worst_airport['num_of_delays_total']/worst_airport['num_of_flights_total']

# %%

data['proportion_delayed_weather'] = (data['total_flights_delayed_by_weather']/data['num_of_flights_total'])

# data['proportion_delayed_weather'] = data['proportion_delayed_weather'].apply(lambda x: '{:.0%}'.format(x))


data.head()

#%%
delays = data.groupby('airport_code')[['proportion_delayed_weather']].sum()
delays

# %%

# Assuming 'df' is your DataFrame
df = pd.DataFrame({
    'proportion_delayed_weather': [8.196491, 8.184684, 8.293364, 10.182066, 7.900256, 11.168835, 6.219897],
    'airport_code': ['ATL', 'DEN', 'IAD', 'ORD', 'SAN', 'SFO', 'SLC'],
})

# Create a bar chart
chart = alt.Chart(df).mark_bar().encode(
    y='proportion_delayed_weather',
    x='airport_code'
)

chart


chart
# %%
row_with_nan = data[data.isna().any(axis=1)].iloc[0]

nan_example_record = row_with_nan.to_dict()

print(json.dumps(nan_example_record, indent=4))
# %%
