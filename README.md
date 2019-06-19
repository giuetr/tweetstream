# tweetstream
A streaming engine for live fetching tweets and store them into a MongoDB database.

------------- 
**Tweetstream** is a light and functional solution for parsing Tweets in real time and storing them in a local MongoDB collection.

An easy-to-use starting point to implement different analysis routines including sentiment analysis, textual analysis and other parsing methods.

I.e.: the app can collect and store tweets based on a group of tickers ('#ADBE', '#NVDA', '#ORCL', ...).


Requirements:
------------- 
- tweepy
- pymongo
- The Twitter Streaming API keys
- MongoDB installed locally

Editing
-------
The code can be used as-it-is, just edit it with your **Twitter Streaming API keys**:

```bash
consumer_key = "your consumer key"
consumer_secr = "your consumer secret"
access_tkn = "your access token"
access_tkn_secr = "your access token secret"
```

Point it to your **local MongoDB**:

```bash
host_mongo= 'mongodb://localhost:XXXXX/twitterdb'
```

And edit the **'tags'** list with your hashtags of interest:
```bash
tags = ['#EU','#Italy','#Germany','#Libra',...]
```


Launch
------------- 

 Simply launch it via prompt and start collecting tweets in real-time:
 ```bash
 $ python tweetstream.py
 ```
 
In the following example we are tracking ***Libra***, Facebook's new cryptocurrency:
![](cmd1.gif)

The stream is on and Tweets are stored in our database collection:
![](db1.gif)

