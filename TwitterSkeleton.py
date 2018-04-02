import tweepy



class TwitterSkeleton:

    def __init__(self):
        auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
        self.auth=auth
        self.API= tweepy.API(auth)

    def sendMessage(self,to_user,message='Hey!'):
        print to_user,message
        self.API.send_direct_message(to_user,text=message)

