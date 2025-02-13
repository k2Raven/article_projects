from django.urls import path
from webapp.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, \
    CommentsCreateView, CommentsUpdateView, CommentsDeleteView, json_echo_view, get_token_view, ArticlesAPIView

app_name = 'webapp'

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('article/add/', ArticleCreateView.as_view(), name='article_add'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<int:pk>/comment/add/', CommentsCreateView.as_view(), name='comment_add'),
    path('comment/<int:pk>/update/', CommentsUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentsDeleteView.as_view(), name='comment_delete'),
    path('echo/', json_echo_view, name='echo'),
    path('token/', get_token_view, name='token'),
    path('articles/', ArticlesAPIView.as_view(), name='articles_json')
]
