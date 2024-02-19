from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Article

class ArticleAdmin(ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    readonly_fields = ('slug', 'created_at')
    search_fields = ('slug', 'title', 'author')

    fieldsets = (
        (("Article ID"), {"fields": ("slug",)}),
        (("Article info"), {"fields": ("title", "author", "created_at")}),
        (("Article content"), {"fields": ("content",)}),
    )

admin.site.register(Article, ArticleAdmin)
