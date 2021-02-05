# Generated by Django 3.1.4 on 2021-01-22 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='文章分類')),
            ],
            options={
                'verbose_name': '文章分類',
                'verbose_name_plural': '文章分類s',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='文章標題')),
                ('sub_title', models.CharField(max_length=100, verbose_name='副標題')),
                ('content', models.TextField(verbose_name='內文')),
                ('create_date', models.DateTimeField(verbose_name='創建時間')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.category', verbose_name='文章分類')),
            ],
            options={
                'verbose_name': '文章列表',
                'verbose_name_plural': '文章列表s',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='專題分類')),
            ],
            options={
                'verbose_name': '專題分類',
                'verbose_name_plural': '專題分類s',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='ArticleCategoryInfo',
        ),
        migrations.DeleteModel(
            name='ArticleInfo',
        ),
        migrations.AddField(
            model_name='info',
            name='flag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.project', verbose_name='專題分類'),
        ),
        migrations.AddField(
            model_name='category',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.project', verbose_name='專案名稱'),
        ),
    ]
