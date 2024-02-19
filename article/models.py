from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    slug = models.SlugField(
        verbose_name='slug',
        max_length=255,
        primary_key=True,
        default='-',
        help_text='This field is autocreated.'
    )

    title = models.TextField(
        verbose_name='title',
        unique=True,
        help_text='Title must be unique'
    )

    created_at = models.DateTimeField(
        verbose_name='created at',
        auto_now_add=True,
        help_text='This field is autocreated.'
    )

    author = models.CharField(
        verbose_name='author',
        max_length=127
    )

    content = models.TextField(
        verbose_name='content'
    )
    
    # Meta 
    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title
