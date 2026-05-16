import pandas as pd
from transformers import pipeline

# Load cleaned dataset
df = pd.read_csv("data/raw/bank_reviews_cleaned.csv")

print("Dataset loaded:", df.shape)

# Load sentiment model
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

labels = []
scores = []

# Run sentiment analysis
for text in df["review"].astype(str):
    result = classifier(text[:512])[0]  # truncate long reviews

    labels.append(result["label"])
    scores.append(result["score"])

# Add results to dataframe
df["sentiment_label"] = labels
df["sentiment_score"] = scores

# Save new dataset
df.to_csv("data/raw/reviews_with_sentiment.csv", index=False)

print("Sentiment analysis completed!")