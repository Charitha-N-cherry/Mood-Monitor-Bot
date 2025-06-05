import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the CSV you created earlier
df = pd.read_csv("reddit_posts.csv")

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()
def get_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

# Combine title + selftext for better analysis
df["full_text"] = df["title"].fillna('') + " " + df["selftext"].fillna('')

# Apply sentiment analysis
df["sentiment"] = df["full_text"].apply(get_sentiment)

df.to_csv("reddit_posts_with_sentiment.csv", index=False)
print(" Done! Sentiment analysis complete and saved.")

#counting the number of negatives,positives,neutrals
print(df["sentiment"].value_counts())

