import time, threading
from TwitterAPI import TwitterAPI

consumer_key        = "your consumer_key here"
consumer_secret     = "your consumer_secret here"
access_token_key    = "your access_token_key here"
access_token_secret = "your access_token_secret here"

#This is the search term for which the script returns tweets
search_term   = "Irvine"

#This is amount of time it takes to refresh the tweets
refresh_delay = 3


##########################################################################
# Fetches the Tweets and prints

def requestTweets():
	r = api.request('search/tweets', {'q':search_term})
	for item in r.get_iterator():
		print item["user"]["screen_name"]
		print item["text"]+"\n"
	threading.Timer(refresh_delay, requestTweets).start()

##########################################################################


api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

requestTweets()
