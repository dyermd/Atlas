from django.db import models
from source.models import Source

# Create your models here.
class Annotation_Model(models.Model):
    source = models.ForeignKey(Source)
    version = models.CharField(max_length=25)
    
    def __unicode__(self):
        return(self.source.name + " " + self.version)

    class Meta:
        verbose_name = "Annotation Model"
        verbose_name_plural = "Annotation Models"

class Annotation(models.Model):
    model = models.ForeignKey(Annotation_Model)
    annotation_id = models.CharField(max_length=250)
    description = models.TextField()

    def __unicode__(self):
        return(self.model.source.name + " " + self.annotation_id)

    class Meta:
        verbose_name = "Annotation"
        verbose_name_plural = "Annotations"
