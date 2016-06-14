from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd

#Variables that contains the user credentials to access Twitter API 
access_token = "340991207-lWN0HAXFpAjDtJn0mOx8Ofk5zgrxwzdv2gFIjnNo"
access_token_secret = "GqrkDzZqbsGCsQfVqDySfA9VtOx9FsfNAkCE4VbI5MiHW"
consumer_key = "RoV6T2ZzYf1mEomjxqs8ChNaS"
consumer_secret = "EQi5YIAAJnRoTzJq5B9MNPuNZcSBeUeuMAUEo3lgCc9LDPnuaz"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        with open('tweet_blackberry.json','a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['BlackBerry', 'priv'])






