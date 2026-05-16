import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/bank_reviews_raw.csv")

print("Original shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna(subset=['review', 'rating'])

# Remove empty reviews
df = df[df['review'].str.strip() != ""]

# Normalize dates
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

print("Cleaned shape:", df.shape)

# Save cleaned data
df.to_csv("data/raw/bank_reviews_cleaned.csv", index=False)

print("Cleaned dataset saved.")