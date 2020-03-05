from django.urls import path
from wangt_index.views import *

app_name = 'wangt_index'
urlpatterns = [
    path('index/', show_index, name='index'),
    path('login/', login, name='login'),
    path('getcode/', get_code, name='getcode'),
    path('loginlogic/', loginlogic, name='loginlogic'),
]