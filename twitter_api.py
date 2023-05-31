import tweepy
from credentials import *

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def post_tweet(text):
    client.create_tweet(text = text)
    print("Tweet posted:", text)
