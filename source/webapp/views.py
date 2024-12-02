from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Article
from webapp.validate import article_validator


def index_view(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'index.html', context=context)

def article_view(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', context={'article': article})

def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')

        article = Article(title=title, content=content, author=author)

        errors = article_validator(article)

        if errors:
            return render(request,
                          'article_create.html',
                          context={'errors': errors, 'article': article})

        article.save()
        return redirect('article_detail', pk=article.id)

def article_update_view(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'article_update.html', context={'article': article})
    elif request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.author = request.POST.get('author')

        errors = article_validator(article)

        if errors:
            return render(request,
                          'article_update.html',
                          context={'errors': errors, 'article': article})

        article.save()
        return redirect('article_detail', pk=article.id)