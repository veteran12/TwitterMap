from django.conf.urls import *
from tmap.views import index
from tmap.views import search
 
urlpatterns = patterns('',
                      url(r'^$',index),
                      url(r'^$',search),
                      )