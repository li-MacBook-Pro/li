from removebg import RemoveBg
import os

rmbg = RemoveBg("XKMh1J7geGfnGY9CFu9zXV8f", "error.log")

# 获取单个照片的抠图   XKMh1J7geGfnGY9CFu9zXV8f

rmbg.remove_background_from_img_file("/Users/li/PycharmProjects/li/练习/抠图/images/1.jpg")  # 图片地址

# 批量获取抠图信息
path = '%s/humanseg' % os.getcwd()
for pic in os.listdir(path):
  rmbg.remove_background_from_img_file("%s/%s" % (path, pic))