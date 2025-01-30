import json
from datetime import datetime

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.article_serializers import ArticleSerializer
from webapp.models import Article, article


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


class ArticlesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        article_serializer = ArticleSerializer(article)
        return Response(article_serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(data=request.data, instance=article)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        article_serializer = ArticleSerializer(article)
        return Response(article_serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(data=request.data, instance=article, partial=True)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        article_serializer = ArticleSerializer(article)
        return Response(article_serializer.data, status=status.HTTP_200_OK)
