import json
from datetime import datetime
from http import HTTPMethod

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api_v2.permissions import MyPermission
from api_v2.serializers.article_serializers import ArticleSerializer, ArticleListSerializer
from webapp.models import Article


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class ArticlesViewSet(ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [MyPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleSerializer

    @action(detail=True, methods=[HTTPMethod.GET], url_path='article_count')
    def article_count_comments(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        return Response({'count': article.comments.count()})

