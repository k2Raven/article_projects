import json
from datetime import datetime

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.generics import get_object_or_404

from api.serializers.article_serializers import ArticleSerializer
from webapp.models import Article



@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


class ArticlesAPIView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        article_data = json.loads(request.body)
        serializer = ArticleSerializer(data=article_data)
        if serializer.is_valid():
            article = serializer.save()
            article_serializer = ArticleSerializer(article)
            return JsonResponse(article_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, pk, **kwargs):
        article_data = json.loads(request.body)
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(data=article_data, instance=article)
        if serializer.is_valid():
            article = serializer.save()
            article_serializer = ArticleSerializer(article)
            return JsonResponse(article_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
