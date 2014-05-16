from django.contrib import admin
from article.models import Article

# Register your models here.
class Article_Admin (admin.ModelAdmin):
    search_fileds = ("pubmed_id", "journal", "title", "year_published")
    list_display = ("pubmed_id", "journal", "title", "year_published")
admin.site.register(Article, Article_Admin)
