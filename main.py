
# Authenticate to Twitter
# https://developer.twitter.com/en/portal/projects/1487176177085255682/apps/23232500/keys

import tweepy
import json

with open('static/keys.json') as f:
    API_keys = json.load(f)

CONSUMER_KEY = API_keys['CONSUMER_KEY']
CONSUMER_SECRET = API_keys['CONSUMER_SECRET']

auth = tweepy.OAuthHandler(
    CONSUMER_KEY, 
    CONSUMER_SECRET
)

ACCESS_TOKEN = API_keys['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = API_keys['ACCESS_TOKEN_SECRET']

auth.set_access_token(
    ACCESS_TOKEN, 
    ACCESS_TOKEN_SECRET
)

API = tweepy.API(auth)

try: 
    API.verify_credentials()
    print('\nAuthentication OK.')

except Exception as e: 
    print('\n', e)

# tweet = API.retweet(id = 1726946437991453064)
# print(tweet)

'''
tweepy.errors.Forbidden: 403 Forbidden
https://stackoverflow.com/a/76520660/11493297

453 - You currently have access to a subset of Twitter API v2 endpoints and 
limited v1.1 endpoints (e.g. media post, oauth) only. If you need access to 
this endpoint, you may need a different access level. 

You can learn more here: https://developer.twitter.com/en/portal/product
'''
