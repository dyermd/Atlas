from django.conf.urls import patterns, url, include
from analysis import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<analysis_id>\d+)/$', views.detail, name='detail'),
    url(r'^launch/$', views.launch, name='launch'),
    url(r'^launch/single_sample_transposon$', views.single_sample_transposon, name='single_sample_transposon'),
)