# Generated by Django 3.1.4 on 2021-01-28 18:42

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_author_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='content_rich',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', null=True, verbose_name='内容详情'),
        ),
    ]
