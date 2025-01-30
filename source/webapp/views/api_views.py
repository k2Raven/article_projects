import json
from datetime import datetime

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie

from webapp.models import Article


def json_echo_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    if request.body:
        answer['content'] = json.loads(request.body)

    return JsonResponse(answer)


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


class ArticlesAPIView(View):
    def get(self, request, *args, **kwargs):
        fields = ('id', 'title', 'content')
        articles = Article.objects.values(*fields)
        # articles = Article.objects.all()
        #
        # articles_data = serialize('json', articles)
        #
        # response = HttpResponse(articles_data)
        #
        # response['Content-Type'] = 'application/json'
        # return response
        return JsonResponse(list(articles), safe=False)

    def post(self, request, *args, **kwargs):
        article_data = json.loads(request.body)
        article = Article.objects.create(**article_data)
        return JsonResponse({'id': article.id})
