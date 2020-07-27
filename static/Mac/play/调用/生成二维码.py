import matplotlib.pyplot as plt
import barcode
from barcode.writer import ImageWriter
bar = barcode.get(u'code39', u"test123456",writer=ImageWriter())
output = bar.render(writer_options={"format": "PNG"}) #渲染生成图像对象
plt.imshow(output)
plt.axis('off')  # 不显示坐标轴
plt.show()
bar.save("11",options={"format": "JPEG"})#保存图形里有渲染然后保存到文件


name = barcode.generate(u'code128', u'test123456',writer=ImageWriter(), output='barcode_png')
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image
im = image.imread(name)  # 读取图片文件
plt.imshow(im)  # 显示图片
plt.axis('off')  # 不显示坐标轴
plt.show()
os.remove(name)