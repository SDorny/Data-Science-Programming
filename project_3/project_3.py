#%%
import pandas as pd
import sqlite3

con = sqlite3.connect('lahmansbaseballdb.sqlite')

df = pd.read_sql_query('SELECT * FROM fielding LIMIT 5;', con)

df


# %%
con = sqlite3.connect('lahmansbaseballdb.sqlite')
df = pd.read_sql_query('SELECT AB, H FROM batting LIMIT 2;', con)

df

# %%
df = pd.read_sql_query('SELECT * FROM Schools WHERE city == "Rexburg";', con)

df
# %%
#########################
# QUESTION 1
# schoolID = idbyuid
# name_full = Brigham Young University-Idaho
#########################
df = pd.read_sql_query(
    'SELECT playerID, schoolID, yearID FROM CollegePlaying WHERE schoolID == "idbyuid";', con)

df

# %%
df = pd.read_sql_query(
    'SELECT playerID, schoolID, yearID, salary, teamID FROM CollegePlaying LEFTJOIN Salaries ON playerID WHERE schoolID == "idbyuid";', con)

df
# %%
