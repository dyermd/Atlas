from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from file.models import File

__author__ = 'mattdyer'

class File_Resource(ModelResource):
    class Meta:
        queryset = File.objects.all()
        resource_name = 'file'
        authorization = Authorization()