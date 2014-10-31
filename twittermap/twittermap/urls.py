from django.conf.urls import patterns, include, url
from django.contrib import admin
from tmap.views import index
from tmap.views import search

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twittermap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^index/', include('tmap.urls')),
    #url(r'^search/', include('tmap.urls')),
    url(r'^index/', index),
    url(r'^search/', search),
    url(r'^admin/', include(admin.site.urls)),
)
