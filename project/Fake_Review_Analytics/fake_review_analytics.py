
import pandas as pd
from textblob import TextBlob

data = pd.read_csv("fake_reviews_dataset.csv")

# Sentiment Analysis
data['sentiment_score'] = data['review_text'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Rule-based Fake Review Detection
def detect_fake(row):
    if row['user_review_count'] > 20 and row['review_text'].count(' ') < 5:
        return "Fake"
    elif row['sentiment_score'] > 0.8 and row['rating'] == 5:
        return "Suspicious"
    else:
        return "Genuine"

data['review_type'] = data.apply(detect_fake, axis=1)

# Save processed file
data.to_csv("processed_reviews.csv", index=False)

print(data[['review_text','rating','review_type']])
