import tweepy
from twitter_authentication import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

user = api.get_user('makoshark')

print user.screen_name + " has " + str(user.followers_count) + " followers."

print "They include these 100 people:"

for friend in user.friends(count=100):
   print friend.screen_name

