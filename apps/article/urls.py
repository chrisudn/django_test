from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('detail/', views.detail),
    path('addArticle/', views.addArticle),
    path('author/', views.get_author),
    path('author_model/', views.author_model),
    path('category/', views.get_category),
    path('category_model/', views.category_model),
    path('info_model/', views.info_model),
    path('indexView/', views.indexView.as_view()),
    path('indexTpView/', views.indexTpView.as_view()),
    path('indexListView/', views.indexListView.as_view()),
    path('indexDetailView/<int:pk>/', views.indexDetalView.as_view()),
    
    #透過這樣傳遞變數進去 
    path('test/<int:year>/<int:month>/<str:str>/<slug:slug>/',views.test),

    # API用的
    # path('articleapi/', views.ArticleView.as_view()),
]