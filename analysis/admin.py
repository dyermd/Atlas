from django.contrib import admin
from analysis.models import Analysis

# Register your models here.

class Analysis_Admin(admin.ModelAdmin):
    search_fields = ("name", "description", "type", "parameters", "status")
    list_fields = ("name", "description", "type", "parameters", "status", "date")
admin.site.register(Analysis, Analysis_Admin)
