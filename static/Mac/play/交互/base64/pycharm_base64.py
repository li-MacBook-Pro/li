import base64
a="哈哈".encode()#进制
print(a)
b=base64.b64encode(a)#转为ASCII
print(b)
c=base64.b64decode(b)#ASCII转为进制
print(c)
#b16

url="www.baidu.com".encode()
print(url)
res=base64.urlsafe_b64encode(url)
print(res)
res_2=base64.urlsafe_b64decode(res)
print(res_2)