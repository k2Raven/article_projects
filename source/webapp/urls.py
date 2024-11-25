
from django.urls import path
from webapp.views import index_view, article_create_view, article_view

urlpatterns = [
    path('', index_view, name='articles'),
    path('article/add/', article_create_view, name='article_add'),
    path('article/<int:pk>/', article_view, name='article_detail'),
]