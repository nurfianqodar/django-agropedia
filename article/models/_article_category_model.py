from django.db import models
from django.utils.text import slugify
from django.utils.dateparse import parse_date
from ._article_model import Article


class ArticleCategory(models.Model):
    id = models.SlugField(max_length=63, primary_key=True, default="autocreate")
    name = models.CharField(max_length=63, unique=True)
    description = models.TextField(max_length=511, null=True, blank=True)
    articles = models.ManyToManyField(
        Article,
        blank=True,
    )

    def save(self):
        self.id = slugify(self.name)
        super().save()

    def __str__(self):
        return self.name

    def count_articles(self):
        return self.articles.all().count()
