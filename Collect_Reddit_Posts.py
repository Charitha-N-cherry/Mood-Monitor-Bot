import praw
import pandas as pd

# Initialize Reddit client
reddit = praw.Reddit(
    client_id="XXX",
    client_secret="YYY",
    user_agent="script:mood-monitor-bot:1.0 (by u/Itchy_Departure2341)"
)



# Subreddits to collect from
subreddits = {
    "r/depression": "sad",
    "r/OffMyChest": "sad",
    "r/GetMotivated": "motivational",
    "r/happy": "motivational"
}

# Collect posts
posts = []

for subreddit_name, label in subreddits.items():
    subreddit = reddit.subreddit(subreddit_name.replace("r/", ""))
    for post in subreddit.hot(limit=50):  
        posts.append({
            "title": post.title,
            "selftext": post.selftext,
            "subreddit": subreddit_name,
            "label": label
        })

# Save to CSV
df = pd.DataFrame(posts)
df.to_csv("reddit_posts.csv", index=False)
print(" Done! Collected", len(df), "posts and saved to reddit_posts.csv")
