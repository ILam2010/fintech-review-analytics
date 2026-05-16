from google_play_scraper import reviews, Sort
import pandas as pd
from tqdm import tqdm

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in apps.items():
    print(f"Scraping {bank} reviews...")

    result, _ = reviews(
        app_id,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=500
    )

    for r in tqdm(result):
        all_reviews.append({
            "review": r['content'],
            "rating": r['score'],
            "date": r['at'].strftime('%Y-%m-%d'),
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)

print(df.head())

df.to_csv("data/raw/bank_reviews_raw.csv", index=False)

print(f"Saved {len(df)} reviews")