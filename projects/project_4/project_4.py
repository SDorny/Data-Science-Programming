#%%
import pandas as pd
import altair as alt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split

# %%
denver = pd.read_csv('https://raw.githubusercontent.com/byuidatascience/data4dwellings/master/data-raw/dwellings_denver/dwellings_denver.csv')
ml_dat = pd.read_csv('https://raw.githubusercontent.com/byuidatascience/data4dwellings/master/data-raw/dwellings_ml/dwellings_ml.csv')

# %%

print(ml_dat.shape)

alt.data_transformers.disable_max_rows()

#%%
x = ml_dat['yrbuilt']
y= ml_dat['arcstyle_BI-LEVEL']

#%%

# using the train test split function
X_train, X_test, y_train, y_test = train_test_split(
  x,y , random_state=76,test_size=0.34, shuffle=True)

#%%
print('X_train : ')
print(X_train.head())
print(X_train.shape)
 
 #%%
print('')
print('X_test : ')
print(X_test.head())
print(X_test.shape)
 
 #%%
print('')
print('y_train : ')
print(y_train.head())
print(y_train.shape)
 #%%

print('')
print('y_test : ')
print(y_test.head())
print(y_test.shape)

#%%

y_test_10 = y_test[:10]

# Calculate the average using numpy
average = np.mean(y_test_10)

# Print the result
print("The average of the first 10 values in the testing y values is", round(average, 2))

#%%
x_test_10 = X_test[:10]

# Calculate the average using numpy
average = np.mean(x_test_10)

# Print the result
print("The average of the first 10 values in the testing x values is", round(average, 2))




# %%
print(denver.shape)
print(ml_dat.shape)

# %%
print(ml_dat.columns)

# %%
alt.Chart(data= denver).mark_point().encode(
    x = alt.X('yrbuilt'),
    y = 'livearea'
)




# %%
