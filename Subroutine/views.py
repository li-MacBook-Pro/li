import datetime,pprint

from django.shortcuts import render, redirect, reverse

from django.http.response import HttpResponse, JsonResponse
from django_redis import get_redis_connection

rds=get_redis_connection('default')

# Create your views here.

def HTML_pb(requset):
    # pprint.pprint(requset.META)
    # print(requset.user)
    print(requset.method)# GET方法
    return render(requset, '瀑布流.html')

def func(request,name):
    # print(name)

    # print(request.POST['username'])
    # print(request.POST['password'])
    # ?username=17686520521&password=li19990929
    # print(request.GET['username'])
    # print(request.GET['password'])

    return HttpResponse(content="hello world")

def func_v0(request):
    # 当前版本转移新版本
    # url=reverse("v1")
    # redirect(url)
    # return redirect(url)
    return redirect(reverse("旧版本"))

def func_v1(request):
    return HttpResponse(content="新版本")

def re(request):
    return HttpResponse(content="re 正则匹配")

#～～～～～～～～～～模版～～～～～～～～～～～～～～～～
def hello():
    return 'django'
class Fruits:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def say(self):
        return 'HA'
ap=Fruits('apple','red')
ls = ['x', 'y', 'z']
dc = {'a': 1, 'b': 2}
def templstes_0(request):
    test = 'THIS IS A LIST!'
    return render(request, 'demo.html', context={
        'username': 'test',  # 字符串
        'foo': [i for i in range(10)],
        'hello': hello,  # 函数
        'fruits_say': ap.say,  # 方法
        'fruits': ap,  # 类对象
        'list': ls,  # 列表
        'dict': dc,  # 字典
        # ～～～～～～～～～～过滤器～～～～～～～～～～～～～～～～～～～～
        'test': test,
        'xx': '',
        'num1': 1,
        'num2': 2,
        # 'list':ls,
        'now': datetime.datetime.now,
        'html': '<h1>hello django</h1>',
        'float': 3.1415926,
    })

def templstes_1(request, username):
    name = request.GET['username']
    # password=request.GET['password']
    return render(request, 'demo_01.html', context={
        'username': name,
    })

def _json(request):
    dc = {
        'name': '李',
        'name1': 'li',
        'age': '18',
    }
    return JsonResponse(data=dc,json_dumps_params={
        # 'ensure_ascii': True,
        'ensure_ascii': False,
    })