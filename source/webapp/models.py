from django.db import models

status_choices = [('new', 'Новая'), ('moderated', 'Модерированная'),  ('published', 'Опубликована')]

class Genre(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, unique=True, verbose_name="Заголовок")
    content = models.TextField(null=True, blank=True, verbose_name="Контент")

    def __str__(self):
        return f'{self.id}. {self.title}'

    class Meta:
        db_table = 'genres'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="Автор")
    content = models.TextField(null=False, blank=False, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    status = models.CharField(max_length=15, choices=status_choices, default=status_choices[0][0], verbose_name='Статус')
    genre = models.ForeignKey('webapp.Genre',
                              null=True,
                              on_delete=models.RESTRICT,
                              related_name='articles', # article_set
                              verbose_name='Жанр')

    def __str__(self):
        return f'{self.id}. {self.title}'

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

