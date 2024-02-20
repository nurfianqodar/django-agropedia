from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import ArticleCategory
from ..serializers import ArticleCategorySerializer


class ArticleCategoryListView(APIView):
    def get(self, request):
        try :
            category = ArticleCategory.objects.all()
            ser = ArticleCategorySerializer(category, many=True)
            return Response(ser.data) 
        except :
            return Response({"errors" : "article is empty"}, status=status.HTTP_404_NOT_FOUND)




class ArticleCategoryView(APIView):
    def get(self, request, category):
        category = ArticleCategory.objects.get(id=category)
        ser = ArticleCategorySerializer(category)
        return Response(ser.data) 




