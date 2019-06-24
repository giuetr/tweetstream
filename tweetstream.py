#Tweetstream core
#A lightweight seamless engine that streams live tweets into a MongoDB collection based on a pre-defined set of hashtags.
#by giuetr ☼☼☼


import tweepy
import json
from pymongo import MongoClient


#Database pointer: change the XXXXX with your local database URI:
host_mongo= 'mongodb://localhost:XXXXX/twitterdb'
       
#Twitter Streaming API credentials: use your private credentials
consumer_key = "xxx"
consumer_secr = "xxx"
access_tkn = "xxx"
access_tkn_secr = "xxx"
                                      
#HASHTAGS list: edit the list with the tags to search
tags = ['#hashtag1','#hashtag2','#hashtag3']


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
            client = MongoClient(host_mongo)
            
            # Use twitterdb database. If it doesn't exist, this creates one.
            db = client.twitterdb
    
            # Decode the JSON from Twitter
            datajson = json.loads(data)
            
            #parse the Tweet 'created_at' data
            created_at = datajson['created_at']
 
            #message with timestamp of collection
            print("Tweet collected on " + str(created_at))
            
            #insert the data into the mongoDB into a collection called twitter_collection
            #if twitter_collectiondoesn't exist, it will be created.
            db.twitter_collection.insert(datajson)
        except Exception as e:
           print(e)
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secr)
auth.set_access_token(access_tkn, access_tkn_secr)
#Set up the listener. The 'wait_on_rate_limit=True' will bypass the Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(tags))
streamer.filter(track=tags)
