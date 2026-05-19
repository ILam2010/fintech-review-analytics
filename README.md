# Fintech Review Analytics

##  Project Overview

This project analyzes Google Play Store reviews of Ethiopian banking mobile apps to understand customer experience, identify pain points, and extract actionable insights for product improvement.

The analysis focuses on three major banks:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The goal is to transform unstructured user reviews into structured insights using data engineering and NLP techniques.

##  Objectives

- Scrape real user reviews from Google Play Store
- Clean and preprocess review data
- Perform sentiment analysis on customer feedback
- Identify early patterns in user satisfaction and complaints
- Build a reproducible data pipeline

##  Data Collection

- Source: Google Play Store
- Tool used: `google-play-scraper`
- Fields collected:
  - Review text
  - Rating (1–5 stars)
  - Date
  - Bank name
  - Source (Google Play)

### Banks analyzed:
- CBE Mobile Banking
- BOA Mobile Banking
- Dashen Super App

##  Data Preprocessing

The following cleaning steps were applied:
- Removed duplicate reviews
- Dropped missing review texts and ratings
- Normalized date format to YYYY-MM-DD
- Removed empty reviews

Clean dataset saved locally as: data/raw/bank_reviews_cleaned.csv


##  Sentiment Analysis (In Progress)

Sentiment analysis is performed using:
- `distilbert-base-uncased-finetuned-sst-2-english`

Each review is classified as:
- Positive
- Negative

with confidence scores.


##  Early Insights (Preliminary)

Initial observations:
- Transfer speed and app performance are frequently mentioned issues
- Login and OTP failures appear across multiple banks
- Positive feedback is mainly related to UI design and convenience



##  Limitations

- Some apps return limited review counts from Google Play API
- Reviews may be biased toward negative experiences
- Language diversity (some reviews are not in English)

## 📁 Project Structure
fintech-review-analytics/
│
├── data/
│ └── raw/
├── scripts/
├── notebooks/
├── src/
├── tests/
├── requirements.txt
├── README.md

##  Tools & Technologies

- Python
- Google Play Scraper
- Pandas
- Hugging Face Transformers
- Git & GitHub



## 👨Author

Data Engineering Project – Omega Consultancy Simulation



#  Database Engineering (Task 3)

## PostgreSQL Setup

PostgreSQL was used to store the cleaned and processed banking app reviews in a relational database format.

### Database Name

bank_reviews

### Tools Used

* PostgreSQL
* pgAdmin
* psycopg2
* SQL

## Database Schema

Two relational tables were created:

### 1. banks

Stores metadata about the banking applications.

| Column    | Type               | Description             |
| --------- | ------------------ | ----------------------- |
| bank_id   | SERIAL PRIMARY KEY | Unique bank identifier  |
| bank_name | VARCHAR(100)       | Name of the bank        |
| app_name  | VARCHAR(150)       | Mobile application name |



### 2. reviews

Stores cleaned and processed customer reviews.

| Column          | Type               | Description                         |
| --------------- | ------------------ | ----------------------------------- |
| review_id       | SERIAL PRIMARY KEY | Unique review identifier            |
| bank_id         | INTEGER            | Foreign key referencing banks table |
| review_text     | TEXT               | Customer review text                |
| rating          | INTEGER            | Star rating (1–5)                   |
| review_date     | DATE               | Review submission date              |
| sentiment_label | VARCHAR(20)        | Sentiment classification            |
| sentiment_score | FLOAT              | Sentiment confidence score          |
| theme           | VARCHAR(100)       | Extracted review theme              |
| source          | VARCHAR(50)        | Data source                         |



## Data Loading Pipeline

A Python ETL script using `psycopg2` was implemented to:

1. Connect to PostgreSQL
2. Insert bank metadata into the `banks` table
3. Insert processed reviews into the `reviews` table
4. Maintain relational integrity using foreign keys

Main script:
scripts/load_to_postgres.py

## Verification Queries

The following SQL queries were executed to verify data integrity:

### Count reviews per bank

```sql id="r4"
SELECT b.bank_name, COUNT(*) AS total_reviews
FROM reviews r
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY b.bank_name;
```

### Average rating per bank

```sql id="r5"
SELECT b.bank_name, AVG(r.rating) AS average_rating
FROM reviews r
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY b.bank_name;
```

### Null check for review text

```sql id="r6"
SELECT *
FROM reviews
WHERE review_text IS NULL;
```



## Outcome

* Successfully inserted 1,000+ processed reviews into PostgreSQL
* Verified relational integrity between tables
* Confirmed no null values in key review fields

