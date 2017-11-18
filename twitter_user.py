from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3348771613-QAi7lNsh1wdZzaBqVftpzGgyzl62sFF9KLBTiCH"
access_token_secret = "5cIUgORFfTwDOSZWWDcWr4o3BOjO5uOOPviK9xsL3cOHF"
consumer_key = "UhuLKGNFGBSoQRD8ad3wu0Unz"
consumer_secret = "Dy501fQbzuhGsr4JGTAMOzZgjAHRFfqwM5FGLXO66CCrfi71GK"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(follow=['js100radio','fm91trafficpro','longdotraffic','weather_th','traffy'])
