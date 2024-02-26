from django.db import models


class ArticleComment(models.Model):
    comment = models.TextField(max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ManyToOneRel()
