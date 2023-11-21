
# Authenticate to Twitter
# https://developer.twitter.com/en/portal/projects/1487176177085255682/apps/23232500/keys

import tweepy
import json

with open('static/keys.json') as f:
    API_keys = json.load(f)

CONSUMER_KEY = API_keys['CONSUMER_KEY']
CONSUMER_SECRET = API_keys['CONSUMER_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

ACCESS_TOKEN = API_keys['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = API_keys['ACCESS_TOKEN_SECRET']
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

API = tweepy.API(auth)
try:
    API.verify_credentials()
    print("\nAuthentication OK")
except:
    print("\nError during authentication")
