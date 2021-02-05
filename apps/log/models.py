from datetime import datetime
from djongo import models

# Create your models here.

class Api(models.Model):
    user_id = models.IntegerField(verbose_name='API KEY ID')
    create_time = models.DateTimeField(default=datetime.now, blank=True,verbose_name='創建時間')
    ip = models.CharField(max_length=100,verbose_name='IP來源')

    class Meta:
        managed = True
        verbose_name = 'API LOG'
        verbose_name_plural = 'API LOG'

    def __str__(self):
        return self.user_id     
