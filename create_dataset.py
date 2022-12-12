# %%
import pandas as pd

from functions import *

news = pd.read_csv("data/BBC News Train.csv")
news, category = extract_categories(news)
news, keywords = extract_keywords(news)
news = create_short_long(news)
sample = make_sample(news)
