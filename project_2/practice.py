#%%
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

data = pd.read_json("https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json")

# %%
#data.head()
#data.info()


# %%
data.describe()

# %%
data.value_counts()

#%%
data.isna().sum()

# %%
