from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.article.models import Info
import json
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Info
        fields = ['name', 'sub_title','content','create_time','status','sort']