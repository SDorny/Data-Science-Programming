#%%
import pandas as pd
import altair as alt
import numpy as np


#%%
df = pd.DataFrame(
{"a" : [5, 4, 6, 2, 3],
"b" : [7, 8, 9, 10, 11],
"c" : [10, 11, 12, 101, 0]})

df


# %%
df2 = df.rename(columns = {'a':'duck'})

# %%
df2.drop(columns=['c'])

# %%
df2.query('b < 9')

# %%
print(df2['duck'].min())

# %%
# The above code can be re-written to 'method chain'
(df
 .rename(columns = {'a':'duck'})
 .filter(['b', 'duck'])
 .query('b < 9')
 .min()
 )
# %%
