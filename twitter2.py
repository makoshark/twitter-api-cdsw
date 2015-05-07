import encoding_fix
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

user = api.get_user('makoshark')

print(user.screen_name + " has " + str(user.followers_count) + " followers.")

print("They include these 100 people:")

for follower in user.followers(count=100):
   print(follower.screen_name)

