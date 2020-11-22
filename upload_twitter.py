#import twitter
import tweepy

from yaml import safe_load

def upload_twitter():

    # re-authenticate
    with open('./resources/twitter_credentials.yml', 'r') as f:
        twitter_credentials = safe_load(f)
    auth = tweepy.OAuthHandler(twitter_credentials['API-KEY'], twitter_credentials['API-SECRET-KEY'])

    with open('./resources/twitter_oauth_credentials.yml', 'r') as f:
        twitter_oauth_credentials = safe_load(f)
    auth.set_access_token(twitter_oauth_credentials['OAUTH-ACCESS-TOKEN'], twitter_oauth_credentials['OAUTH-ACCESS-TOKEN-SECRET'])

    # init api
    api = tweepy.API(auth)

    # post stuff
    media_obj = api.media_upload("./meme.png")
    api.update_status(status='Test test test', media_ids=[media_obj.media_id])

if __name__ == '__main__':
    upload_twitter()
