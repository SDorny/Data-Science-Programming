#%%
import pandas as pd
import sqlite3
import altair as alt
alt.data_transformers.enable("vegafusion")

con = sqlite3.connect('lahmansbaseballdb.sqlite')

# %%
"""Question 1"""
query1 = pd.read_sql_query(
    '''SELECT DISTINCT cp.playerID, cp.schoolID, s.salary, cp.yearID, s.teamID
        FROM CollegePlaying cp
        JOIN Salaries s
        ON s.playerID = cp.playerID
        WHERE cp.playerID = s.playerID AND schoolID = 'idbyuid'
        ORDER BY s.salary DESC;''', 
    con)

query1
######################################################################################################################################################
#%%
"""Question 2a"""
query2 = pd.read_sql_query(
    '''SELECT playerID, 1.0*H / AB AS battingAvg, H AS Hits, AB AS AtBats, yearID
        FROM Batting
        WHERE AB >= 1
        ORDER BY battingAvg DESC
        LIMIT 5;''', 
    con)

query2

# %%
"""Question 2b"""
query2 = pd.read_sql_query(
    '''SELECT playerID, 1.0*H / AB AS battingAvg, H AS Hits, AB AS AtBats, yearID
        FROM Batting
        WHERE AB >= 100
        ORDER BY battingAvg DESC
        LIMIT 5;''', 
    con)

query2
# %%
"""Question 2c"""
query2 = pd.read_sql_query(
    '''SELECT playerID, 1.0*SUM(H) / SUM(AB) AS battingAvg, H AS Hits, AB AS AtBats
        FROM Batting
        GROUP BY playerID
        HAVING SUM(AB) >= 100
        ORDER BY battingAvg DESC
        LIMIT 5;''', 
    con)

query2
######################################################################################################################################################
# %%,
"""Question 3"""
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

#################################################################################################
#%%
"""Teams Table"""
team = pd.read_sql_query(
    'SELECT * FROM Teams;', con)

team
#%%
"""Batting Table"""
batting = pd.read_sql_query(
    '''SELECT AB
    FROM Batting
    WHERE H > 0;''', con)

batting
#%%
"""Salaries Table"""
salaries = pd.read_sql_query(
    'SELECT * FROM Salaries;', con)

salaries
#%%
"""College Playing Table"""
college = pd.read_sql_query(
    'SELECT * FROM CollegePlaying;', con)

college
