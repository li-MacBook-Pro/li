# 1、图像处理第一步：
# 首先我们所借助常用的OpenCV处理手段进行处理图片。首先进行的是图片二值化处理和创建结构元素，其中详细代码如下：
import cv2
import numpy as np
path = "13.jpg"
img = cv2.imread(path)
hight, width, depth = img.shape[0:3]
#图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))
#创建形状和尺寸的结构元素
kernel = np.ones((3, 3), np.uint8)

# 2、扩张修复区域：

# 识别到修复区域并根据相邻像素值进行扩张达到弥补像素值修复图片的效果。cv2.inpaint（）函数主要涉及两种算法。

# 一种算法是从该区域的边界开始，然后进入区域内，逐渐填充边界中的所有内容。
# 它需要在邻近的像素周围的一个小邻域进行修复。该像素由邻居中所有已知像素的归一化加权和代替。
# 选择权重是一个重要的问题。对于靠近该点的那些像素，靠近边界的法线和位于边界轮廓上的像素，给予更多的权重。

# 另一种是基于流体动力学并利用偏微分方程。基本原则是heurisitic。
# 它首先沿着已知区域的边缘行进到未知区域（因为边缘是连续的）。
# 它继续等照片（连接具有相同强度的点的线，就像轮廓连接具有相同高度的点一样），同时在修复区域的边界处匹配渐变矢量。
# 为此，使用来自流体动力学的一些方法。获得颜色后，填充颜色以减少该区域的最小差异。
#扩张待修复区域
hi_mask = cv2.dilate(thresh, kernel, iterations=1)
specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)
cv2.namedWindow("Image", 0)
cv2.resizeWindow("Image", int(width / 2), int(hight / 2))
cv2.imshow("Image", img)
cv2.namedWindow("newImage", 0)
cv2.resizeWindow("newImage", int(width / 2), int(hight / 2))
a=cv2.imshow("newImage", specular)
cv2.imwrite("43.jpg",specular)
cv2.waitKey(0)
cv2.destroyAllWindows()



# 修复程序处理二的搭建

# 1、图像处理第二步：

# 转换成hsv值，根据hsv值判断图片的前景和后景。HSV是一种将RGB色彩空间中的点在倒圆锥体中的表示方法。
# HSV即色相(Hue)、饱和度(Saturation)、明度(Value)，又称HSB(B即Brightness)。
# 色相是色彩的基本属性，就是平常说的颜色的名称，如红色、黄色等。
# 饱和度（S）是指色彩的纯度，越高色彩越纯，低则逐渐变灰，取0-100%的数值。明度（V），
# 取0-max(计算机中HSV取值范围和存储的长度有关)。HSV颜色空间可以用一个圆锥空间模型来描述。
# 圆锥的顶点处，V=0，H和S无定义，代表黑色。圆锥的顶面中心处V=max，S=0，H无定义，代表白色。
# 其中主要用到的函数是cv2库中的cv2.cvtColor()函数，
# 将RGB图像（在opencv中设计BGR图像）转换为HSV图像用到了参数cv2.COLOR_BGR2HSV。

import cv2
import os
import numpy as np
sta=0
for file in os.listdir("cut_test"):
    sta=sta+1
    print("正在处理"+"cut_test/" + file)
    img = cv2.imread("cut_test/" + file)
    #img=cv2.imread('1.jpg')
    rows,cols,channels = img.shape
    cropped = img[0:479, 0:cols]
    #转换hsv
    hsv=cv2.cvtColor(cropped,cv2.COLOR_BGR2HSV)
    # 图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
    thresh = cv2.inRange(hsv, np.array([90,10,125]), np.array([135,180,255]))
    erode = cv2.erode(thresh, None, iterations=2)
    dilate = cv2.dilate(erode, None, iterations=0)
    # 创建形状和尺寸的结构元素
    kernel = np.ones((3, 3), np.uint8)


# 2、图像修复：

# 在扩张修复区域的基础上外加调整像素值图片处理。

# 其中腐蚀操作详细如下：

# 定义了一个十字形结构元素 其实是一个矩阵，我们知道在图片的腐蚀过程，对图片的每个点，使用这个结构扫描每一个点，
# 用结构元素与其覆盖的二值图像做“与”操作,如果都为1，结果图像的该像素为1。
# 否则为0,腐蚀处理的结果是使原来的二值图像减小一圈。使用的函数：cv2.erode(img,kernel);

# 膨胀操作详细如下：

# 使用同样的结构，对图片的每个点，使用这个结构扫描每一个点，用结构元素与其覆盖的二值图像做“与”操作,如果出现1，结果图像的该像素为1。
# 否则为0,腐蚀处理的结果是使原来的二值图像扩大一圈。使用的函数：cv2.dilate(img,kernel)

# 扩张待修复区域
    hi_mask = cv2.dilate(dilate, kernel, iterations=1)
    specular = cv2.inpaint(cropped, hi_mask, -5, flags=cv2.INPAINT_NS)
    #合并
    htich = np.vstack((specular, img[479:rows, 0:cols]))
    '''
    blue=[]
    #获取mask,调整lower中h控制颜色
    lower_blue=np.array([90,10,125])
    upper_blue=np.array([135,180,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    erode=cv2.erode(mask,None,iterations=1)
    dilate=cv2.dilate(erode,None,iterations=1)
    #腐蚀膨胀
    erode=cv2.erode(mask,None,iterations=1)
    cv2.imshow('erode',erode)
    dilate=cv2.dilate(erode,None,iterations=1)
    cv2.imshow('dilate',dilate)
    for i in range(rows):
        for j in range(cols):
            if dilate[i,j]==255:
                blue.append([i,j])
    for w in blue:
        x=w[0]
        y=w[1]
        img[x,y]=[255,255,255]
    '''
    cv2.imwrite("dels_test/" + str(sta) + ".jpg", htich)
'''
    cv2.imshow('Mask', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''