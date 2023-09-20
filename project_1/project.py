#%%
# load packages
import pandas as pd
import altair as alt

#%%
# load data
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(url)

# %%
names
# %%
names['name'].value_counts()

# %%
names.year.min()
names.year.max()

# %%
names.columns
# %%
names.shape
names.head()
names.describe()
