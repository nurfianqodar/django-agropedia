from rest_framework import serializers
from ..models import Article


class ListArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["title", "author", "slug"]


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
