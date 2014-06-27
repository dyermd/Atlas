from django.db import models

# Create your models here.

class File(models.Model):
    BAM = "BAM"
    VCF = "VCF"
    QC = "QC"
    QC3B3 = "3x3"
    TRAN = "Transposon Tab"
    TRANR = "Transposon Report"

    FILE_TYPE = (
        (BAM, "BAM"),
        (VCF, "VCF"),
        (QC, "QC"),
        (QC3B3, "3x3"),
        (TRAN, "Transposon Tab"),
        (TRANR, "Transposon Report"),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    #file = models.FileField(upload_to="documents/%Y/%m/%d")
    file_path = models.CharField(max_length=300)
    file_type = models.CharField(max_length=50, choices=FILE_TYPE, default=BAM)
    is_primary = models.BooleanField()
    ts_run_report = models.CharField(max_length=300, blank=True, null=True)
    date = models.DateField()


    def __unicode__(self):
        return(self.name)

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"