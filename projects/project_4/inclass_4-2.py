#%%
from types import GeneratorType
import pandas as pd
import altair as alt
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# %%
denver = pd.read_csv('https://raw.githubusercontent.com/byuidatascience/data4dwellings/master/data-raw/dwellings_denver/dwellings_denver.csv')
ml_dat = pd.read_csv('https://raw.githubusercontent.com/byuidatascience/data4dwellings/master/data-raw/dwellings_ml/dwellings_ml.csv')

alt.data_transformers.disable_max_rows()
subset_data = ml_dat.sample(n = 4999)

# %%
ml_dat.columns

#%%
x = ml_dat.filter(['finbsmnt', 'basement'])
y= ml_dat.before1980

#%%
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=166,test_size=0.2, shuffle=True)

# create the model
classifier = DecisionTreeClassifier()

classifier.fit(x_train, y_train)

y_predicitons = classifer.predict(x_test)


