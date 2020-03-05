from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from utils.send_mess import YunPian
from wangt_cmfz import settings
from utils.random_code import generate_code

from redis import Redis
red = Redis(host='127.0.0.1',port=6379)    # 连接redis数据库


# 主页视图
def show_index(request):

    return render(request, 'wangt_index/index.html')


# 登录视图
def login(request):

    return render(request, 'login/login.html')


#验证手机号
import re
def check_phone(tel):
    ret = re.match(r"^1[3456789]\d{9}$", tel)
    if ret:
        return True
    else:
        return False


# 发送手机验证码
@csrf_exempt   # 该视图函数不需要进行csrf校验
def get_code(request):
    """
    根据前台用户的手机号为用户生成随机验证码并完成发送
    :param request: 用户手机号
    :return:    发送成功与否
    """

    mobile = request.POST.get('mobile')
    print(mobile)
    # 获取到手机号后需要对手机号进行基本的正则验证
    phone_status = check_phone(mobile)
    if not phone_status:
        # print("手机号格式错误")
        return HttpResponse("error")
    # 先根据手机号去redis比对手机号是否已经发送过短信以及时间戳是否满足再次发送的条件
    if red.get(mobile):
        print('验证码已存在',red.get(mobile))
        return HttpResponse('existe')

    # 根据获取到手机号去发送短信
    yunpian = YunPian(settings.APIKEY)
    code = generate_code(4)
    print(code)
    yunpian.send_message(mobile, code)
    print("发送成功")

    # 向redis中存入当前手机号与验证码及超时时间
    red.set(mobile, code, 60)  # 设置有效时长为60s

    return HttpResponse("ok")


# 登录逻辑
@csrf_exempt
def loginlogic(request):
    """
    校验用户登录信息的方法
    :param request:
    :return:    """
    mobile = request.POST.get('mobile')
    username = request.POST.get('username')
    code = request.POST.get('code')
    print(mobile, username, code)
    # 判断用户的验证码是否在有效期内
    if not red.get(mobile) or red.get(mobile) != code:
        return render(request, 'login/login.html')
    # 根据当前时间戳减去存入的时间戳，看是否超过规定时间，如果超过  则提示重新发送短信

    # 如果验证码在有效期内，判断用户输入的验证码与redis储存的验证码是否一致

    return redirect('wangt_index:index')