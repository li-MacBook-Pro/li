# file=open('/Users/li/Desktop/1.txt','rb')
# content=file.read().decode('utf-8')
# print(content)
# content=file.read(2)
# file=open('/Users/li/Desktop/1.txt','a+')
# file.write('我希望世界和平')
# file.close()
#,encoding='utf-8'
# a='这是测试的字符串'
# print(a.encode(encoding='gbk'))
class Open:
    def __init__(self,file):
        self.file=file
    def __enter__(self):
        print('我开始了')
        self.f=open(self.file,'r')
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        print('我没了')
with Open('/Users/li/Desktop/1.txt') as F:
    a=F.read()
    print(a)

print('~~~~~~~~~~')

# import os
# print(os.getcwd())
# print(os.listdir('.'))
# print(os.chdir('.'))
# # os.remove(文件名)
# os.rename("oldname","new")
#
# import io
# sio = io.StringIO()