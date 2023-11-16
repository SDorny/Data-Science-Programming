#%%
import pandas as pd
import numpy as np


s3 = pd.Series(
    [
        "this is a regular sentence",
        "https://docs.python.org/3/tutorial/index.html",
        np.nan
    ]
)

s3.str.split('/')[1][2]


# %%
url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

starwars_data = pd.read_csv(url, encoding = "ISO-8859-1", skiprows = 2, header = None)
starwars_cols = pd.read_csv(url, encoding = "ISO-8859-1", nrows = 2, header = None)

starwars_cols.iloc[0,].unique()  


#%%

starwars_cols.iloc[1,].str.replace("Response","")



# %%
url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

starwars_data = pd.read_csv(url, encoding = "ISO-8859-1", skiprows = 2, header = None)
starwars_cols = pd.read_csv(url, encoding = "ISO-8859-1", nrows = 2, header = None)

url.iloc[1,].unique()          

#%%

starwars_data.head()
