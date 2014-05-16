from django.conf.urls import patterns, url
from protein import views

urlpatterns = patterns('', 
     url(r'^$', views.index, name='index'),
)
