from django.db import models

from datetime import datetime


class Joke(models.Model):
    joke_id = models.IntegerField()
    joke_category = models.CharField(max_length=100, verbose_name='Категория')
    joke_start_data = models.DateTimeField(default=datetime.now(), null=True, verbose_name='Дата создания')
    joke_setup = models.CharField(max_length=200, verbose_name='Шутка')
    joke_punchline = models.CharField(max_length=100, verbose_name='Ответ')


class Entertainments(models.Model):
    start_data = models.DateTimeField(default=datetime.now(), verbose_name='Время и дата создания запроса.', null=True)
    category = models.CharField(max_length=100, verbose_name='Категория резвлечения.', null=True)
    entertainment = models.CharField(max_length=100, verbose_name='Развлечение.', null=True)
    participants = models.IntegerField(verbose_name='Количество участников.', null=True)
    price = models.FloatField(verbose_name='Цена.', null=True)
    accessibility = models.FloatField(verbose_name='Доступность.', null=True)
    entertainment_id = models.IntegerField(verbose_name='ID развлечения.', null=True)


class DogsPhoto(models.Model):
    start_data = models.DateTimeField(default=datetime.now(), null=True, verbose_name='Дата создания')
    link = models.URLField(verbose_name='Ссылка на фото', max_length=255, null=True, blank=True)
    status = models.CharField(verbose_name='Статус ответа', max_length=255)
