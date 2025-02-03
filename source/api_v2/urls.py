from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api_v2.views import LogoutView, ArticlesViewSet

router = DefaultRouter()
router.register('articles', ArticlesViewSet)

app_name = 'api_v2'

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_logout'),
]
