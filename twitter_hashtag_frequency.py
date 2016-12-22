# run python twitter_hashtag_frequency.py user_timeline_tweetusername.jsonl
# user_timeline_tweetusername.jsonl is my jsonl file that is pulled with running python twitter_get_user_timeline
import sys
from collections import Counter
import json

def get_hashtags(tweet):
    entities = tweet.get('entities', {})
    hashtags = entities.get('hashtags', [])
    return [tag['text'].lower() for tag in hashtags]

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        hashtags = Counter()
        for line in f:
            tweet = json.loads(line)
            hashtags_in_tweet = get_hashtags(tweet)
            hashtags.update(hashtags_in_tweet)
        for tag, count in hashtags.most_common(20):
            print("{}: {}".format(tag, count))

''' At the time of this commit the result of running the hashtag frequency script was the following
trump2016: 240
makeamericagreatagain: 204
maga: 111
americafirst: 80
draintheswamp: 78
imwithyou: 62
bigleaguetruth: 58
votetrump: 53
debate: 47
crookedhillary: 38
trumptrain: 34
trumppence16: 34
debates2016: 24
icymi: 22
supertuesday: 20
vpdebate: 19
debates: 16
rncincle: 15
wiprimary: 13
thankyoutour2016: 12
'''
