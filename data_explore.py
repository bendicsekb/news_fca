# %%
import pandas as pd

#["Text"].apply(lambda e: len(e)).describe()
pd.read_csv("data/BBC News Train.csv")
# %%

news = pd.read_csv("data/BBC News Train.csv")

# create an enum with the categories in the dataset, with categories as object attributes
categories = news["Category"].unique()
category = type("Category", (), dict(zip(categories, range(len(categories)))))
news["Category"] = news["Category"].apply(lambda e: category.__dict__[e])

# %% 
# create a new column 'short' where the valueis True if the text is shorter than the median length of the text
median_length = news["Text"].apply(lambda e: len(e)).median()
news["Short"] = news["Text"].apply(lambda e: len(e) < median_length)
news["Long"] = news["Short"].__neg__()


# %%
# keep a sample of 30 of the dataset from each category
sample = news.groupby("Category").apply(lambda e: e.sample(30, random_state=42))


# %%
print(sample['Short'].value_counts())
print(sample['Category'].value_counts())
sample.describe()
# %%
