#import twitter
import tweepy

from yaml import safe_load

with open('./resources/twitter_credentials.yml', 'r') as f:
    twitter_credentials = safe_load(f)

#api = twitter.Api(consumer_key=twitter_credentials['API-KEY'],
#                  consumer_secret=twitter_credentials['API-SECRET-KEY'])

#auth = tweepy.AppAuthHandler(twitter_credentials['API-KEY'], twitter_credentials['API-SECRET-KEY'])
auth = tweepy.OAuthHandler(twitter_credentials['API-KEY'], twitter_credentials['API-SECRET-KEY'])
try:
    redirect_url = auth.get_authorization_url()
    print(redirect_url)
except tweepy.TweepError:
    print('Error! Failed to get request token.')

try:
    auth.get_access_token(input())
except tweepy.TweepError:
    print('Error! Failed to get access token.')

api = tweepy.API(auth)

#user= api.get_user('realDonaldTrump')
#print(user)

api.update_status(status='Test test test')

