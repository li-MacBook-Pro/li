#功能：对于某个特定函数，在不添加代码的情况下，为这个函数增加新的功能的东西，而这个东西就是另一个函数
# def b(func):#是函数的地址func  闭包
#     def c():
#         func()
#         print('这是装饰器')
#     return c
#
# @b
# def a():
#     print('这是一个a函数')
#
# a()#a()和b(a)()等价
# print('——————————————————————')
# b(a)()
# print('——————————————————————')
# b(a())
# print('——————————————————————')
# def d(func):
#     print('~~~111~~~~')
#     def c(n,m):
#         print('计算开始')
#         func(n,m)
#     return c
# @d
# def b(n,m):
#     print(m+n)

# b(1,2)
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# d(b)(1,2)
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# d(b(1,2))
# ~~~111~~~~
# 计算开始
# 3
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~111~~~~         #需要注释掉@
# 计算开始
# 计算开始
# 3
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 计算开始
# 3
# ~~~111~~~~

#
# def d(k):
#     print('这是%d'%k)
#     def c(func):
#         def a(n,m):
#             print('计算开始')
#             func(n,m)
#         return a
#     return c
#
# @d(k=4)
# def b(n,m):
#     print(m+n)
#
# b(1,2)
# d(k=4)(b)(1,2)#=c(b)()=a()


def check(func):
    def c():
        print('欢迎进去校园网请登录:')
        name=input('姓名')
        password=input('密码')
        name=name.strip()
        password=password.strip()
        tag=func(name,password)
        if tag==(0,1):
            print('欢迎进入学生信息系统')
        elif tag==(0,0)or tag==(1,0):
            print('账号密码不符合')
        elif tag==(1,1):
            print('欢迎进入教育')
        else:
            print('你怕是个外乡人')

    return c
@check
def login(name,password):
    a={'詹姆斯刘能':'123456','尼古拉斯赵四':'123456'}
    b={'霹雳无敌夕某人':'123456','冠绝古今夕某人':'123456'}
    if name in a:
        if a[name]==password:
            return (0,1)
        else:
            return (0,0)
    elif name in b:
        if b[name]==password:
            return (1,1)
        else:
            return (1,0)
    else:
        return False
login()






class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        areas = self.length * self.width
        return areas
@property  # 就像访问属性一样
def area(self):
    return self.width * self.length
@staticmethod
# 静态方法  和class类断开联系
def func():  	# self  在调用的时候会报错
    print('staticmethod func')
@classmethod  	# 类方法 
def show(cls):  	# cls 代表类本身 
    print(cls)
    print('show fun')


#查看函数运行时间：

import time
def run_time(func):
    def new_fun(*args,**kwargs):
        t0 = time.time()
        back = func(*args,**kwargs)
        print('函数运行的时间: %s'%(time.time() - t0))
        return back
    return new_fun