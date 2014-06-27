from django.conf.urls import patterns, url, include
from project import views

__author__ = 'mattdyer'

urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^(?P<project_id>\w+)/$', views.detail, name='detail'),
)


