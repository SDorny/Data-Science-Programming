####################################################################################
# IMPORTING
####################################################################################
#%%
import pandas as pd 
import altair as alt
import numpy as np

url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

# Data only
data = pd.read_csv(url, encoding='cp1252')
# Columns only
columns = pd.read_csv(url, encoding='cp1252', nrows=2, header=None)


####################################################################################
# TRANSFORMING
####################################################################################
#%%
data.head()

#%%
clean_data= data.rename(columns={'Have you seen any of the 6 films in the Star Wars franchise?': 'seen_any',
                                 'Do you consider yourself to be a fan of the Star Wars film franchise?': 'is_fan',
                                 'Which of the following Star Wars films have you seen? Please select all that apply.':'seen_1',
                                 'Unnamed: 4':'seen_2',
                                 'Unnamed: 5':'seen_3',
                                 'Unnamed: 6':'seen_4',
                                 'Unnamed: 7':'seen_5',
                                 'Unnamed: 8':'seen_6',
                                 'Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.':'fav_1',
                                 'Unnamed: 10':'fav_2',
                                 'Unnamed: 11':'fav_3',
                                 'Unnamed: 12':'fav_4',
                                 'Unnamed: 13':'fav_5',
                                 'Unnamed: 14':'fav_6',
                                 'Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.':'know_han',
                                 'Unnamed: 16':'know_luke',
                                 'Unnamed: 17':'know_leia',
                                 'Unnamed: 18':'know_anakin',
                                 'Unnamed: 19':'know_obi',
                                 'Unnamed: 20':'know_palp',
                                 'Unnamed: 21':'know_vader',
                                 'Unnamed: 22':'know_lando',
                                 'Unnamed: 23':'know_fett',
                                 'Unnamed: 24':'know_c3po',
                                 'Unnamed: 25':'know_r2d2',
                                 'Unnamed: 26':'know_jarjar',
                                 'Unnamed: 27':'know_padme',
                                 'Unnamed: 28':'know_yoda',
                                 'Which character shot first?':'shot_first',
                                 'Are you familiar with the Expanded Universe?':'know_eu',
                                 'Do you consider yourself to be a fan of the Expanded Universe?Œæ':'eu_fan',
                                 'Do you consider yourself to be a fan of the Star Trek franchise?':'is_trekie',
                                 'Gender':'gender',
                                 'Age':'age',
                                 'Household Income':'income',
                                 'Education':'latest_degree',
                                 'Location (Census Region)':'region'
                                 })

#%%
clean_data.head()
#%%
df = clean_data.drop(clean_data.index[1])
df.head()



####################################################################################
# FILTERING
####################################################################################
#%%

df = df[df['seen_any'] != 'No']

#unique_values = df['seen_any'].unique()
#print(unique_values)






####################################################################################
# I am done for this week. Need to ask what we should do for age ranges, income ranges 
#
####################################################################################


























# def replace_values(val):
#     if pd.isnull(val):
#         return 'No'
#     elif 'Star Wars' in val:
#         return 'Yes'
#     else:
#         return val

# # Assuming df is your DataFrame
# columns = ['seen_1', 'seen_2', 'seen_3', 'seen_4', 'seen_5', 'seen_6']
# df[columns] = df[columns].map(replace_values)


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
