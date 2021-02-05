import xadmin
from apps.article.models import Info,Category,Album,Author

# Register your models here.
class InfoXadmin(object):
    list_display = ('name','status','category','sort')
    list_editable = ('sort','status')
    # 注意這不能跨表搜尋，解決方法是有在要再帶入正確的跨表名稱__欄位名
    # https://blog.csdn.net/zhichuan0307/article/details/108349310
    search_fields = ['name']
    list_filter = ['status','flag_id','category']
    style_fields = {'content_rich': 'ueditor'}
    model_icon = 'fa fa-book'
    # pass

class CategoryXadmin(object):
    model_icon = 'fa fa-list'
    pass
class AlbumXadmin(object):
    list_display = ('text','image_img','article')
    list_filter = ['text','article']
    search_fields = ['text']
    model_icon = 'fa fa-list'
    pass

class AuthorXadmin(object):
    list_display = ('name','sex')
    list_editable = ('sex')
    pass


xadmin.site.register(Info,InfoXadmin)
xadmin.site.register(Category,CategoryXadmin)
xadmin.site.register(Album,AlbumXadmin)
xadmin.site.register(Author,AuthorXadmin)
