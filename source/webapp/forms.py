from django import forms
from django.forms import widgets

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    author = forms.CharField(max_length=50, required=True, label="Автор")
    content = forms.CharField(required=True, label="Контент", widget=widgets.Textarea)
