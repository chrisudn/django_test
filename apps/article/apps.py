from os import read
from django.apps import AppConfig


class ArticleConfig(AppConfig):
    name = 'apps.article'
    verbose_name = '文章列表'
