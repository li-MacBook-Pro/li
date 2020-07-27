# 可迭代对象
# 可通过for…in 进行遍历的数据类型包括 list,tuple, dict, set, str；以及生成器generator，及带yield的生成器函数
# 这些可直接作用于for循环的对象统称为可迭代对象：Iterable

# from collections import Iterable
# print(isinstance('abc',Iterable))
# print(isinstance((x for x in range(10)),Iterable))
# print(isinstance(100,Iterable))

# 迭代器
# Iterator，无限大数据流，内部定义__next__( )方法，返回下一个值的对象
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    print('done')


g = fib(5)
print(next(g))
next(g)
next(g)
next(g)
print(next(g))

g = fib(10)

for item in g:
    print(item)

g = fib(20)

while True:
    try:
        x = next(g)
        print('g: ', x)
    except StopIteration as e:
        print('Generation return value: ', e.value)
        break