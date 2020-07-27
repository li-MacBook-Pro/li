class A:
    def __init__(self):
        self.a=1
        self.b=2
    def __iter__(self):
        return self
    def __next__(self):
        self.result=self.a
        self.a,self.b=self.b,self.a+self.b

        return self.result
u=A()
b=iter(u)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))



class A:
    def __init__(self):
        self.a=1
        self.b=2
    def __iter__(self):
        return self
    def __next__(self):
        self.result = self.a
        if self.result<30:
            self.a, self.b = self.b, self.a + self.b
            return self.result
        else:
            raise StopIteration

u=A()
for i in u:
    print(i)



def feibo(n):
    a = 1
    b = 2
    while True:
        result = a
        if n > result:
            a, b = b, a + b
            c.append(result)
        else:
            break
c=[]
feibo(30)
print(c)

def feibo():
    a = 1
    b = 2
    while True:
        result = a
        a, b = b, a + b
        yield result
a=feibo()
count=0
while count<9:
     b=next(a)
     print(b)
     count+=1


def a():
    a=1
    while True:
        a+=1
        b=yield a
        print('bbbbb',b)
c=a()
next(c)
count=0
while count<5:
    d=c.send(count)
    print('ddddd',d)
    count+=1