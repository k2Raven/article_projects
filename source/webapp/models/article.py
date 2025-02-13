from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from webapp.models import BaseModel

User = get_user_model()


class Article(BaseModel):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    content = models.TextField(null=False, blank=False, verbose_name="Контент")
    tags = models.ManyToManyField('webapp.Tag', related_name='articles', blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, related_name='articles',
                               verbose_name='Автор')

    def __str__(self):
        return f'{self.id}. {self.title}'

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        permissions = [
            ('change_article_tags', 'Менять теги статье')
        ]

    def get_absolute_url(self):
        return reverse('webapp:article_detail', kwargs={'pk': self.pk})