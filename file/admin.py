from django.contrib import admin
from file.models import File

# Register your models here.
class File_Admin(admin.ModelAdmin):
    search_fields = ("name", "description", "file_type", "is_primary")
    list_display = ("name", "description", "file_path", "file_type", "is_primary")
admin.site.register(File, File_Admin)