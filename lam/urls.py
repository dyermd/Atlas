from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('home.urls', namespace='home')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^protein/', include('protein.urls', namespace='protein')),
    url(r'^analysis/', include('analysis.urls', namespace='analysis')),
)
