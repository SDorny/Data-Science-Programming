#%%
import pandas as pd
import sqlite3
import altair as alt
alt.data_transformers.enable("vegafusion")

con = sqlite3.connect('lahmansbaseballdb.sqlite')

# %%
#########################
# QUESTION 1
# schoolID = idbyuid
# name_full = Brigham Young University-Idaho
#########################
query1 = pd.read_sql_query(
    '''SELECT CollegePlaying.playerID, CollegePlaying.schoolID, Salaries.salary, CollegePlaying.yearID, Salaries.teamID
    FROM CollegePlaying
    JOIN Salaries
    ON Salaries.playerID = CollegePlaying.playerID
    WHERE CollegePlaying.schoolID = 'idbyuid'
    ORDER BY Salaries.salary DESC;''', 
    con)

query1
#%%
###########################
# Salaries Table
###########################
salaries = pd.read_sql_query(
    'SELECT * FROM Salaries;', con)

salaries
#%%
###########################
# CollegePlaying Table
###########################
college = pd.read_sql_query(
    'SELECT * FROM CollegePlaying;', con)

college

######################################################################################################################################################
#%%
#########################
# QUESTION 2A
# Probably need to clean data
#########################
query2 = pd.read_sql_query(
    '''SELECT Salaries.playerID, CAST((Batting.H/Batting.AB) AS FLOAT) AS battingAvg, Salaries.yearID
    FROM Batting
    JOIN Salaries
    ON Salaries.playerID = Batting.playerID
    WHERE Batting.AB > 0 AND Salaries.yearID = 2001
    ORDER BY battingAvg DESC
    LIMIT 5;''', 
    con)

query2


#%%
###########################
# CollegePlaying Table
###########################
batting = pd.read_sql_query(
    '''SELECT AB
    FROM Batting
    WHERE H > 0;''', con)

batting
# %%
#########################
# QUESTION 2B
# Probably need to clean data
#########################
query2 = pd.read_sql_query(
    '''SELECT Salaries.playerID, CAST((Batting.H/Batting.AB) AS FLOAT) AS battingAvg, Salaries.yearID
    FROM Batting
    JOIN Salaries
    ON Salaries.playerID = Batting.playerID
    WHERE Batting.AB > 10 AND Salaries.yearID = 2001
    ORDER BY battingAvg DESC
    LIMIT 5;''', 
    con)

query2
# %%
#########################
# QUESTION 2C
# Probably need to clean data
#########################
query2 = pd.read_sql_query(
    '''SELECT 
    FROM Batting
    JOIN Salaries
    ON Salaries.playerID = Batting.playerID
    WHERE Batting.AB > 10 AND Salaries.yearID = 2001
    ORDER BY battingAvg DESC
    LIMIT 5;''', 
    con)

query2

#%%
###########################
# Teams Table
###########################
team = pd.read_sql_query(
    'SELECT * FROM Teams;', con)

team
######################################################################################################################################################

# %%,
#########################
# QUESTION 3
# Tampa Bay Rays
#########################
query3 = pd.read_sql_query(
    '''SELECT teamID, name, HR, yearID
    FROM Teams
    WHERE (yearID > '2000' AND name == 'Baltimore Orioles') OR (yearID > '2000' AND name == 'Boston Red Sox');''', 
    con)

query3

#%%

source = query3

alt.Chart(source).mark_line().encode(
    x='yearID:T',
    y='HR:Q',
    color='name:N',
)

# %%
