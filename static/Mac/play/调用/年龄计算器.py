import datetime
'''年龄计算器'''

def print_age():
    year =input('Enter your age (Y M D)Separated by spaces: ')
    try:
     year = [int(i) for i in year.split()]
     birth_data = datetime.date(year[0], year[1], year[2])
     today = birth_data.today()
     time_diff = today - birth_data
     print('Your age is: {} year and {} days ,Alive time：{}'. format(
      time_diff.days // 365, time_diff.days % 365,time_diff.days))
    except :
        print('Please use the format Y M D')
print_age()

'''圣诞节计算器'''
'''
def print_time_difference(live,print_str):
    day=live.days
    time_=(live-datetime.timedelta(days=day)).seconds
    hour=time_//3600
    minute=(time_-3600*hour)//60
    second=time_-3600*hour-minute*60
    print(print_str+'{}天{}小时{}分{}秒。'.format(day,hour,minute,second))
def count_time_different(enter_day,way=4,flat=1):
    eyear=enter_day.year
    emonth=enter_day.month
    eday=enter_day.day
    if flat:
        print('输入日期为{}年{}月{}日'.format(eyear,emonth,eday))
        print('输入的时间为{}时{}分{}秒'.format(enter_day.hour,enter_day.minute,enter_day.second))
        if emonth==12 and eday==25:
            print('输入的日期刚好就是圣诞节哦！')
    if way==1:#  计算输入日期距离其上一次圣诞时间
        if emonth==12 and eday>25:
            last_christmas = datetime.datetime(eyear, 12, 25, 23, 59, 59, 999)
        else:
            last_christmas=datetime.datetime(eyear-1,12,25,23,59,59,999)
        last_time_difference=enter_day-last_christmas
        print_time_difference(last_time_difference,'距离其上一次圣诞节已经过去了')
    elif way==2:#  计算输入日期距离其下一次圣诞节的时间
        if emonth==12 and eday>=25:
            next_christmas=datetime.datetime(eyear+1,12,25,0,0,0,0)
        else:
            next_christmas=datetime.datetime(eyear,12,25,0,0,0,0)
        next_time_difference=next_christmas-enter_day
        print_time_difference(next_time_difference,'距离其下一次圣诞节还有')
    elif way==3:#  计算输入日期距离今年圣诞节的时间
        now=datetime.datetime.now()
        if eyear>now.year or (eyear==now.year and emonth==12 and eday>25):
            this_christmas=datetime.datetime(now.year,12,25,23,59,59,999)
            this_time_difference=enter_day-this_christmas
            print_time_difference(this_time_difference,'距离今年（{}年）的圣诞节已过去'.format(now.year))
        elif eyear==now.year and emonth==12 and eday==25:
            print('而且是今年的圣诞节！')
        else:
            this_christmas=datetime.datetime(now.year,12,25,0,0,0,0)
            this_time_difference=this_christmas-enter_day
            print_time_difference(this_time_difference,'距离今年（{}年）的圣诞节还有'.format(now.year))
    else:
        for i in range(1,4):
            count_time_different(enter_day,i,0)
if __name__ == '__main__':
    print('本程序用于计算某个特定时间距离圣诞节的时间差')
    print('请输入你需要计算的日期（格式：年-月-日 时：分：秒（24小时制）：')
    enter_day=1
    while enter_day:
        enter_day=input()# 直接回车退出
        try:
            enter_day = datetime.datetime.strptime(enter_day, '%Y-%m-%d %H:%M:%S')
            print(type(enter_day))
            count_time_different(enter_day)
        except:
            pass
'''