from django import forms
from django.forms import widgets

from webapp.models import Tag


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    author = forms.CharField(max_length=50, required=True, label="Автор")
    content = forms.CharField(required=True, label="Контент", widget=widgets.Textarea)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), label='Теги', required=True)
