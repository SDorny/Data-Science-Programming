##########################################################################
# Libraries
##########################################################################

import pandas as pd
import sqlite3
import altair as alt
alt.data_transformers.enable("vegafusion")


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

##########################################################################
# Graphs
# Link: https://altair-viz.github.io/user_guide/customization.html
##########################################################################

source = query3                                         # query3 was the table

# If you want to adjust the legend
domain = ['New York Yankees', 'Boston Red Sox']         # Names
range_ = ['#003087', '#BD3039']                         # Colors

alt.Chart(
    source,                                             # Using the table
    title=alt.Title(                                    # Title of Graph
        "The Battle For Homeruns in the Past Decade",   # Subtitle being split
        subtitle=["The two rivals follow a similar pattern,", "yet the Yankees remain on top."]
    )).mark_line().encode(
    alt.X('yearID:T').scale(zero=False).title('Year'),  # Not starting at 0, changing name of axis
    alt.Y('HR:Q').scale(zero=False).title('# of Home Runs'),
    color=alt.Color('name:N').title("Team Name").scale(domain=domain, range=range_),
).configure_axis(                                       # Getting Rid of Gridlines
    grid=False
).configure_view(                                       # Getting rid of borderlines
    stroke=None
)


##########################################################################
# Wrangling
##########################################################################

# Use filter to select specific columns
filtered_df = df.filter(items=['Employee', 'Age'])

# Use Query to filter employees with age > 30 and salary > 70000
filtered_df = df.query('Age > 30 & Salary > 70000')

# Groupby
# Agg Func: Count, Nunique, min, max, sum, mean, etc
grouped = df.groupby('Department')['Salary'].mean()

# Replace
data = data.replace('n/a', np.nan)                      # Replace (that, with this)  

# Add a new column
df['Salary'] = [70000, 80000, 60000, 65000]



# MISSING VALUES
# Replace missing values in 'Late-Arriving' column with the mean
data['num_of_delays_late_aircraft'] = data['num_of_delays_late_aircraft']
.fillna(data['num_of_delays_late_aircraft'].mean())

# Use dropna to remove rows with missing values
df_clean = df.dropna()

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