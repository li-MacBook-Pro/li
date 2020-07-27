import hashlib
#https://www.somd5.com/
#https://www.sojson.com/
print("哈哈".encode())#进制
h="哈哈"
hash_0=h.encode("utf-8")
print(hash_0)

hash_1=hashlib.md5()#更新
hash_1.digest()#更新
hash_1.hexdigest()#更新
print(hash_1)
print(hash_1.digest())
print(hash_1.hexdigest())#16进制解密

hash_2=hashlib.md5()#更新/保留原来的数据
hash_2.update(hash_0)#更新/保留原来的数据
hash_2.update(hash_0)#更新/保留原来的数据
print(hash_2)
print(hash_2.digest())
print(hash_2.hexdigest())#16进制解密

#第一种
result_1=hashlib.new('md5',"哈哈".encode())
print(result_1)
print(result_1.digest())
print(result_1.hexdigest())
#第二种
result_2=hashlib.md5("嘻嘻".encode())
print(result_2)
print(result_2.digest())
print(result_2.hexdigest())