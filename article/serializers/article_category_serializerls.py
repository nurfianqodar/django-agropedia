from rest_framework import serializers
from ..models import Article, ArticleCategory


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = '__all__'