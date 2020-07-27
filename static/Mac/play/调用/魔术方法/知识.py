# # #初始化__init__
# # #析构  __del__  在删除之前的准备动作
# # #del  del.函数明    先出发__del__函数，再删除函数。
# # #__str__输出为字符串类型   return self.方法名   只能通过print触发    self.()
# # #__repr__专门用在交互式环境，返回一些相关信息给开发者看，通过直接调用类对象触发，
# # #   ！！！  __call__像函数一样调用
# #__new__开辟空间，给我们即将诞生对象的   cls只能在new用
# #单例模式
#
#
class Cat:
    def __init__(self, variety, weight, sex, age, name):
        self.variety = variety
        self.weight = weight
        self.sex = sex
        self.age = age
        self.name = name
        self.baian = ('{}在吗！本喵是{}可是困的的，不要随便打扰我睡觉啦！！！我可是一个{}，不要随便打听女孩子的年龄和体重呦，但是还是要偷偷的告诉你本喵今年{}啦，体重{}'.format(self.name,self.variety,self.sex,self.age,self.weight))
        self.xihuo = ('{}在吗！本喵是{}可是很忙的，不要随便打扰！！！本喵可是一个{}，今年{}，体重{}标准身材，不要迷恋本喵！'.format(self.name, self.variety, self.sex,self.age,self.weight))
    def __str__(self):
        return '本喵是{}。'.format(self.variety)
    def __repr__(self):
        if self.name=='白安':
            return self.baian
        elif self.name=='夕火':
            return self.xihuo
白安= Cat('英国短毛猫', '4KG', '淑女', '3岁', '白安')
夕火 = Cat('阿什拉', '20KG', '钢铁直男', '20岁', '夕火')

print(白安,夕火)
#
#
# # class A:
# #     def __new__(cls):
# #         return B
# #     def __init__(self):
# #         self.a='今天是上分的好日子'
# class A:
#     def __new__(cls):
#         if not hasattr(cls,'夕火'):
#             cls.夕火=super().__new__(cls)
#         return cls.夕火
#     def __init__(self):
#         self.a='今天是上分的好日子'
# s=A()
# m=A()
# print(id(s),id(m))
# # class B:
# #     def __init__(self):
# #         self.a=1
# # aa=A()
# # print(aa)
# # print(aa().a)
#
#
#
# #类属性和实例属性   self实例属性，其他都是类属性  他们之间没有任何关系,修改类属性会创建一个实例属性，cls只能在new用
# #if not hasattr
# # class A:
# #   ...:     a=2
# #   ...:     def __init__(self):
# #   ...:         self.b=3
# #   ...:
# # A.__dict__
# # Out[5]:
# # mappingproxy({'__module__': '__main__',
# #               'a': 2,
# #               '__init__': <function __main__.A.__init__(self)>,
# #               '__dict__': <attribute '__dict__' of 'A' objects>,
# #               '__weakref__': <attribute '__weakref__' of 'A' objects>,
# #               '__doc__': None})
# # aa=A()
# # aa.__dict__
# # Out[7]: {'b': 3}
# # aa.a
# # Out[8]: 2
# # aa.a=4
# # A.__dict__
# # Out[10]:
# # mappingproxy({'__module__': '__main__',
# #               'a': 2,
# #               '__init__': <function __main__.A.__init__(self)>,
# #               '__dict__': <attribute '__dict__' of 'A' objects>,
# #               '__weakref__': <attribute '__weakref__' of 'A' objects>,
# #               '__doc__': None})
# # aa.__dict__
# # Out[11]: {'b': 3, 'a': 4}
#
#
#
# class B(object):
#     instant = None
#     flag = True
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instant is None:
#             cls.instant = super().__new__(cls)
#         return cls.instant
#
#     def __init__(self,a,b):
#         if not B.flag:
#             return
#         self.name = '张三'
#         B.flag = False
#         print(self.name)
#         print('B已经被初始化了')
#
#
# d = B(3,2)
# print('d对象所在的内存地址是 %d, B类所在的内存地址是 %d' % (id(d), id(B)))
# e = B(2,3)
# print('e对象所在的内存地址是 %d, B类所在的内存地址是 %d' % (id(e), id(B)))
# f = B(1,1)
# print('f对象所在的内存地址是 %d, B类所在的内存地址是 %d' % (id(f), id(B)))
#
#
#
# class Foo:
#     def __init__(self):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         pass
#
# obj = Foo()
# # 执行type的 __call__ 方法，调用 Foo类（是type的对象）的 __new__方法，用于创建对象，然后调用 Foo类（是type的对象）的 __init__方法，用于对对象初始化。
#
# obj()    # 执行Foo的 __call__ 方法