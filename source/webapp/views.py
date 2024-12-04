from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ArticleForm
from webapp.models import Article


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
        form = ArticleForm()
        return render(request, 'article_create.html', {'form': form})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                content=form.cleaned_data['content'],
                status=form.cleaned_data['status'],
                genre=form.cleaned_data['genre'],
                publish_date=form.cleaned_data['publish_date'],
            )
            return redirect('article_detail', pk=article.id)

        else:
            return render(request,
                          'article_create.html',
                          context={'form': form})


def article_update_view(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = ArticleForm(initial={
            'title': article.title,
            'author': article.author,
            'content': article.content,
            'status': article.status,
            'genre': article.genre,
            'publish_date': article.publish_date,
        })
        return render(request, 'article_update.html', context={'form': form})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.author = form.cleaned_data['author']
            article.content = form.cleaned_data['content']
            article.status = form.cleaned_data['status']
            article.genre = form.cleaned_data['genre']
            article.publish_date = form.cleaned_data['publish_date']
            article.save()
            return redirect('article_detail', pk=article.id)
        else:
            return render(request, 'article_update.html', context={'form': form})


def article_delete_view(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'article_delete.html', context={'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('articles')
