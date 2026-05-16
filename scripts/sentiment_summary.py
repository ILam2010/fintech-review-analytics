import pandas as pd

df = pd.read_csv("data/raw/reviews_with_sentiment.csv")

print("\nSentiment distribution by bank:\n")
print(df.groupby(["bank", "sentiment_label"]).size())

print("\nAverage sentiment score by bank:\n")
print(df.groupby("bank")["sentiment_score"].mean())