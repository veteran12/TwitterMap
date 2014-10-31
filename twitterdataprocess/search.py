'''
Created on Oct 28, 2014

@author: zhangtong
'''
from boto.dynamodb2.table import Table
import boto.dynamodb2

connection= boto.dynamodb2.connect_to_region('us-east-1a', aws_access_key_id='',
                                                aws_secret_access_key='')
tweetMap = Table('tweetMap')

#result = tweetMap.batch_get(keys=[
#    {'tweetid': '525403743609970688'},
#])

result = tweetMap.scan(text__contains="KingHillwriter")

coordinate = []
for item in result:
    element = (item['text'].encode('utf-8'))
    coordinate.append(element)
for item in coordinate:
    print item
