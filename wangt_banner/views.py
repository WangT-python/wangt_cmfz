import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from wangt_index.models import *

# Create your views here.

def get_dict(param: Banner):
    if isinstance(param, Banner):
        # print('get_dict', param)
        return {
            'id': param.id,
            'title': param.title,
            'status': param.status,
            'pic': str(param.pic),
            'time': str(param.creat_time).split(".")[0],
            'path': param.url
        }


# 轮播图列表
def show_banner(request):
    page_num = int(request.GET.get('page'))
    rows = int(request.GET.get('rows'))
    pics = Banner.objects.all()
    pagtor = Paginator(pics, per_page=rows)
    page = pagtor.page(page_num)
    data = {
        'page': page_num,
        'total': pagtor.num_pages,
        'records': pagtor.count,
        'rows': list(page.object_list),
    }
    json_str = json.dumps(data, skipkeys=True, ensure_ascii=False, default=get_dict)
    print(json_str)
    return HttpResponse(json_str)


# 添加轮播图
@csrf_exempt
def add_banner(request):
    title = request.POST.get("title")
    status = request.POST.get("status")
    pic = request.FILES.get("pic")
    print(title, status, pic, type(pic))
    pic_url = f'/static/img/{pic.name}'
    try:
        Banner.objects.create(title=title, status=status, pic=pic, url=pic_url)
    except:
        return HttpResponse('error')
    return HttpResponse("ok")

# 修改轮播图
def edit_banner(request):
    return HttpResponse()


# 删除轮播图
def del_banner(request):
    return HttpResponse()