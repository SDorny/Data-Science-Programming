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
