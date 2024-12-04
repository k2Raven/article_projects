from datetime import date
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from webapp.models import status_choices, Genre

# def publish_date_validate(publish_date):
#     if publish_date < date.today():
#         raise ValidationError('Дата публикации не может быть раньше чем сегодня')

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    author = forms.CharField(max_length=50, required=True, label="Автор")
    content = forms.CharField(required=True, label="Контент", widget=widgets.Textarea)
    status = forms.ChoiceField(choices=status_choices, label='Статус')
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), label='Жанр')
    publish_date = forms.DateField(label='Дата Публикации',
                                   # validators=[publish_date_validate],
                                   widget=widgets.DateInput(attrs={'type': 'date'}))

    def clean_publish_date(self):
        publish_date = self.cleaned_data['publish_date']
        if publish_date and publish_date < date.today():
            raise ValidationError('Дата публикации не может быть раньше чем сегодня')
        return publish_date

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title == content:
            raise ValidationError('Название и контент не могут быть одинаковыми')

        return cleaned_data
