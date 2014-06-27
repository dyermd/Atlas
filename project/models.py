from django.db import models
from sample.models import Sample

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return(self.name)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class Uses_Sample(models.Model):
    project = models.ForeignKey(Project)
    sample = models.ForeignKey(Sample)

    def __unicode__(self):
        return(self.project.name + " " + self.sample.name)

    class Meta:
        verbose_name = "Uses Sample"
        verbose_name_plural = "Uses Samples"