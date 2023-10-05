#%%
import pandas as pd   # to load and transform data
import numpy as np    # for math/stat calculations

# from url to pandas dataframe
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json" 
cars = pd.read_json(url)


# %%
cars_filtered = cars.query("cyl == 6").filter(["car", "hp"])

cars


# %%
cars_sorted = cars_filtered.sort_values(by="hp", ascending=False)
cars_sorted

# %%
cars.replace([999, "n/a", ""], np.nan, inplace=True)

cars

# %%
cars["power_to_wt"] = cars["hp"]/cars["wt"]


# %%
###############################################
# Creates a copy of cars and adds two columns
###############################################
cars.assign(
    power_to_wt_part2 = cars["hp"] / cars.wt,
    silly_column = cars.disp * cars.qsec,
    newest = lambda df: df.newest*100
)


# %%
grouped = cars.groupby("cyl").agg(
    avg_hp = ("hp", np.mean),
    sum_hp = ("wt", np.sum)
).reset_index()

grouped
# %%
