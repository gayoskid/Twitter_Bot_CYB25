import schedule
import time
from scrape_posts import *
from twitter_api import *

def schedule_tweets():
    # Scrape posts and store them
    scrape_posts()

    # Schedule the tweets to be posted every 5 hours
    for post in post_contents:
        tweet_text = post["Title"]
        schedule.every(1).minutes.do(post_tweet, text = tweet_text).tag('tweet')

    # Keep running the schedule in the background
    while True:
        schedule.run_pending()
        time.sleep(1)
