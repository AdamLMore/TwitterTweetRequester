import time, threading
from TwitterAPI import TwitterAPI

consumer_key        = "your consumer_key here"
consumer_secret     = "your consumer_secret here"
access_token_key    = "your access_token_key here"
access_token_secret = "your access_token_secret here"


#The term that is searched for in the query 
search_term   = "twitch"
#The amount of time it takes to refresh the feed
refresh_delay = 3
#Latest tweet ID
latest_id = 0
#Total number of tweets fetched at a time
count = 1 


##########################################################################
# Fetches the Tweets and prints

def requestTweets():
	global latest_id
	r = api.request('search/tweets', {'q':search_term, 'count':count, 'since_id':int(latest_id)})
	for item in r.get_iterator():
		latest_id = item["id"]
		print item["user"]["screen_name"]
		print item["text"]+"\n\n"
		print "==========================================================="
		print "\n"
	threading.Timer(refresh_delay, requestTweets).start()

##########################################################################


api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

requestTweets()
