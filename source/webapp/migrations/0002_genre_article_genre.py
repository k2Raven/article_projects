# Generated by Django 5.1.3 on 2024-11-28 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'db_table': 'genres',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='articles', to='webapp.genre', verbose_name='Жанр'),
        ),
    ]