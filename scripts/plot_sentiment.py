import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/reviews_with_sentiment.csv")

plt.figure(figsize=(8,5))

sns.countplot(data=df, x="bank", hue="sentiment_label")

plt.title("Sentiment Distribution Across Banks")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.tight_layout()
plt.show()