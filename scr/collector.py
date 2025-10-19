import feedparser

# RSS feed URL
rss_url = "https://news.google.com/rss"

# Parse the feed
feed = feedparser.parse(rss_url)

# Print feed title
print(f"Feed Title: {feed.feed.title}\n")