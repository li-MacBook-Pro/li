from MyQR import myqr
'''
words：二维码内容，链接或者句子
version：二维码大小，范围为[1,40]
level：二维码纠错级别，范围为{L,M,Q,H}，H为最高级，默认。
picture：自定义二维码背景图，支持格式为 .jpg，.png，.bmp，.gif，默认为黑白色
colorized：二维码背景颜色，默认为 False，即黑白色
contrast：对比度，值越高对比度越高，默认为 1.0
brightness：亮度，值越高亮度越高，默认为 1.0，值常和对比度相同
save_name：二维码名称，默认为 qrcode.png
save_dir：二维码路径，默认为程序工作路径
'''
# myqr.run(words='https://hao.360.com/')# 普通二维码
myqr.run(words='https://www.15e129bd0cee.com/index/home.html',# https://www.15e129bd0cee.com/index/home.html
         picture='5.jpg',
         save_name='qr1.png',
         colorized=True)# 图片二维码
# myqr.run(words='https://hao.360.com/',
#          picture='/Users/li/Desktop/181.gif',
#          save_name='qr4.gif',
#          save_dir="/Users/li/Desktop",
#          colorized=True)# 会动二维码