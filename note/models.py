from django.db import models

# Create your models here.
class Note(models.Model):
    note = models.TextField()
    date = models.DateField()

    def __unicode__(self):
        return(self.note)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
