from django.db import models
from file.models import File

# Create your models here.

class Sample(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    plate_name = models.CharField(max_length=25, blank=True, null=True)

    def __unicode__(self):
        return(self.name)

    class Meta:
        verbose_name = "Sample"
        verbose_name_plural = "Sample"

class Uses_File(models.Model):
    sample = models.ForeignKey(Sample)
    file = models.ForeignKey(File)

    def __unicode__(self):
        return(self.sample.name + " " + self.file.name)

    class Meta:
        verbose_name = "Uses File"
        verbose_name_plural = "Uses Files"

class Sample_Relationship(models.Model):
    TUMOR = "Tumor"
    NORMAL = "Normal"
    CASE = "Case"
    CONTROL = "Control"
    MOTHER = "Mother"
    FATHER = "Father"
    CHILD = "Child"

    RELATIONSHIP_TYPE = (
        (TUMOR, "Tumor"),
        (NORMAL, "Normal"),
        (CASE, "Case"),
        (CONTROL, "Control"),
        (MOTHER, "Mother"),
        (FATHER, "Father"),
        (CHILD, "Child"),
    )

    sample1 = models.ForeignKey(Sample, related_name="sample1")
    sample2 = models.ForeignKey(Sample, related_name="sample2")
    role1 = models.CharField(max_length=15, choices=RELATIONSHIP_TYPE, default=NORMAL)
    role2 = models.CharField(max_length=15, choices=RELATIONSHIP_TYPE, default=NORMAL)
    
    def __unicode__(self):
        return(self.sample1.name + " " + self.role1 + " " + self.sample2.name + " " + self.role2)

    class Meta:
        verbose_name = "Sample Relationship"
        verbose_name_plural = "Sample Relationships"
