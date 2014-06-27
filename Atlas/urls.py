from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api

#import the tastypie api resources
from analysis.api import Analysis_Resource
from project.api import Project_Resource
from project.api import Uses_Sample_Resource
from sample.api import Sample_Resource
from file.api import File_Resource
from sample.api import Uses_File_Resource

#set up the resources
v1_api = Api(api_name='v1')
v1_api.register(Analysis_Resource())
v1_api.register(Project_Resource())
v1_api.register(File_Resource())
v1_api.register(Uses_Sample_Resource())
v1_api.register(Sample_Resource())
v1_api.register(Uses_File_Resource())

#admin stuff
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('home.urls', namespace='home')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^project/', include('project.urls', namespace='project')),
    url(r'^sample/', include('sample.urls', namespace='sample')),
    url(r'^file/', include('file.urls', namespace='file')),
    url(r'^analysis/', include('analysis.urls', namespace='analysis')),
)
