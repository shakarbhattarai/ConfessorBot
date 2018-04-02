from TwitterSkeleton import TwitterSkeleton


class MessageHelper:
    def __init__(self):
        self.APIinstance = TwitterSkeleton()

    def send(self,message):
        self.originalmessage=message
        self.setUsernameandMessage()
        self.APIinstance.sendMessage(self.toSend.replace('@',''),self.actualMessage)

    def setUsernameandMessage(self):
        self.toSend,self.actualMessage=self.originalmessage.split(':')


