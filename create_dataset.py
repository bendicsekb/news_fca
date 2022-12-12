# %%
import pandas as pd

from functions import *

news = pd.read_csv("data/BBC News Train.csv")
news, category = extract_categories(news)
news = create_short_long(news)
news = create_specific_general(news)
sample = make_sample(news)
sample = remove_unnecessary_columns(sample)
sample.set_index("ArticleId", inplace=True)
write_cxt(sample, "data/bbc.cxt")