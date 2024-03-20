#%%
import altair as alt
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics

url="https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
names=pd.read_csv(url)
# %%
