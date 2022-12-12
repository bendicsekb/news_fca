# %%
import pandas as pd

import functions
import importlib
importlib.reload(functions)
from functions import *

#["Text"].apply(lambda e: len(e)).describe()
news = pd.read_csv("data/BBC News Train.csv")
news
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
news = pd.read_csv("data/BBC News Train.csv")
news, category = extract_categories(news)
news = create_short_long(news)
news = create_specific_general(news)
sample = make_sample(news)

# %%
sample
# %%
sample = news.groupby("Category").apply(lambda e: e.sample(30, random_state=42)).reset_index(drop=True)
sample
# %%

sample = make_sample(news)
sample
# %%
sample
# %%
news = pd.read_csv("data/BBC News Train.csv")
categories = news["Category"].unique()
category = type("Category", (), dict(zip(categories, range(len(categories)))))

# %%

categories = [c.capitalize() for c in categories]
categories
# %%
for c in categories:
    news[c] = news["Category"].apply(lambda e: str(e).lower() == str(c).lower())

# %%
news[categories] = pd.DataFrame(news["Category"].apply(lambda e: {c: e == c for c in categories}))
news
# %%
news["Category"].apply(lambda e: {c: e == c for c in categories})

# %%
news
# %%
news, CATEGORY = extract_categories(news)
# %%
news
# %%
news = pd.read_csv("data/BBC News Train.csv")
news, CATEGORY = extract_categories(news)
news = create_short_long(news)
news = create_specific_general(news)
news = remove_unnecessary_columns(news)
sample = make_sample(news)
