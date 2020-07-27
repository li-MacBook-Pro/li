import base64
import cv2
import numpy
import hashlib

def get_md5_value(str):
    my_md5 = hashlib.md5()  # 获取一个MD5的加密算法对象
    my_md5.update(str)  # 得到MD5消息摘要
    hash = my_md5.hexdigest()  # 以16进制返回消息摘要，32位
    return hash
img_path = '/Users/li/Desktop/1.jpg'
with open(img_path, 'rb') as f:
    image_data = f.read()
    base64_data = base64.b64encode(image_data)  # base64编码
strs=str(base64_data)




imgData = base64.b64decode(strs)

md5 = get_md5_value(imgData)

print('imgData：' + md5, len(md5))


# nparr = numpy.fromstring(imgData,numpy.uint8)
# img_np = cv2.imdecode(nparr,1) #0是灰度 ，1 是彩色的
# cv2.imshow('image_name', img_np)  # 显示这个图
# cv2.waitKey(0)#等待键盘输入后
#
# name = '你好'
# file = open(name + '_' + md5 + '.jpg', 'wb')
# file.write(imgData)
# file.close()





# 第一题https://www.somd5.com/
import base64,hashlib
def get_md5_value(str):
    my_md5 = hashlib.md5()
    my_md5.update(str)
    hash = my_md5.hexdigest()
    return hash
with open('/Users/li/Desktop/1.jpg', 'rb') as f:
    image_data = f.read()
    base64_data = base64.b64encode(image_data)
strs=str(base64_data)
imgData = base64.b64decode(strs)
md5 = get_md5_value(imgData)
print(md5)
