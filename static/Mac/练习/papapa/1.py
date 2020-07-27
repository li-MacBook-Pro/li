import urllib.request as p
# data=urllib.request.urlopen('https://baidu.com/')
data=p.urlopen('http://baidu.com/')# 对地址发起请求
a=data.read()# 读取response对象里面的数据
b=p.urlopen('http://baidu.com/').read().decode()# bytes转成str
print(data)
print(a)
print(b)