import encoding_fix
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import time

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# I found the idea of how to the user the Cursor here:
#   https://tweepy.readthedocs.org/en/v3.4.0/cursor_tutorial.html
for page in tweepy.Cursor(api.home_timeline, count=200).pages():
    for tweet in page:
        print(tweet.text)
    time.sleep(1)
