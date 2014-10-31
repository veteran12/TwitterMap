from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from boto.dynamodb2.table import Table
import json as simplejson
import boto.dynamodb2

# Create your views here.
def index(request):
    #template = loader.get_template("index.html")
    #return HttpResponse(template.render())
    return render(request, 'index.html')
    #return HttpResponse("haha22")

def search(request):
    keyword = request.GET.get('keyword', '')
    #connection= boto.dynamodb2.connect_to_region('us-east-1a', aws_access_key_id='',
    #                                            aws_secret_access_key='')
    conn = boto.connect_dynamodb()
    tweetMap = Table('tweet')

    #result = tweetMap.batch_get(keys=[
    #    {'tweetid': '525403743609970688'},
    #])
    result = tweetMap.scan(text__contains=keyword)
    
    coordinates = {}
    i = 0
    for item in result:
        i = i + 1
        latitude = item['latitude'].encode('utf-8')
        longitude = item['longitude'].encode('utf-8')
        text = item['text'].encode('utf-8')
        element = (latitude, longitude, text)
        #element = keyword
        coordinates[i] = element

    
    jsondata = simplejson.dumps(coordinates)
    return HttpResponse(jsondata, content_type="application/json")    
    #t = loader.get_template("index.html")
    #c = Context({'coordinates':coordinates})
    #return HttpResponse(t.render(c))
    #return HttpResponse(item['text'].encode('utf-8'))
