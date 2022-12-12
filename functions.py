def make_sample(df, n=30, random_state=42):
    return df.groupby("Category").apply(lambda e: e.sample(n, random_state=random_state))

def create_short_long(df):
    median_length = df["Text"].apply(lambda e: len(e)).median()
    df["Short"] = df["Text"].apply(lambda e: len(e) < median_length)
    df["Long"] = df["Short"].__neg__()
    return df

def extract_categories(df):
    categories = df["Category"].unique()
    category = type("Category", (), dict(zip(categories, range(len(categories)))))
    df["Category"] = df["Category"].apply(lambda e: category.__dict__[e])
    return df, category

def extract_keywords(df):
    return df, []