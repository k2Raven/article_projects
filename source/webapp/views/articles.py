from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlencode
from django.views.generic import View, TemplateView, FormView, ListView, DetailView
from webapp.forms import ArticleForm, SearchForm
from webapp.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/index.html'
    context_object_name = 'articles'
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 2

    def dispatch(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) | Q(author__icontains=self.search_value))

        return queryset

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context



class ArticleDetailView(DetailView):
    template_name = 'articles/article_view.html'
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by('-created_at')
        return context


class ArticleCreateView(FormView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm

    # def get_success_url(self):
    #     return reverse('article_detail', kwargs={'pk': self.article.pk})

    def form_valid(self, form):
        article = form.save()
        return redirect('article_detail', pk=article.pk)

class ArticleUpdateView(FormView):
    template_name = 'articles/article_update.html'
    form_class = ArticleForm

    def dispatch(self, request, *args, **kwargs):
        self.article = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.article
        return context

    def get_object(self):
        return get_object_or_404(Article, pk=self.kwargs.get('pk'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

    def form_valid(self, form):
        self.article = form.save()
        return redirect('article_detail', pk=self.article.id)

class ArticleDeleteView(View):
    def dispatch(self, request, *args, **kwargs):
        self.article = get_object_or_404(Article, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'articles/article_delete.html', context={'article': self.article})

    def post(self, request, *args, **kwargs):
        self.article.delete()
        return redirect('articles')
