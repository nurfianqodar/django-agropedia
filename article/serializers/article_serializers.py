from rest_framework import serializers
from ..models import Article, ArticleCategory

class ListArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('slug', 'title', 'author', 'created_at') 

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'