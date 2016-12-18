import json
from tweepy import Cursor
from twitter_client import get_twitter_client

if __name__ == '__main__':
    client = get_twitter_client()

    with open('home_timeline.jsonl', 'w') as f: # Output in JSON Lines format
        for page in Cursor(client.home_timeline, count=200, include_rts=True).pages(4): # 200 Tweets, 4 Pages
            for status in page:
                # Process a status
                f.write(json.dumps(status._json)+ "\n")
