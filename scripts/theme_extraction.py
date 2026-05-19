import pandas as pd

df = pd.read_csv("data/raw/reviews_with_sentiment.csv")

def classify_theme(text):
    text = str(text).lower()

    if any(word in text for word in ["login", "log in", "sign in"]):
        return "Login Issues"

    elif any(word in text for word in ["otp", "code", "verification"]):
        return "OTP Issues"

    elif any(word in text for word in ["slow", "delay", "transfer"]):
        return "Transaction Performance"

    elif any(word in text for word in ["crash", "freeze", "bug"]):
        return "App Stability"

    elif any(word in text for word in ["ui", "design", "interface"]):
        return "UI/UX"

    else:
        return "Other"

df["theme"] = df["review"].apply(classify_theme)

df.to_csv("data/raw/reviews_with_themes.csv", index=False)

print("Theme extraction completed!")