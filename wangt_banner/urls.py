from django.urls import path
from wangt_banner.views import *

app_name = 'wangt_banner'
urlpatterns = [
    path('add_banner/', add_banner, name='add_banner'),
    path('show_banner/', show_banner, name='show_banner'),
    path('edit_banner/', edit_banner, name='edit_banner'),
    path('del_banner/', del_banner, name='del_banner'),

]