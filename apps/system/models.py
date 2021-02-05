from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime
from stdimage.models import StdImageField
# from stdimage.utils import UploadToUUID

# Create your models here.
# 專題資訊
class Project(models.Model):
    name = models.CharField(max_length=100,verbose_name='專題名稱')
    code = models.CharField(max_length=100,verbose_name='專題代號_英文')
    text = models.CharField(max_length=200,verbose_name='專題簡介')
    image = StdImageField(max_length=100,                      
    upload_to='system/'+datetime.now().strftime('banner/%Y/%m'),
                                                     verbose_name="視覺圖",
                          variations={'thumbnail': {'width': 100, 'height': 75}},blank=True,null=True)
    create_time = models.DateTimeField(default=datetime.now, blank=True,verbose_name='創建時間')

    class Meta:
        db_table = ''
        managed = True
        verbose_name = '專題名稱'
        verbose_name_plural = '專題名稱s'

    def image_img(self):
        if self.image:
            return str('<img src="%s" />' % self.image.thumbnail.url)
        else:
            return u'upload picture'

        image_img.short_description ='Carousel image'
    image_img.allow_tags = True    

    def __str__(self):
        return self.name
        


# 專題系統介面資訊
class Message(models.Model):
    name = models.CharField(max_length=100,verbose_name='中文')
    name_eng = models.CharField(max_length=100,verbose_name='英文')
    project = models.ForeignKey('Project',on_delete=CASCADE)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = '專案系統介面資訊'
        verbose_name_plural = '專案系統介面資訊s'

    def __str__(self):
        return self.name





        



