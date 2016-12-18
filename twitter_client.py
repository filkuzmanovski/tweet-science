# Twitter client for reading environment variables and authentication
import os # for pulling .environ dictionary
import sys
from tweepy import API
from tweepy import OAuthHandler

# authentication
def get_twitter_auth():
    """ Twitter authentication setup.

    Return: tweepy.OAuthHandler object
    """
    try: # read environment variables
        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_ACCESS_TOKEN_KEY']
        access_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    except KeyError: # missing environment variables error
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

# create instance of tweepy.API
def get_twitter_client():
    """ Twitter API client setup.

    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client
