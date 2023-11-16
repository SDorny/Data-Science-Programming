#%%

import pandas as pd 
import altair as alt
import numpy as np

url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

# Import the data with 'latin1' encoding
data = pd.read_csv(url, encoding='cp1252')

columns = pd.read_csv(url, encoding='cp1252', nrows=2, header=None)
# %%
data.head()

#%%

# Assuming df is your DataFrame and 'oldName' is the name of the column you want to change
clean_data= data.rename(columns={'Have you seen any of the 6 films in the Star Wars franchise?': 'seen_any',
                                 'Gender':'gender'
                                 })


#%%
seen_it = (clean_data
            .filter(['seen_any', 'gender']))

#male_seen_it = seen_it.query('gender'=='Male')
male = seen_it[seen_it['gender'] != 'Female']

male.dropna()



#%%
seen_it = clean_data['seen_any'].value_counts()['Yes']
havent_seen = clean_data['seen_any'].value_counts()['No']
total_counts= seen_it+havent_seen
total_counts

#%%
percent_seen_it=seen_it/total_counts
percent_seen_it

###########################################################################
#%%

m_seen_it = male['seen_any'].value_counts()['Yes']
m_havent_seen = male['seen_any'].value_counts()['No']
m_total_counts= m_seen_it+m_havent_seen
m_total_counts

#%%
m_percent_seen_it=m_seen_it/m_total_counts
m_percent_seen_it







#%%
total = clean_data['seen_any'].value_counts()
total

#%%

# %%
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
