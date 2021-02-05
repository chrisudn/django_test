import xadmin
from apps.system.models import Project,Message

class ProjectXadmin(object):
    search_fields = ['name','code','text']
    list_display = ['name', 'image_img']
    model_icon = 'fa fa-flask'
    pass

class MessageXadmin(object):
    model_icon = 'fa fa-smile-o'
    pass


xadmin.site.register(Project,ProjectXadmin)
xadmin.site.register(Message,MessageXadmin)



