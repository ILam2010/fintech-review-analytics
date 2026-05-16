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
