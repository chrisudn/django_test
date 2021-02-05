"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from apps.article.forms import CategoryForm
from apps import article
from apps.article.apps import ArticleConfig
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.views.static import serve
import xadmin
from books.settings import MEDIA_ROOT
from apps.article.views import category_model, get_author, index,detail,indexView,indexTpView,indexListView,indexDetalView,addArticle,get_category,addCategory,author_model, info_model,ArticleView

from django.conf import settings
from django.conf.urls.static import static

from django.views import static ##新增
# from django.conf import settings ##新增
# from django.conf.urls import url ##新增

from rest_framework.authtoken import views

# 這邊的意思是 URL的路徑，ROUTER的概念，跟VIEWS底下的render指定的不同，那邊只的意思是，資料的結構
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('article/' , include('apps.article.urls')),
    # 下面這些就可以一進去apps.article裡面管理
    # path('article/', index,name='index'),
    # path('article/detail/', detail),
    # path('article/addArticle/', addArticle),
    # path('article/author/', get_author),
    # path('article/author_model/', author_model),
    # path('article/category/', get_category),
    # path('article/category_model/', category_model),
    # path('article/info_model/', info_model),
    # path('article/indexView/', indexView.as_view()),
    # path('article/indexTpView/', indexTpView.as_view()),
    # path('article/indexListView/', indexListView.as_view()),
    # path('article/indexDetailView/<int:pk>/', indexDetalView.as_view()),

    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    re_path('ueditor/', include('DjangoUeditor.urls')),
    # url(r'^ueditor/', include('DjangoUeditor.urls')),
    # url(r'^static/(?P<path>.*)$', static.serve,{'document_root': settings.STATIC_ROOT}, name='static'),
    re_path('static/(?P<path>.*)$', static.serve,{'document_root': settings.STATIC_ROOT}, name='static'),

    # API用的
    path('api/articleapi/', ArticleView.as_view()),
    path('api/articleapi/<int:sort>/<int:status>/', ArticleView.as_view()),
    
]
