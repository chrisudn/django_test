from django.shortcuts import get_object_or_404, render
from django import views,forms
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.db import models, reset_queries
from apps.article.models import Info,Category,Author
from django.views.generic.base import View, TemplateView
from django.views.generic import ListView,DetailView

from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets
from apps.article.serializers import ArticleSerializer 
from apps.article.models import Info

from django.http import Http404



from pprint import pprint
# Create your views here.

def index(request):
    # data = {'title':'這是文章標題','content':'這是文章內容'}
    # 這邊從MODEL，做SQL的語法把資料去來
    # contxt = Info.objects.using('second').all()
    contxt = Info.objects.all()
    # 用DICT組好資料
    data = {
        'contxt' : contxt,
        'test' : '這是一個單筆測試資料'
    }
    pprint(data)
    # 傳資料給頁面
    # 這邊指向的的路徑，是整個專案的資料結構
    return render(request,'article/index.html',data)

def detail(request):
    data = {'content':'一堆詳細內容','date':'2021-01-25'}
    if request.GET:
        pprint(request.GET)
        request.GET.get('article_id')
        data['article_id'] = request.GET.get('article_id')
        pprint(request.GET.get('article_id'))
    pprint(data)
    return render(request,'article/detail.html',data)   

def addArticle(request):
    # save 多DB寫入測試
    # new_article = Info(name='test2',category_id = 1,flag_id=1)
    # new_article.save(using='second')
    # return render(request,'article/index.html')
    MyInfo  = Info()
    MyInfo.name = 'save GOOD'
    MyInfo.category_id = 1
    MyInfo.flag_id = 1
    # MyInfo.save(using='second')
    MyInfo.save()
    return render(request,'article/index.html')

def addCategory(request):
    MyCategory = Category()
    MyCategory.name = '測試新增'
    MyCategory.project_id = 1
    MyCategory.save()
    return render(request,'article/index.html')


# 練習 CBV  View TemplateView ListView DetialView
# 繼承view之後，get post....都可以分開方法寫，可以比較簡潔清晰
class indexView(View):
    
    def get(self, request, *args, **kwargs):
       
        return render(request,'article/indexView.html')

    def post(self, request, *args, **kwargs):
       
        return render(request,'article/indexView.html')    

    def push(self, request, *args, **kwargs):
       
        return render(request,'article/indexView.html')        
    
#TemplateView  一般用在不用傳遞資料的靜態頁面，當工作做完，呈現的頁面，比如公司簡介，關於我們，這種|當然他也可以傳資料進去
class indexTpView(TemplateView):
    template_name  = 'article/indexTpView.html'

    def get_context_data(self, **kwargs):
        context = super(indexTpView,self).get_context_data(**kwargs)
        context["phone"] = '0937606870'
        pprint(context)
        return context

# ListView 用這個就不用自己拉資料這樣複雜拉。
class indexListView(ListView):
    # 一定要給他MODEL
    model = Info
    template_name = 'article/indexListView.html'
    # 這樣就可以把資料傳給頁面了
    context_object_name = 'Info'  

    # 這方法用來QUERY資料
    def get_queryset(self):
        return Info.objects.filter(status = 0)

    # 這方法用來傳非本MODEL的資料，或是一些靜態的資資料
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["con"] = '-----這是一個靜態的文字傳過來----' 
        return context             

# DetailView  3.1版只要在urls 裡面加上<int:pk> 就可以帶入變數拉
class indexDetalView(DetailView):
    model = Info
    template_name = 'article/indexDetailView.html'
    context_object_name = 'Info'

    def get_queryset(self):
        return Info.objects.filter(status = 0)   

    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset=queryset)
    #     pprint(obj.name)
    #     if obj.status != 0:
    #         raise Http404()
    #     return obj

from .forms import CategoryForm,AuthorForm,AuthorModelForm, CategoryModelForm, InfoModeForm
def get_category(request):
    if request.method == 'POST':
        form =  CategoryForm(request.POST)
        if form.is_valid():
            # 驗證通過再寫入，寫入要自己實現
            myCategory = Category()
            myCategory.name = form.cleaned_data['name']
            myCategory.project = form.cleaned_data['project']
            myCategory.save()
            pprint('寫入')
            # return HttpResponseRedirect('/article/')
    else:
        form = CategoryForm()

    return render(request,'article/category.html',{'form':form}) 

def get_author(request):
    if request.POST:
        # Form物件本身不會寫入，他的目的只是讓你產生表單，和幫你驗證
        myform = AuthorForm(request.POST)
        if myform.is_valid():
            # 驗證通過再寫入，寫入要自己實現
            name = myform.cleaned_data['name']
            sex = myform.cleaned_data['sex']
            myAuthor = Author()
            myAuthor.name = name
            myAuthor.sex = sex
            myAuthor.save()

            pprint('寫入')

    else:
        myform = AuthorForm()

    return render(request,'article/author.html',{'form':myform})

def category_model(request):
    form = CategoryModelForm()

    if request.POST: 
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}  
    return render(request,'article/category_model.html',context)      

def author_model(request):
    form = AuthorModelForm()
    
    if request.POST:
        form = AuthorModelForm(request.POST)
        if form.is_valid:
            form.save()
    
    context = {
        'form':form
    }

    return render(request,'article/author_model.html',context)

def info_model(request):
    form = InfoModeForm()

    if request.POST:
        form = InfoModeForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            print("寫入")

    context = {'form':form}
    return render(request,'article/info_model.html',context)            


     
def test(request,year,month,str,slug):
    pprint(year)
    pprint(month)
    context = {
        'data':{'year':year,'month':month,'str':str,'slug':slug}
    }
    return render(request,'article/test.html',context)

from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated  # <-- Here

from apps.log.models import Api
import socket
# API的部分
class ArticleView(GenericAPIView):
    queryset = Info.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) 

    def get(self, request, *args, **krgs):
        pprint(krgs)
        # pprint(krgs['sort'])
        # pprint(krgs['status'])
        users = Info.objects.filter(Q(sort = krgs['sort']) | Q(status = krgs['status']))
        # users = self.get_queryset()
        serializer = self.serializer_class(users, many=True)
        data = serializer.data
        # 寫入記錄一段LOG
        self.addLog(request)
        return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})

    def post(self, request, *args, **krgs):
        pprint(request.data)
        article = Info.objects.filter(Q(sort = request.data['sort']) | Q(status = request.data['status']))
        serializer = self.serializer_class(article, many=True)
        data = serializer.data
        # 寫入記錄一段LOG
        self.addLog(request)
        return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})

    def addLog(self,request):
        log = Api()
        log.user_id = 3
        log.ip = request.META['REMOTE_ADDR']
        pprint(request.META['REMOTE_ADDR'])
        # log.ip = socket.gethostbyname(socket.gethostname())
        # pprint(socket.gethostbyname(socket.gethostname()))
        log.save(using = 'mongodb')

    # def post(self, request, *args, **krgs):
    #     data = request.data
    #     try:
    #         serializer = self.serializer_class(data=data)
    #         serializer.is_valid(raise_exception=True)
    #         with transaction.atomic():
    #             serializer.save()
    #         data = serializer.data
    #     except Exception as e:
    #         data = {'error': str(e)}
    #     return JsonResponse(data)
    

