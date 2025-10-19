import feedparser
import csv

def collect_save_data(config):
    # RSS feed URL
    rss_url = config['source']['rss_url']
    save_to_file = config['output']['save_to_file']
    file_name = config['output']['file_name']

    # Parse the feed
    feed = feedparser.parse(rss_url)

    # create an empty dictionary to insert the data
    dict_data = {"Title":[],
                 "Link":[],
                 "Published":[]}

    for entry in feed.entries[:]:
        dict_data["Title"].append(entry.title)
        dict_data['Link'].append(entry.link)
        dict_data['Published'].append(entry.published)

    # save data as csv under data folder
    if save_to_file:
        with open(f'{file_name}',"w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(dict_data.keys())
            writer.writerows(zip(*dict_data.values()))
        print(f"\nArticles saved in {file_name}")

