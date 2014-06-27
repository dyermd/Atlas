from django.contrib import admin
from project.models import Project
from project.models import Uses_Sample

# Register your models here.
class Project_Admin(admin.ModelAdmin):
    search_fields = ("name", "description")
    list_display = ("name", "description")
admin.site.register(Project, Project_Admin)

class Uses_Sample_Admin(admin.ModelAdmin):
    search_fields = ("project__name", "project__description", "sample__name", "sample__description")
    list_display = ("project", "sample")
admin.site.register(Uses_Sample, Uses_Sample_Admin)