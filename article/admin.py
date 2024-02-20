from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Article, ArticleCategory

class ArticleAdmin(ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
    readonly_fields = ('slug', 'created_at')
    search_fields = ('slug', 'title', 'author')

    fieldsets = (
        (("Article ID"), {"fields": ("slug",)}),
        (("Article info"), {"fields": ("title", "author", "created_at")}),
        (("Article content"), {"fields": ("content",)}),
    )


class ArticleCategoryAdmin(ModelAdmin):
    list_display = ('name', 'count_articles')
    filter_horizontal = ("articles",)
    readonly_fields = ['id', 'count_articles']
    

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
