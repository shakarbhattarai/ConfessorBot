import tweepy

CONSUMER_KEY="CONSUMER_KEY_HERE"
CONSUMER_SECRET="CONSUMER_SECRET_HERE"
ACCESS_TOKEN="ACCESS_TOKEN_HERE"
ACCESS_TOKEN_SECRET="ACCESS_TOKEN_SECRET_HERE"

class TwitterHelper:

    def __init__(self):
        auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
        self.API= tweepy.API(auth)

    def sendMessage(self,to_user,message='Hey!'):
        self.API.send_direct_message(user_id=to_user,text=message)