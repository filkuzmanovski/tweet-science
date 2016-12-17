# Twitter client for reading environment variables and authentication
import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    """ Twitter authentication setup.

    Return: tweepy.OAuthHandler object
    """
    try:
        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_TOKEN']
        access_secret = os.environ['TWITTER_TOKEN_SECRET']
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    """ Twitter API client setup.

    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client
