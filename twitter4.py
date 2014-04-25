import tweepy
from twitter_authentication import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# code to write the file
import codecs
output_file = codecs.open("MY_DATA.tsv", "w", "utf-8")

public_tweets = api.search("data science", count=10)

for tweet in public_tweets:
    print >>output_file, tweet.user.screen_name + "\t" + str(tweet.created_at) + "\t" + tweet.text

