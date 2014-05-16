from django.contrib import admin
from note.models import Note

# Register your models here.
class Note_Admin(admin.ModelAdmin):
    search_fields = ("note", "date")
    list_display = ("note", "date")
admin.site.register(Note, Note_Admin)
