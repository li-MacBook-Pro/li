import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares=[1,4,9,16,25]
plt.plot(input_values,squares,linewidth=1)# 绘制线条粗细

# 要删除数据点的轮廓，可在调用scatter()时传递实参edgecolor='none'。
# s=floct 点的大小
# 要修改数据点的颜色，可向scatter()传递参数c,c='red'。
# 还可以使用RGB颜色模式自定义颜色，可传递参数c，并将其设置为一个元组，其中包含三个0～1之间的小数值，它们分别表示红色、绿色和蓝色分量。值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅。
# 颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。c=y_values,cmap=plt.cm.Blues。请访问http://matplotlib.org/，单击Examples，向下滚动到Color Examples，再单击colormaps_reference。➡️https://matplotlib.org/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py


# 设置图表标题并给坐标轴加上标签￼ 
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)# 设置刻度标记的大小
plt.savefig('squares_plot.png', bbox_inches='tight')# 自动保存图表
plt.show()# 查看器