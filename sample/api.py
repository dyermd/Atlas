from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields

from sample.models import Sample
from sample.models import Uses_File

from file.api import File_Resource

__author__ = 'mattdyer'

class Sample_Resource(ModelResource):
    class Meta:
        queryset = Sample.objects.all()
        resource_name = 'sample'
        authorization = Authorization()

class Uses_File_Resource(ModelResource):
    file = fields.ForeignKey(File_Resource, 'file')
    sample = fields.ForeignKey(Sample_Resource, "sample")

    class Meta:
        queryset = Uses_File.objects.all()
        resource_name = 'uses_file'
        authorization = Authorization()