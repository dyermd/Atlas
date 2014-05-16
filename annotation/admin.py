from django.contrib import admin
from annotation.models import Annotation_Model
from annotation.models import Annotation

# Register your models here.

class Annotation_Model_Admin(admin.ModelAdmin):
    search_fields = ("source__name", "version")
    list_display = ("source", "version")
admin.site.register(Annotation_Model, Annotation_Model_Admin)

class Annotation_Admin(admin.ModelAdmin):
    search_fields = ("model__source__name", "annotation_id", "description")
    list_display = ("model", "get_version", "annotation_id", "description")

    def get_version(self, obj):
        return obj.source.version
    get_version.short_description="Version"
admin.site.register(Annotation, Annotation_Admin)
