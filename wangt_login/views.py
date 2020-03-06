from django.http import HttpResponse
from django.shortcuts import render
from wangt_login.models import *
# Create your views here.


def my_dict(str):
    return str


# 用户列表
def show_user(request):
    users = User.objects.all()
    json_str = my_dict(users)
    return HttpResponse(json_str)


# 登录页面
def login(request):
    return render(request,)
