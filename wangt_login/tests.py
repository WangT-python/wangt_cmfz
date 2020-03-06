import os
import django
from django.test import TestCase
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wangt_cmfz.settings")
# Create your tests here.
django.setup()
from wangt_login.models import *

# User.objects.create(name="张三1", pwd="123456", gender=1, phone="12343256788", address="北京市海淀区张家坎1号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="张三2", pwd="123456", gender=1, phone="12343256787", address="北京市海淀区张家坎2号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="张三3", pwd="123456", gender=1, phone="12343256786", address="北京市海淀区张家坎3号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="张三4", pwd="123456", gender=1, phone="12343256785", address="北京市海淀区张家坎4号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="张三5", pwd="123456", gender=1, phone="12343256784", address="北京市海淀区张家坎5号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="张三6", pwd="123456", gender=1, phone="12343256783", address="北京市海淀区张家坎6号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="王晗1", pwd="123456", gender=0, phone="12343256783", address="上海市浦东开发区1号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="王晗2", pwd="123456", gender=0, phone="12343256784", address="上海市浦东开发区2号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="王晗3", pwd="123456", gender=0, phone="12343256785", address="上海市浦东开发区3号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="王晗4", pwd="123456", gender=0, phone="12343256786", address="上海市浦东开发区4号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="马汉1", pwd="123456", gender=1, phone="12343256776", address="辽宁省1号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="马汉2", pwd="123456", gender=1, phone="12343256766", address="辽宁省2号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="马汉3", pwd="123456", gender=1, phone="12343256756", address="辽宁省3号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="唐三1", pwd="123456", gender=1, phone="12343296756", address="四川省1号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="唐三2", pwd="123456", gender=1, phone="12343286756", address="四川省2号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="唐三3", pwd="123456", gender=1, phone="12343276756", address="四川省3号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="唐三4", pwd="123456", gender=1, phone="12343266756", address="四川省4号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
# User.objects.create(name="唐三5", pwd="123456", gender=1, phone="12343256756", address="四川省5号", head_img="/static/img/original.jpg", brief="痛苦就对了，舒服是留给死人的！")
