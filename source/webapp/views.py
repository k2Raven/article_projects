from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Article, Genre


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
        genres = Genre.objects.all()
        return render(request, 'article_create.html', context={'genres': genres})
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        genre_id = request.POST.get('genre_id')
        # genre = get_object_or_404(Genre, pk=genre_id)
        article = Article.objects.create(title=title,
                                         content=content,
                                         # genre=genre,
                                         genre_id=genre_id,
                                         author=author)
        return redirect('article_detail', pk=article.id)