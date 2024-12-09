from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from webapp.forms import ArticleForm
from webapp.models import Article


class ArticleListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'articles': Article.objects.all()
        }
        return render(request, 'index.html', context=context)


class ArticleDetailView(TemplateView):
    template_name = 'article_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        return context


class ArticleCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                content=form.cleaned_data['content'],
            )
            tags = form.cleaned_data['tags']
            print(tags)
            article.tags.set(tags)
            return redirect('article_detail', pk=article.id)
        else:
            return render(request,
                          'article_create.html',
                          context={'form': form})


class ArticleUpdateView(View):
    def dispatch(self, request, *args, **kwargs):
        self.article = get_object_or_404(Article, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = ArticleForm(initial={
            'title': self.article.title,
            'author': self.article.author,
            'content': self.article.content,
            'tags': self.article.tags.all(),
        })
        return render(request, 'article_update.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            self.article.title = form.cleaned_data['title']
            self.article.author = form.cleaned_data['author']
            self.article.content = form.cleaned_data['content']
            self.article.save()
            tags = form.cleaned_data['tags']
            self.article.tags.set(tags)
            return redirect('article_detail', pk=self.article.id)
        else:
            return render(request, 'article_update.html', context={'form': form})


class ArticleDeleteView(View):
    def dispatch(self, request, *args, **kwargs):
        self.article = get_object_or_404(Article, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'article_delete.html', context={'article': self.article})

    def post(self, request, *args, **kwargs):
        self.article.delete()
        return redirect('articles')
