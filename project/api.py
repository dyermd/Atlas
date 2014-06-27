from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields

from project.models import Project
from project.models import Uses_Sample

from sample.api import Sample_Resource

__author__ = 'mattdyer'

class Project_Resource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        authorization = Authorization()

class Uses_Sample_Resource(ModelResource):
    project = fields.ForeignKey(Project_Resource, 'project')
    sample = fields.ForeignKey(Sample_Resource, "sample")

    class Meta:
        queryset = Uses_Sample.objects.all()
        resource_name = 'uses_sample'
        authorization = Authorization()