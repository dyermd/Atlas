from django.contrib import admin
from sample.models import Sample
from sample.models import Sample_Relationship
from sample.models import Uses_File

# Register your models here.
class Sample_Admin(admin.ModelAdmin):
    search_fields = ("name", "description")
    list_display = ("name", "description")
admin.site.register(Sample, Sample_Admin)

class Uses_File_Admin(admin.ModelAdmin):
    search_fields = ("sample__name", "file__name", "file__description", "file__type")
    list_display = ("sample", "file", "get_path", "get_type", "get_primary")

    def get_path(self, obj):
        return obj.file.file_path
    get_path.short_description="Path"

    def get_type(self, obj):
        return obj.file.file_type
    get_type.short_description="Type"

    def get_primary(self, obj):
        return obj.file.is_primary
    get_primary.short_description="Is Primary"
admin.site.register(Uses_File, Uses_File_Admin)

class Sample_Relationship_Admin(admin.ModelAdmin):
    search_fields = ("sample1__name", "sample1__description", "sample2__name", "sample2__description", "role1", "role2")
    list_display = ("sample1", "role1", "sample2", "role2")
admin.site.register(Sample_Relationship, Sample_Relationship_Admin)
