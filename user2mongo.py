from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient
from tweepy import Stream

MONGO_HOST= 'mongodb://localhost/twitter'  # assuming you have mongoDB installed locally
                                             # and a database called 'twitterdb'

WORDS = ['js100radio','fm91trafficpro','longdotraffic','weather_th','traffy']


ACCESS_TOKEN = "3348771613-QAi7lNsh1wdZzaBqVftpzGgyzl62sFF9KLBTiCH"
ACCESS_TOKEN_SECRET = "5cIUgORFfTwDOSZWWDcWr4o3BOjO5uOOPviK9xsL3cOHF"
CONSUMER_KEY = "UhuLKGNFGBSoQRD8ad3wu0Unz"
CONSUMER_SECRET = "Dy501fQbzuhGsr4JGTAMOzZgjAHRFfqwM5FGLXO66CCrfi71GK"


class StreamListener(tweepy.StreamListener):    
    #This is a class provided by tweepy to access the Twitter Streaming API. 

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")
 
    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            client = MongoClient(MONGO_HOST)
            
            # Use twitterdb database. If it doesn't exist, it will be created.
            db = client.twitter
    
            # Decode the JSON from Twitter
            datajson = json.loads(data)
            
            #grab the 'created_at' data from the Tweet to use for display
            created_at = datajson['created_at']

            #print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at))
            
            #insert the data into the mongoDB into a collection called twitter_search
            #if twitter_search doesn't exist, it will be created.
            db.follow.insert(datajson)
        except Exception as e:
           print(e)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(follow=['js100radio','fm91trafficpro','longdotraffic','weather_th','traffy'])