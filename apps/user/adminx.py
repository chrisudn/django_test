import xadmin
from xadmin import views

class GlobalSetting(object):
    site_title ="專題後台上稿系統"
    site_footer ="新聞部 數據中心"
    # menu_style ="accordion"



xadmin.site.register(views.CommAdminView,GlobalSetting)




