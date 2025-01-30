from django.urls import path
from api.views import get_token_view, ArticlesAPIView

app_name = 'api'

urlpatterns = [
    path('token/', get_token_view, name='token'),
    path('articles/', ArticlesAPIView.as_view()),
    path('articles/<int:pk>/', ArticlesAPIView.as_view())
]
