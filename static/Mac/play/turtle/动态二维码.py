from MyQR import myqr
import matplotlib.pyplot as plt
# 生成的二维码最终在你电脑的存储位置
# 当你使用了动态图作为背景，这里可以写成".gif"，保存出来的就是gif动态二维码！
save_name = '傻逼1.gif'
myqr.run(
    # 该链接表示你想要生成二维码的链接。
    words='https://blog.csdn.net/weixin_41261833',
    version=10,  # 容错率
    level='H',  # 纠错水平，范围是L、M、Q、H，从左到右依次升高
    colorized=True, # False为黑白
    contrast=1.5,  # 用以调节图片的对比度，1.0 表示原始图片。
    brightness=1.0,  # 用来调节图片的亮度。
    save_name=save_name,#存储的文件名
    # 背景图片的路径，你如果给的是".png/.jpg"等静态图片，最终生成的就是静态二维码！
    # 背景图片的路径，你如果给的是".gif"等动态图片，最终只需要保存为".gif"，生成的就是动态二维码！
    picture=r"G:\1Pycharm_Project\csdn分享系列\小猪佩奇的几个操作\动态.gif"
    )
# 查看生成的二维码图片
img = Image.open(save_name) # 读取所保存的图片展示二维码
plt.figure("Image") # 图像窗口名称
plt.imshow(img)
plt.axis('off') # 关掉坐标轴为 off
plt.show()