import pandas as pd
import random
# Ensure UTF-8 encoding to avoid errors with Unicode characters
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Load the CSV with sentiment results
df = pd.read_csv("reddit_posts_with_sentiment.csv")  # Use your actual file name

# Count total and negative posts
total_posts = len(df)
negative_count = (df["sentiment"] == "negative").sum()

# Set dynamic threshold: 10% of total posts
threshold_percent = 25  # change to 20 for 20%, etc.
threshold = total_posts * (threshold_percent / 100)

# Motivational messages
motivational_quotes = [
    "You’ve got this 💪",
    "Keep going, brighter days are ahead 🌞",
    "Every day is a fresh start 🌱",
    "Believe in your potential 🌟",
    "You are stronger than you think 🛡️",
    "Difficult roads often lead to beautiful destinations 🚀"
]

# Mood check and motivational trigger
print(f"Total posts: {total_posts}")
print(f"Negative posts: {negative_count}")
print(f"Threshold for motivation: {int(threshold)}")

if negative_count > threshold:
    print("\n⚠️ You seem to be reading a lot of sad content.")
    print("💡 Here's something positive for you:")
    print("👉", random.choice(motivational_quotes))
else:
    print("\n✅ You're doing okay. Stay positive! 🌸")
