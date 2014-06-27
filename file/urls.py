from django.conf.urls import patterns, url, include
from file import views

__author__ = 'mattdyer'

urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^(?P<file_id>\w+)/$', views.detail, name='detail'),
)