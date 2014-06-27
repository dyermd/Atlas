from django.db import models

# Create your models here.
class Analysis(models.Model):
    PENDING = "Pending"
    RUNNING = "Running"
    COMPLETE = "Complete"
    FAILED = "Failed"
    QUEUED = "Queued"

    STATUS = (
        (PENDING, "Pending"),
        (RUNNING, "Running"),
        (COMPLETE, "Complete"),
        (FAILED, "Failed"),
        (QUEUED, "Queued")
    )

    GERM = "Germline Variant Detection"
    SOM = "Somatic Variant Detection"
    QC = "QC"
    TRAN = "Transposon Screen"

    ANALYSIS_TYPE = (
        (GERM, "Germline Variant Detection"),
        (SOM, "Somatic Variant Detection"),
        (QC, "QC"),
        (TRAN, "Transposon Screen"),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=30, choices=ANALYSIS_TYPE, default=GERM)
    date = models.DateField()
    parameters = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS, default=PENDING)
    sge_job_number = models.IntegerField(blank=True, null=True)


    def __unicode__(self):
        return(self.name)

    class Meta:
        verbose_name = "Analysis"
        verbose_name_plural = "Analyses"

