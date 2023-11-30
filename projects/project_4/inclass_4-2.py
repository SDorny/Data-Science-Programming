#%%
import pandas as pd
import altair as alt
alt.data_transformers.enable("vegafusion")

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

# %%
denver = pd.read_csv('https://raw.githubusercontent.com/byuidatascience/data4dwellings/master/data-raw/dwellings_denver/dwellings_denver.csv')
ml_dat = pd.read_csv('https://raw.githubusercontent.com/byuidatascience/data4dwellings/master/data-raw/dwellings_ml/dwellings_ml.csv')

alt.data_transformers.disable_max_rows()
denver_sample = denver.sample(n=100)
subset_data = ml_dat.sample(n = 100)

#########################################################################
## Build 2 Charts that Evaluate Potentail Relationships
##########################################################################
sample_chart = subset_data
#%%

sample_chart.columns

#%%
source = sample_chart

alt.Chart(source).mark_circle(size=60).encode(
    alt.X('yrbuilt', axis=alt.Axis(format='d')).scale(domain=(1950, 2015)).title('Year Built'),
    alt.Y('numbaths').title('# of Baths'),
    color='before1980:N',
).interactive()

#%%
source = sample_chart

alt.Chart(source).mark_circle(size=60).encode(
    alt.X('yrbuilt', axis=alt.Axis(format='d')).scale(domain=(1950, 2015)).title('Year Built'),
    alt.Y('stories').title('# of Floors'),
    color='before1980:N'
).interactive()

#%%
x = ml_dat.filter(['livearea', 'finbsmnt', 'basement', 'nocars', 
                   'numbdrm', 'numbaths', 'gartype_Att/Det', 
       'gartype_Det', 'arcstyle_CONVERSIONS', 'arcstyle_END UNIT',
       'arcstyle_MIDDLE UNIT', 'arcstyle_ONE AND HALF-STORY',
       'arcstyle_TRI-LEVEL', 'arcstyle_TRI-LEVEL WITH BASEMENT',
       'arcstyle_TWO AND HALF-STORY', 'arcstyle_TWO-STORY'])

y= ml_dat.before1980

#%%
#########################################################################
## Build a Classification Model
##########################################################################
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=166,test_size=0.2)

# create the model
classifier = RandomForestClassifier()

classifier.fit(X_train, y_train)

y_predicitons = classifier.predict(X_test)

metrics.accuracy_score(y_test, y_predicitons)


#%%
#########################################################################
## Justify Your Classification Model 
##########################################################################

importance = classifier.feature_importances_
# summarize feature importance
for i,v in enumerate(importance):
 print('Feature: %0d, Score: %.5f' % (i,v))

#%%

source = sample_chart

alt.Chart(source).mark_circle(size=60).encode(
    alt.X('yrbuilt', axis=alt.Axis(format='d')).scale(domain=(1950, 2015)).title('Year Built'),
    alt.Y('livearea').title('Live Area'),
    color='before1980:N',
).interactive()

# %%
####################################
## Quality of your classification
#####################################
print(metrics.classification_report(y_test, y_predicitons))


