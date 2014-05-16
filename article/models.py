from django.db import models

# Create your models here.
class Article(models.Model):
    pubmed_id = models.IntegerField()
    pubmed_id.primary_key = True
    journal = models.CharField(max_length=100)
    title = models.TextField()
    year_published = models.IntegerField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
