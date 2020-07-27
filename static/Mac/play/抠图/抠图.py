import os
import paddlehub as hub

# # 加载模型
# humanseg=hub.Module(name='deeplabv3p_xception65_humanseg')
# base_dir=os.path.abspath(os.path.dirname(__file__))
#
# # 获取当前文件目录
# path =os.path.join(base_dir,'images/')
# # 获取文件列表
# files=[path + i for i in os.listdir(path)]
# print(files)
# # 抠图
# results=humanseg.segmentation(data={'image':files})
# for result in results:
#     print(result)

# humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')
# base_dir = os.path.abspath(os.path.dirname(__file__))
# path = os.path.join(base_dir, 'images/')
# files = [path + i for i in os.listdir(path)]
# results = humanseg.segmentation(data={'image': files})

import sys

# 加载模型
# humanseg = hub.Module(name="deeplabv3p_xception65_humanseg")
#
# # 指定抠图图片目录
# path = 'images/'
# files = []
# dirs = os.listdir(path)
# for diretion in dirs:
#     files.append(path + diretion)
#
# # 抠图
# results = humanseg.segmentation(data={"image": files})

# for result in results:
#     print(result['origin'])
#     print(result['processed'])






# # 加载模型
humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')
base_dir = os.path.abspath(os.path.dirname(__file__))

# 获取当前文件目录
path = os.path.join(base_dir, 'images/')
# 获取文件列表
files = [path + i for i in os.listdir(path)]
print(files)
# 抠图
results = humanseg.segmentation(data={'image': files})
for result in results:
    print(result)

# humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')
# base_dir = os.path.abspath(os.path.dirname(__file__))
# path = os.path.join(base_dir, 'images/')
# files = [path + i for i in os.listdir(path)]
# results = humanseg.segmentation(data={'images': files})