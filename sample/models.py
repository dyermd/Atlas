from django.db import models

# Create your models here.

class Sample(models.Model):
    BAM = "BAM"
    VCF = "VCF"

    FILE_TYPE = (
        (BAM, "BAM"),
        (VCF, "VCF"),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to="documents/%Y/%m/%d")
    file_type = models.CharField(max_length=10, choices=FILE_TYPE, default=BAM)

    def __unicode__(self):
        return(self.name)

    class Meta:
        verbose_name = "Sample"
        verbose_name_plural = "Samples"

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
    role1 = models.CharField(max_length=15, choices=RELATIONSHIP_TYPE, default=NORMAL);
    role2 = models.CharField(max_length=15, choices=RELATIONSHIP_TYPE, default=NORMAL);
    
    def __unicode__(self):
        return(self.sample1.name + " " + self.role1 + " " + self.sample2.name + " " + self.role2)

    class Meta:
        verbose_name = "Sample Relationship"
        verbose_name_plural = "Sample Relationships"
