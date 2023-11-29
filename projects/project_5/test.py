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



#%%
####################################################################################
# STEP 2
####################################################################################
"""QUESTION 2 a)"""
have_seen_star_wars = df[df['seen_any'] == 'Yes']
have_seen_star_wars

# %%
have_seen_star_wars

# %%
"""QUESTION 2 b)"""
have_seen_star_wars['age'].unique()

def convert_age_range_to_number(age_range):
    if age_range == '18-29':
        return 1
    elif age_range == '30-44':
        return 2
    elif age_range == '45-60':
        return 3
    elif age_range == '> 60':
        return 4
    else:
        return 0
# %%
have_seen_star_wars['age_number'] = have_seen_star_wars['age'].apply(convert_age_range_to_number)

# %%
have_seen_star_wars.drop('age', axis=1, inplace=True)

# %%
have_seen_star_wars

# %%
data['education'].unique()
# %%
"""QUESTION 2 c)"""
def convert_education_to_number(education):
    if education == 'High school degree':
        return 1
    elif education == 'Bachelor degree':
        return 2
    elif education == 'Some college or Associate degree':
        return 3
    elif education == 'Graduate degree':
        return 4
    elif education == 'Less than high school degree':
        return 5
    else:
        return 0
# %%
have_seen_star_wars['education_number'] = have_seen_star_wars['education'].apply(convert_education_to_number)

# %%
have_seen_star_wars.drop('education', axis=1, inplace=True)

# %%
have_seen_star_wars

# %%
have_seen_star_wars['age_number'].unique()

# %%
have_seen_star_wars['education_number'].unique()

# %%
"""QUESTION 2 d)"""
have_seen_star_wars['household_income'].unique()

# %%
def convert_income_to_number(income):
    if income == '$0 - $24,999':
        return 1
    elif income == '$25,000 - $49,999':
        return 2
    elif income == '$50,000 - $99,999':
        return 3
    elif income == '$100,000 - $149,999':
        return 4
    elif income == '$150,000+':
        return 5
    else:
        return 0

# %%
have_seen_star_wars['household_income_number'] = have_seen_star_wars['household_income'].apply(convert_income_to_number)

# %%
have_seen_star_wars.drop('household_income', axis=1, inplace=True)

# %%
have_seen_star_wars

# %%
have_seen_star_wars['household_income_number'].unique()

# %%
"""QUESTION 2 e)"""
# If the income is 50k or greater then I will consider it as high. Otherwise, low. I am
# representing that in my target as 1s and 0s, respectively.

def create_income_target(income_number):
    return 1 if income_number >= 3 else 0

have_seen_star_wars['y'] = have_seen_star_wars['household_income_number'].apply(create_income_target)

# %%
have_seen_star_wars

# %%
have_seen_star_wars['y'].unique()

# %%
"""QUESTION 2 f)"""
# gender column
def convert_gender_to_number(gender):
    if gender == 'Female':
        return 1
    elif gender == 'Male':
        return 2
    else:
        return 0

# %%
have_seen_star_wars['gender_number'] = have_seen_star_wars['gender'].apply(convert_gender_to_number)

# %%
have_seen_star_wars.drop('gender', axis=1, inplace=True)

# %%
have_seen_star_wars['gender_number'].unique()
# %%
# star_trek_fan column
def convert_star_trek_fan_to_number(fan):
    if fan == 'Yes':
        return 2
    elif fan == 'No':
        return 1
    else:
        return 0

# %%
have_seen_star_wars['star_trek_fan_number'] = have_seen_star_wars['star_trek_fan'].apply(convert_star_trek_fan_to_number)

# %%
have_seen_star_wars.drop('star_trek_fan', axis=1, inplace=True)

# %%
have_seen_star_wars['star_trek_fan_number'].unique()

# %%
# expanded_universe_fan column
def convert_expanded_universe_fan_to_number(fan):
    if fan == 'Yes':
        return 2
    elif fan == 'No':
        return 1
    else:
        return 0

# %%
have_seen_star_wars['expanded_universe_fan_number'] = have_seen_star_wars['expanded_universe_fan'].apply(convert_expanded_universe_fan_to_number)

# %%
have_seen_star_wars.drop('expanded_universe_fan', axis=1, inplace=True)

# %%
have_seen_star_wars['expanded_universe_fan_number'].unique()

# %%
have_seen_star_wars

# %%
# familiar_expanded_universe column
def convert_familiar_expanded_to_number(answer):
    if answer == 'Yes':
        return 2
    elif answer == 'No':
        return 1
    else:
        return 0

# %%
have_seen_star_wars['familiar_expanded_universe_number'] = have_seen_star_wars['familiar_expanded_universe'].apply(convert_familiar_expanded_to_number)

# %%
have_seen_star_wars.drop('familiar_expanded_universe', axis=1, inplace=True)

# %%
have_seen_star_wars['familiar_expanded_universe_number'].unique()

# %%
have_seen_star_wars

# %%
# star_wars_fan column
def convert_star_wars_fan_to_number(fan):
    if fan == 'Yes':
        return 2
    elif fan == 'No':
        return 1
    else:
        return 0

# %%
have_seen_star_wars['star_wars_fan_number'] = have_seen_star_wars['star_wars_fan'].apply(convert_star_wars_fan_to_number)

# %%
have_seen_star_wars.drop('star_wars_fan', axis=1, inplace=True)

# %%
have_seen_star_wars['star_wars_fan_number'].unique()

# %%
have_seen_star_wars

# %%
# seen_star_wars column
def convert_seen_star_wars_to_number(seen):
    if seen == 'Yes':
        return 2
    elif seen == 'No':
        return 1
    else:
        return 0

# %%
have_seen_star_wars['seen_star_wars_number'] = have_seen_star_wars['seen_star_wars'].apply(convert_seen_star_wars_to_number)

# %%
have_seen_star_wars.drop('seen_star_wars', axis=1, inplace=True)

# %%
have_seen_star_wars['star_wars_fan_number'].unique()

# %%
have_seen_star_wars

#%%
####################################################################################
# STEP 3: CHART 1
####################################################################################
# People who have seen all six movies
df1 = df[df['seen_any'] != 'No']
df1 = df1.dropna(subset=['seen_1', 'seen_2', 'seen_3', 'seen_4', 'seen_5', 'seen_6'])


#%%
# Figuring out the counts and percentages
fav1=df1['fav_1'].value_counts()['1']/471
fav2=df1['fav_2'].value_counts()['1']/471
fav3=df1['fav_3'].value_counts()['1']/471
fav4=df1['fav_4'].value_counts()['1']/471
fav5=df1['fav_5'].value_counts()['1']/471
fav6=df1['fav_6'].value_counts()['1']/471

#%%

# Creating the first chseen
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

#%%
####################################################################################
# STEP 3: CHART 2
####################################################################################
# People who have seen all six movies
df2 = df.dropna(subset=['seen_1', 'seen_2', 'seen_3', 'seen_4', 'seen_5', 'seen_6'], how = "all")
pd.get_dummies(df2.filter(['seen_1', 'seen_2', 'seen_3', 'seen_4', 'seen_5', 'seen_6'])).mean()


#%%
# Creating the first chseen
df2c = pd.DataFrame({
    'votes': [0.804988,0.683832,0.658683,0.726946,0.907784,0.883832],
    'movies': ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 
                     'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'],
})

df2c
#%%
# Define your base chart

base = alt.Chart(df2c,
        title=alt.Title(
       "Which 'Star Wars' Movies Have You Seen",
       subtitle="Of 835 respondents who have seen any film",
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

