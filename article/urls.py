from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListArticleView.as_view()),
    path('categories/', views.ArticleCategoryListView.as_view()),
    path('categories/<str:category>/', views.ArticleCategoryView.as_view()),
    path('article/<str:slug>/', views.ArticleView.as_view())
]