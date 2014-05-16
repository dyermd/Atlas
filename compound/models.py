from django.db import models
from source.models import Source
from annotation.models import Annotation

# Create your models here.
class Compound(models.Model):
    lam_id = models.CharField(max_length=25)
    lam_id.primary_key = True
    name = models.CharField(max_length=250)
    smiles = models.TextField()
    structure_2d = models.ImageField(upload_to = "image_folder")
    
    def __unicode__(self):
        return(self.lam_id)

    class Meta:
        verbose_name = "Compound"
        verbose_name_plural = "Compounds"

class Compound_Xref(models.Model):
    compound = models.ForeignKey(Compound)
    source = models.ForeignKey(Source)
    xref = models.CharField(max_length=100)

    def __unicode__(self):
        return(self.compound.lam_id + " " + self.source.name + " " + self.xref)

    class Meta:
        verbose_name = "Compound Xref"
        verbose_name_plural = "Compound Xrefs"

class Patent(models.Model):
    compound = models.ForeignKey(Compound)
    source = models.ForeignKey(Source)
    patent_id = models.CharField(max_length=100)
    expiration_year = models.IntegerField()

    def __unicode__(self):
        return(self.compound.lam_id + " " + self.expiration_year)

    class Meta:
        verbose_name = "Patent"
        verbose_name_plural = "Patents"

class Manufacturer(models.Model):
    compound = models.ForeignKey(Compound)
    name = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __unicode__(self):
        return(self.compound.lam_id + " " + self.name)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

class Side_Effect(models.Model):
    compound1 = models.ForeignKey(Compound, related_name="compoundA")
    compound2 = models.ForeignKey(Compound, related_name="compoundB")
    side_effect = models.CharField(max_length=250)
    source = models.ForeignKey(Source)
    probability = models.FloatField()

    def __unicode__(self):
        if(self.compound1.name == self.compound2.name):
            return(self.compound1.name + " " + self.side_effect)
        else:
            return(self.compound1.name + " " + self.compound2.name + " " + self.side_effect)

    class Meta:
        verbose_name = "Side-Effect"
        verbose_name_plural = "Side-Effects"

class Annotated_With(models.Model):
    compound = models.ForeignKey(Compound)
    annotation = models.ForeignKey(Annotation, related_name="compound_annotation")

    def __unicode__(self):
        return(self.compound.name + " " + self.annotation.description)

    class Meta:
        verbose_name = "Annotated With"
        verbose_name_plural = "Annotated With"
