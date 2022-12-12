from pandas import DataFrame
def make_sample(df: DataFrame, n=30, random_state=42):
    """Make a sample of n elements from each category in the dataset"""
    return df.groupby("Category").apply(lambda e: e.sample(n, random_state=random_state)).reset_index(drop=True)

def create_short_long(df: DataFrame):
    """Create a new column 'short' where the value is True if the text is shorter than the median length of the text"""
    median_length = df["Text"].apply(lambda e: len(e)).median()
    df["Short"] = df["Text"].apply(lambda e: len(e) < median_length)
    df["Long"] = df["Short"].__neg__()
    return df

def extract_categories(df: DataFrame):
    """Create an enum with the categories in the dataset, with categories as object attributes"""
    categories: str = df["Category"].unique()
    categories = [c.capitalize() for c in categories]
    category = type("Category", (), dict(zip(categories, range(len(categories)))))
    for c in categories:
        df[c] = df["Category"].apply(lambda e: str(e).lower() == str(c).lower())
    return df, category

def create_specific_general(df: DataFrame):
    """Create a new column 'specific' where the value is True if the category is specific"""
    df["Specific"] = [True] * len(df)
    df["General"] = df["Specific"].__neg__()
    return df

def remove_unnecessary_columns(df: DataFrame):
    """Remove the columns that are not necessary for formal concept analysis"""
    return df.drop(columns=["Category", "Text"])