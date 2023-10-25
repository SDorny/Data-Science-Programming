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
        WHERE AB >= 1 AND yearID = 2010
        ORDER BY battingAvg DESC
        LIMIT 5;''', 
    con)

query2

# %%
"""Question 2b"""
query2 = pd.read_sql_query(
    '''SELECT playerID, 1.0*H / AB AS battingAvg, H AS Hits, AB AS AtBats, yearID
        FROM Batting
        WHERE AB >= 10 AND yearID = 2010
        ORDER BY battingAvg DESC
        LIMIT 5;''', 
    con)

query2
# %%
"""Question 2c"""
query2 = pd.read_sql_query(
    '''SELECT playerID, 1.0*SUM(H) / SUM(AB) AS battingAvg, SUM(H) AS Hits, SUM(AB) AS AtBats
        FROM Batting
        GROUP BY playerID
        HAVING SUM(AB) > 100
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
    WHERE (yearID > '2006' AND name == 'New York Yankees') OR (yearID > '2006' AND name == 'Boston Red Sox');''', 
    con)

query3
#%%
source = query3

domain = ['New York Yankees', 'Boston Red Sox']
range_ = ['#003087', '#BD3039']

alt.Chart(
    source,
    title=alt.Title(
        "The Battle For Homeruns in the Past Decade",
        subtitle=["The two rivals follow a similar pattern,", "yet the Yankees remain on top."]
    )).mark_line().encode(
    alt.X('yearID:T').scale(zero=False).title('Year'),
    alt.Y('HR:Q').scale(zero=False).title('# of Home Runs'),
    color=alt.Color('name:N').title("Team Name").scale(domain=domain, range=range_),
).configure_axis(
    grid=False
).configure_view(
    stroke=None
)

#################################################################################################
#%%
"""Teams Table"""
team = pd.read_sql_query(
    '''SELECT * FROM Teams
    WHERE name = "New York Yankees";''', con)

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
