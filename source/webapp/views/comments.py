from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from webapp.forms import CommentForm
from webapp.models import Comment, Article


class CommentsCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comments/comment_create.html'
    form_class = CommentForm

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        form.instance.article = article
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:article_detail', kwargs={'pk': self.object.article.pk})


class CommentsUpdateView(PermissionRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/comment_update.html'
    permission_required = 'webapp.change_comment'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('webapp:article_detail', kwargs={'pk': self.object.article.pk})


class CommentsDeleteView(PermissionRequiredMixin, DeleteView):
    model = Comment
    permission_required = 'webapp.delete_comment'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('webapp:article_detail', pk=self.object.article.pk)