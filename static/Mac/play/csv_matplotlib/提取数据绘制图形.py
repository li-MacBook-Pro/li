import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期、最高气温和最低气温￼
# filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)# reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中。
    header_row = next(reader)
    #一
    # for index, column_header in enumerate(header_row):# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
    #     print(index, column_header)
    #highs = []
    # 二
    # for row in reader:
    #     highs.append(row[1])
    #highs = []
    # 三
    # dates, highs = [], []
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")# 我们将包含日期信息的数据（row[0]）转换为datetime对象
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
# 根据数据绘制图形￼
fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(highs, c='red')# 将最高气温列表传给plot()
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
# 设置图形的格式
# plt.title("Daily high temperatures, July 2014", fontsize=24)# 并传递c='red'以便将数据点绘制为红色（红色显示最高气温，蓝色显示最低气温）。接下来，我们设置了一些其他的格式，如字体大小和标签
plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # 我们调用了fig.autofmt_xdate()来绘制斜的日期标签，以免它们彼此重叠。
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.show()