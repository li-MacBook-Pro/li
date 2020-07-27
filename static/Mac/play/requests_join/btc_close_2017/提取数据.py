import json
import requests

# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# req = requests.get(json_url)
# 将数据写入文件￼ 
# with open('btc_close_2017_request.json','w') as f:
#     f.write(req.text)
# file_requests = req.json()


#提取相关数据

filename = 'btc_close_2017.json'# 将数据加载到一个列表中￼
with open(filename) as f:
    btc_data = json.load(f)
#提取相关数据
for btc_dict in btc_data:# 打印每一天的信息
    date = btc_dict['date']
    month = btc_dict['month']
    week = btc_dict['week']
    weekday = btc_dict['weekday']
    close = btc_dict['close']
    print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))
#将字符转换为数字
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))