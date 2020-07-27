from PIL import Image
im = Image.open("/Users/li/Desktop/1.jpg")
im.show()
def jiami(x):
    leng=len(bin(x).replace('0b',''))
    if leng==8:   #如果位数为8
        return int('0b'+(bin(x).replace('0b','')[::-1]),2)
    else:     #之所以用else ,因为要先变成8位二进制
        return int('0b'+((8-leng)*'0'+bin(x).replace('0b',''))[::-1],2)
from skimage import io
from numpy import *
x=io.imread("/Users/li/Desktop/1.jpg")#图片路径根据自己更改
io.imshow(x)
i,j,k=x.shape
y=uint8(zeros(x.shape))
for q in range(i):
    for w in range(j):
        for r in range(k):
            y[q,w,r]=jiami(x[q,w,r])
io.imshow(y)
io.imsave("/Users/li/Desktop/1.jpg",y)
i,j,k=y.shape
z=uint8(zeros(y.shape))
for q in range(i):
    for w in range(j):
        for r in range(k):
            z[q,w,r]=jiami(y[q,w,r])
io.imshow(z)
io.imsave("/Users/li/Desktop/1.jpg",z)