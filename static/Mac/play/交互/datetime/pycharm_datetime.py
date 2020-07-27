import time
time.sleep(0)
#时间戳
# print(time.time())
import datetime
# print('最小日期：{}'.format(datetime.date.min))
# print('最大日期：{}'.format(datetime.date.max))
# now_time = datetime.datetime.now().strftime('%F %T')
# print('当前时间为：' + now_time)
print('当前时间为：' + datetime.datetime.now().strftime('%F %T'))
# print(type(now_time))
# a=datetime.datetime.now()
# print(type(a))
# from datetime import datetime


# my_date=datetime.date(2016,8,10)
# print(type(my_date))
# my_time=datetime.time(12,43,23)
# print(type(my_time))



# n=datetime.datetime(2019,1,1,23,24,45)
n=datetime.datetime.now()
# print(n)

# # 日期时间----时间戳
# my_stamp=datetime.datetime.timestamp(a)#日期时间转时间戳
# my_stamp=datetime.datetime.timestamp(n)#日期时间转时间戳
# print(my_stamp)
# my_date=datetime.datetime.fromtimestamp(my_stamp)#时间戳转为日期时间对象
# print(my_date)


# #日期时间----字符串
# aa=n.strftime('%Y-%m-%d-%H-%M-%S')#日期时间转为字符串
# print(aa)
# bb=datetime.datetime.strptime(aa,'%Y-%m-%d-%H-%M-%S')#字符串转日期时间对象
# print(bb)

#时间计算
# na=datetime.timedelta(days=1,
#                 minutes=0, hours=0)
# print(n)
# print(na)
# print(n+na)




def print_age():
    year =input('Enter your age (Y M D)Separated by spaces: ')
    try:
     year = [int(i) for i in year.split()]
     birth_data = datetime.date(year[0], year[1], year[2])
     today = birth_data.today()
     print(today)
     time_diff = today - birth_data
     print(time_diff)
     print(time_diff.days)
     print('Your age is: {} year and {} days ,Alive time：{}'. format(
      time_diff.days // 365, time_diff.days % 365,time_diff.days))
    except :
        print('Please use the format Y M D')
print_age()

