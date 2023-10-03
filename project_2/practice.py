#%%
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

data = pd.read_csv("https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json")

data

# %%

data.dtypes
# %%
data.info()
# %%
