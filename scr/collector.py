import feedparser
import csv

# RSS feed URL
rss_url = "https://news.google.com/rss"

# Parse the feed
feed = feedparser.parse(rss_url)

# Print feed title
print(f"Feed Title: {feed.feed.title}\n")

for entry in feed.entries[:5]:
    print(f" Title: {entry.title}")
    print(f" Link:{entry.link}")
    print(f" Published: {entry.published}")
    print(f" Summary: {entry.summary[:200]}...") # first 100 characters
    print(" -"*40)

# create an empty dictionary to insert the data
dict_data = {"Title":[],
             "Link":[],
             "Published":[]}

for entry in feed.entries[:5]:
    dict_data["Title"].append(entry.title)
    dict_data['Link'].append(entry.link)
    dict_data['Published'].append(entry.published)

# save data as csv under data folder
with open("../data/output_data.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(dict_data.keys())
    writer.writerows(zip(*dict_data.values()))

