from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from analysis.models import Analysis

__author__ = 'mattdyer'

class Analysis_Resource(ModelResource):
    class Meta:
        queryset = Analysis.objects.all()
        resource_name = 'analysis'
        authorization = Authorization()
