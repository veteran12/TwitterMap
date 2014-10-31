'''
Created on Oct 23, 2014

@author: zhangtong
'''
from boto.dynamodb2.table import Table
import json
import boto.dynamodb2
import json as simplejson
from django.core.wsgi import get_wsgi_application

connection= boto.dynamodb2.connect_to_region('us-east-1a', aws_access_key_id='',
                                                aws_secret_access_key='')
tweetMap = Table('tweet')

fp = open("/Users/zhangtong/Desktop/CLOUD_COMPUTING/twitter_map/data.json")
#fout = open("/Users/zhangtong/Desktop/CLOUD_COMPUTING/twitter_map/outfile", "w")
for line in fp:
    s = json.loads(line)
    print s
    if s.has_key("text") and s.has_key("geo") and s.has_key("coordinates") and s.has_key("place") and s.has_key("created_at"):
        id_str = s["id_str"].encode('utf-8') if s["id_str"] else "N/A"
        text = s["text"].encode('utf-8') if s["text"] else "N/A"
        #geo = s["geo"].encode('utf-8') if s["geo"] else "N/A"
        coordinates = s["coordinates"]["coordinates"]
        #place = s["place"].encode('utf-8') if s["place"] else "N/A"
        created_at = s["created_at"].encode('utf-8') if s["created_at"] else "N/A"
        #tmp = text + "|" + geo + "|" + coordinates + "|" + place + "|" + created_at
        print id_str + " " + text + created_at
        print coordinates[0], coordinates[1]
        #fout.write(tmp + "\n")
        tweetMap.put_item(data = {
                        'tweetid' : id_str,
                        'text' : text,
                        'latitude' : str(coordinates[0]),
                        'longitude' : str(coordinates[1]),
                        'created_at' : created_at,
                        })
tweetMap.save()
#fout.close()
fp.close()
