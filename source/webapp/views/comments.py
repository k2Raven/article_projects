from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import CommentForm
from webapp.models import Comment, Article


class CommentsCreateView(CreateView):
    model = Comment
    template_name = 'comments/comment_create.html'
    form_class = CommentForm

    # def form_valid(self, form):
    #     article = get_object_or_404(Article, pk=self.kwargs['pk'])
    #     form.instance.article = article
    #     return super().form_valid(form)

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        self.object = form.save(commit=False)
        self.object.article = article
        self.object.save()
        # form.save_m2m() Только если есть связь многие ко многим
        return redirect(article.get_absolute_url())

    # def get_success_url(self):
    #     return reverse('article_detail', kwargs={'pk': self.object.article.pk})