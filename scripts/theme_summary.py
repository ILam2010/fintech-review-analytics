import pandas as pd

df = pd.read_csv("data/raw/reviews_with_themes.csv")

print(df.groupby(["bank", "theme"]).size())