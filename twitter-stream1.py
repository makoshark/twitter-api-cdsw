import tweepy
from twitter_authentication import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print tweet.user.screen_name + "\t" + tweet.text

    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        return False

l = StreamListener()
streamer = tweepy.Stream(auth=auth, listener=l)

streamer.sample()
