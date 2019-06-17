import tweepy
import json
from pymongo import MongoClient


#Database pointer: change the XXXXX with your local database URI:
MONGO_HOST= 'mongodb://localhost:XXXXX/twitterdb'
                                             
#HASHTAGS list: edit the list with the tags to search
WORDS = ['#hashtag1','hashtag2','hashtag3']

#Twitter Streaming API credentials: use your private credentials
CONSUMER_KEY = "xxx"
CONSUMER_SECRET = "xxx"
ACCESS_TOKEN = "xxx"
ACCESS_TOKEN_SECRET = "xxx"
 
 
class StreamListener(tweepy.StreamListener):    
    #tweepy class to access the Twitter Streaming API. 
 
    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the Twitter streaming API.")
 
    def on_error(self, status_code):
        # On error - display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        #The engine: database connection and real-time fetching:
        try:
            client = MongoClient(MONGO_HOST)
            
            # Use twitterdb database. If it doesn't exist, this creates one.
            db = client.twitterdb
    
            # Decode the JSON from Twitter
            datajson = json.loads(data)
            
            #parse the Tweet 'created_at' data
            created_at = datajson['created_at']
 
            #message with timestamp of collection
            print("Tweet collected at " + str(created_at))
            
            #insert the data into the mongoDB into a collection called twitter_search
            #if twitter_search doesn't exist, it will be created.
            db.twitter_search.insert(datajson)
        except Exception as e:
           print(e)
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)