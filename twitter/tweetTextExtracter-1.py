import json
import codecs

import re
from itertools import chain
import pickle
tweets = []
output_file=open('test.json', 'w')
for line in open('tweetsamsung.json'):
    tweets.append(json.loads(line))
print "The number of tweets is ",len(tweets)
#for i in range(0,len(tweets)):
result=[]
for item in tweets:
    try:
    	my_dict={}
    	my_dict['follower_count'] = item.get('user').get('followers_count')
    	result.append(my_dict)
    except:
        pass
back_json = json.dumps(result, output_file)
        

