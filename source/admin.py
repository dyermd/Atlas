from django.contrib import admin
from source.models import Source

# Register your models here.
class Source_Admin(admin.ModelAdmin):
    search_fields = ("name", "url")
    list_display = ("name", "url")
admin.site.register(Source, Source_Admin)
