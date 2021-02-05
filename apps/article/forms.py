from django import forms
from django.core.checks.messages import Info
from django.db.models import fields
from django.db.models.enums import Choices
from django.db.models.fields import CharField
from apps.article.models import Author, Category,Info
from apps.system.models import Project

# 我目前理解，有關聯性的TABLE沒法用這個吧!!!，為了證明這點，1.直接寫入看看，2.新建一個都沒有關聯的table
class CategoryForm(forms.Form):
    name = forms.CharField(max_length=10,label='文章分類')
    project = forms.ModelChoiceField(queryset=Project.objects.all())

# 結果 1.是可以的 (與始否是有外鍵無關)
# 結果 2.也是不行 (Form物件本身不提供寫入，要自己實現)
# 我猜應該是寫入格式有問題，這也太難找問題拉
# 我查到，如果要這樣處理有foreignKey的資料，要用ModelForm 因為ModelForm有save的方法
# 我理解了forms.Form 主要是用來產生表單，和驗證。至於寫入這件事情要另外寫入(真正的定義是這樣的)

class AuthorForm(forms.Form):
    GENDER = [
        ('male','男性'),
        ('female','女性')
    ]
    name = forms.CharField(max_length=50,label='作者名稱')  
    sex = forms.ChoiceField(label='作者性別',choices=GENDER)

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        # fields = ['name','sex']  
        fields = '__all__'  

class InfoModeForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__' 
  