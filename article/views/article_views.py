from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import  Article
from ..serializers import ArticleSerializer, ListArticleSerializer

class ListArticleView(APIView):
    def get(self, request):
        try :
            articles = Article.objects.all()
            ser = ListArticleSerializer(articles, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)
        except :
            return Response({"errors" : "article is empty"}, status=status.HTTP_404_NOT_FOUND)

class ArticleView(APIView):
    def get(self, request, slug):
        article = Article.objects.get(slug=slug)
        ser = ArticleSerializer(article)
        return Response(ser.data)
    