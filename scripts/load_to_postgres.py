import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
    password="Postgres@123"
)

cur = conn.cursor()

# Load dataset
df = pd.read_csv("data/raw/reviews_with_themes.csv")

# Insert banks first
banks = df["bank"].unique()

bank_ids = {}

for bank in banks:
    cur.execute(
        """
        INSERT INTO banks (bank_name, app_name)
        VALUES (%s, %s)
        ON CONFLICT (bank_name) DO NOTHING
        """,
        (bank, bank)
    )

conn.commit()

# Fetch bank IDs
cur.execute("SELECT bank_id, bank_name FROM banks")
rows = cur.fetchall()

for row in rows:
    bank_ids[row[1]] = row[0]

# Insert reviews
for _, row in df.iterrows():

    cur.execute(
        """
        INSERT INTO reviews (
            bank_id,
            review_text,
            rating,
            review_date,
            sentiment_label,
            sentiment_score,
            theme,
            source
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            bank_ids[row["bank"]],
            row["review"],
            int(row["rating"]),
            row["date"],
            row["sentiment_label"],
            float(row["sentiment_score"]),
            row["theme"],
            row["source"]
        )
    )

conn.commit()

print("Data inserted successfully!")

cur.close()
conn.close()