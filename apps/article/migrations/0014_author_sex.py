# Generated by Django 3.1.4 on 2021-01-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20210128_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='sex',
            field=models.CharField(choices=[('male', '男性'), ('female', '女性')], default='male', max_length=10),
        ),
    ]
