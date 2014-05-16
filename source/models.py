from django.db import models

# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __unicode__(self):
        return(self.name)

    class meta:
        verbose_name = "Source"
        verbose_name_plural = "Sources"
