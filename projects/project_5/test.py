####################################################################################
# STEP 1: IMPORTING
####################################################################################
#%%
import pandas as pd 
import altair as alt
import numpy as np
alt.data_transformers.enable("vegafusion")

url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

# Data only
data = pd.read_csv(url, encoding='cp1252')

####################################################################################
# STEP 1: TRANSFORMING
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
df = clean_data.drop(clean_data.index[0])
df.head()



#********************************************************************************************************
#%%

####################################################################################
# STEP 3: CHART 1
####################################################################################
# People who have seen all six movies
df = df[df['seen_any'] != 'No']
df = df.dropna(subset=['seen_1', 'seen_2', 'seen_3', 'seen_4', 'seen_5', 'seen_6'])


#%%
# Figuring out the counts and percentages
fav1=df['fav_1'].value_counts()['1']/471
fav2=df['fav_2'].value_counts()['1']/471
fav3=df['fav_3'].value_counts()['1']/471
fav4=df['fav_4'].value_counts()['1']/471
fav5=df['fav_5'].value_counts()['1']/471
fav6=df['fav_6'].value_counts()['1']/471

#%%

# Creating the first chart
df1 = pd.DataFrame({
    'votes': [fav1,fav2,fav3,fav4,fav5,fav6],
    'movies': ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 
                     'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'],
})

df1
#%%
# Define your base chart

base = alt.Chart(df1,
        title=alt.Title(
       "What's the Best 'Star Wars' Movie?",
       subtitle="Of 471 respondents who have seen all six films",
       anchor='start'
   )).encode(
    alt.X('votes', title='Votes', axis=None),
    alt.Y("movies", sort=df1['movies'].tolist(), axis=alt.Axis(title=None)),
    text=alt.Text('votes', format='.0%')
)

# Define your bar and text charts
bar_chart = base.mark_bar(color='#008ED4')
text_chart = base.mark_text(align='left', dx=2)

# Layer your charts
layered_chart = bar_chart + text_chart

# Set the configuration on the layered chart
configured_chart = layered_chart.configure_axis(
    grid=False
).configure(background='#F1F0F1'
).configure_view(
    stroke=None
)

configured_chart

####################################################################################
# STEP 3: CHART 2
####################################################################################












#%%
# seen_it = clean_data['seen_any'].value_counts()['Yes']
# havent_seen = clean_data['seen_any'].value_counts()['No']

# #%%
# total_counts= seen_it+havent_seen
# total_counts

# #%%
# percent_seen_it=seen_it/total_counts
# percent_seen_it

# ###########################################################################
# #%%

# m_seen_it = male['seen_any'].value_counts()['Yes']
# m_havent_seen = male['seen_any'].value_counts()['No']
# m_total_counts= m_seen_it+m_havent_seen
# m_total_counts

# #%%
# m_percent_seen_it=m_seen_it/m_total_counts
# m_percent_seen_it







# #%%
# total = clean_data['seen_any'].value_counts()
# total

