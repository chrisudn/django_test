from datetime import datetime

from django.core.checks.messages import INFO
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields import CharField, files
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelForm
from stdimage.models import StdImageField
from DjangoUeditor.models import UEditorField

from apps.system.models import Project

# Create your models here.

# 文章本身
class Info(models.Model):
    name = models.CharField(max_length=100,verbose_name='文章標題')
    sub_title = models.CharField(max_length=100,verbose_name='副標題')
    content = models.TextField(verbose_name='內文')
    content_rich = UEditorField(verbose_name='内容详情', width='100%', height=300, imagePath="content/ueditor/", filePath="content/ueditor/", default='',upload_settings={'imageMaxSizing': 1024000},toolbars='full',blank=True,null=True)
    create_time = models.DateTimeField(default=datetime.now, blank=True,verbose_name='創建時間')
    status = models.BooleanField(default=False,verbose_name='文章上下架')
    sort = models.IntegerField(verbose_name='排序',blank=True,null=True)
    category = models.ForeignKey('Category',on_delete=CASCADE,verbose_name='文章分類')
    flag = models.ForeignKey(Project,on_delete=CASCADE,verbose_name='專題分類')

    class Meta:
        # db_table = ''
        managed = True
        verbose_name = '文章列表'
        verbose_name_plural = '文章列表s'

    def __str__(self):
        return self.name

# 文章分類
class Category(models.Model):
    name = models.CharField(max_length=10,verbose_name='文章分類')
    project = models.ForeignKey(Project,on_delete=CASCADE,verbose_name='專案名稱')  

    class Meta:
        db_table = ''
        managed = True
        verbose_name = '文章分類'
        verbose_name_plural = '文章分類s'

    def __str__(self):
        return self.name

#相本圖片庫
class Album(models.Model):
    text = models.CharField(max_length=200,verbose_name='圖說')
    image = StdImageField(max_length=100,                      
    upload_to='system/'+datetime.now().strftime('photo/%Y/%m'),
                                                     verbose_name="視覺圖",
                          variations={'thumbnail': {'width': 100, 'height': 75}},blank=True,null=True)
    article = models.ForeignKey(Info,verbose_name='相關文章',on_delete=CASCADE,blank=True,null=True)                  
    # article = models.ManyToManyField('Info',verbose_name='相關文章')

    class Meta:
        managed = True
        verbose_name = '相本圖庫'
        verbose_name_plural = '相本圖庫s'

    def image_img(self):
        if self.image:
            return str('<img src="%s" />' % self.image.thumbnail.url)
        else:
            return u'upload picture'

        image_img.short_description ='Carousel image'
    image_img.allow_tags = True        

    def __str__(self):
        return self.text   

class Author(models.Model):
    GENDER = [
        ('male','男性'),
        ('female','女性')
    ]
    name = models.CharField(max_length=50,verbose_name='作者名稱')         
    sex = models.CharField(max_length=10,choices=GENDER,default='male')
    class Meta:
        db_table = ''
        managed = True
        verbose_name = '作者資料'
        verbose_name_plural = '作者資料s'


        
