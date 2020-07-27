# a=[1,2,3,4,5,6]
# for i in a:
#     print(i)
#
# b=iter(a)
# while True:
#     try:
#         c=next(b)
#         print(c)
#     except StopIteration:
#         break
#

# class A:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.result = self.a
#         if self.result<30:
#             self.a, self.b = self.b, self.a + self.b
#             return self.result
#         else:
#             raise StopIteration
#
# u=A()
# # b=iter(u)
# for i in u:
#     print(i)

# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# def feibo():
#     a = 1
#     b = 2
#     while True:
#         result = a
#         a, b = b, a + b
#         yield result
# a=feibo()
# count=0
# while count<9:
#      b=next(a)
#      print(b)
#      count+=1
#
# def a():
#     n=1
#     n+=1
#     print(n)
#     yield n
#     n+=1
#     print(n)
# b=a()
# c=next(b)
# print(c)
# next(b)


# def a():
#     a=1
#     while True:
#         a+=1
#         b=yield a
#         print('bbbbb',b)
# c=a()
# next(c)
# count=0
# while count<5:
#     d=c.send(count)
#     print('ddddd',d)
#     count+=1
#



import time
def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print('[消费者]Consuming %s...'%n)
        time.sleep(1)
        r='200 ok'

def produce(c):
    next(c)
    n=0
    while n<5:
        n+=1
        print('[生产者]Producing %s...'%n)
        r=c.send(n)
        print('[生产者]Consumer return: %s...'%r)
    c.close()
c=consumer()
produce(c)