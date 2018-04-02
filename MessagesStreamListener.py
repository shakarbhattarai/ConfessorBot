import tweepy
import time

from MessageHelper import MessageHelper
import json

def follow_back(a):

    for follower in tweepy.Cursor(a.APIinstance.API.followers).items():
        follower.follow()
        print follower.screen_name

class MessagesStreamListener(tweepy.StreamListener):

    def on_connect(self):
        pass

    def setAPIObject(self,api):
        self.api=api
    def on_direct_message(self, status):
        #sendmeanonmsg
        try:
            if status._json['direct_message']['sender']['screen_name'] !='sendmeanonmsg':
                self.api.send(status._json['direct_message']['text'])
        except:

            pass

    def on_warning(self, notice):
        print "Can't handle that many transactions. Please wait for a while until you make further requests"

a=MessageHelper()
listener=MessagesStreamListener(a.APIinstance)
listener.setAPIObject(a)
follow_back(a)
listen=tweepy.streaming.Stream(auth=a.APIinstance.auth, listener=listener)
listen.userstream()
