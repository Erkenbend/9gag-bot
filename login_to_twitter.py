import tweepy

from yaml import safe_load, safe_dump

####
## Run this when auth has expired
####

with open('./resources/twitter_credentials.yml', 'r') as f:
    twitter_credentials = safe_load(f)

auth = tweepy.OAuthHandler(twitter_credentials['API-KEY'], twitter_credentials['API-SECRET-KEY'])

try:
    redirect_url = auth.get_authorization_url()
    print(redirect_url)
except tweepy.TweepError:
    print('Error! Failed to get request token.')

try:
    print('Please paste token from this URL ^')  # TODO automate this step with selenium
    auth.get_access_token(input())
except tweepy.TweepError:
    print('Error! Failed to get access token.')

with open('./resources/twitter_oauth_credentials.yml', 'w') as f:
    safe_dump({'OAUTH-ACCESS-TOKEN': auth.access_token, 'OAUTH-ACCESS-TOKEN-SECRET': auth.access_token_secret}, f)
