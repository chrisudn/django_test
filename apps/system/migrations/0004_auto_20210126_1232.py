# Generated by Django 3.1.4 on 2021-01-26 12:32

import datetime
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_message_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='banner/2021/01', verbose_name='Carousel'),
        ),
        migrations.AlterField(
            model_name='project',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='創建時間'),
        ),
    ]
