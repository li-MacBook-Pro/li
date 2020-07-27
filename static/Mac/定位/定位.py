# coding:utf8
'''
Created on 2016年6月14日
@author: zou
'''
import serial
import MySQLdb
import urllib2
import urllib
import httplib
import json
import time

ser = serial.Serial('COM4', 9600)


######################################################
def recv(serial):
    data = ''
    while True:
        tmp = serial.read(1)
        if tmp == '\n':
            break
        else:
            data += tmp

    return data


######################################################
def GetInfo(Str):
    info = []
    tmp = Str[7:]
    strs = ''
    for ch in tmp:
        if ch == '\n':
            return
        else:
            if ch == ',':
                info.append(strs)
                strs = ''
            else:
                strs = strs + ch

    return info


######################################################

def getYear(data):
    retdata = ''
    ret = ''
    tail = data
    # print tail
    tail = tail[::-1]
    # print tail
    count = 0
    for ch in tail:
        if count == 3:  # 616022
            if ch == ',':
                break
            else:
                ret += ch
        elif ch == ',':
            count = count + 1

    # print ret
    retdata += ret[1]
    retdata += ret[0]
    retdata += ret[3]
    retdata += ret[2]
    retdata += ret[5]
    retdata += ret[4]
    # print retdata
    return retdata


######################################################
def rightNum(strs, flag):
    ret = ''
    if cmp(flag, 't') == 0:
        # times      024335.00
        ret = strs[0:2]
        ret += ':'
        ret += strs[2:4]
        ret += ':'
        ret += strs[4:6]
    elif cmp(flag, 'l') == 0:  # latitude   3422.99947N
        if int(strs[0:3]) < 180:
            ret = strs[0:3]
            ret += '.'
            ret += strs[3:5]
            ret += strs[6:10]
        else:
            ret = strs[0:2]
            ret += '.'
            ret += strs[2:4]
            ret += strs[5:9]
    elif cmp(flag, 'L') == 0:  # longitude  10858.95306E
        if int(strs[0:3]) < 180:
            ret = strs[0:3]
            ret += '.'
            ret += strs[3:5]
            ret += strs[6:10]
        else:
            ret = strs[0:2]
            ret += '.'
            ret += strs[2:4]
            ret += strs[5:9]
    else:
        return None

    return ret


#########################################################
def Getlocation(db, ti, la, lo):
    # 发送http请求获取具体位置信息
    # import urllib
    url = 'http://api.map.baidu.com/geocoder/v2/'
    ak = 'ak=1aZ2PQG7OXlk9E41QPvB9WjEgq5WO8Do'
    # back='&callback=renderReverse&location='
    back = '&location='
    location = '34.992654,108.589507'
    output = '&output=json&pois=0'
    url = url + '?' + ak + back + location + output

    temp = urllib2.urlopen(url)
    hjson = json.loads(temp.read())
    locate = hjson["result"]["formatted_address"]  # 省，市，县
    # print locate
    mapinfo = hjson["result"]["sematic_description"]  # 详细描述
    # print mapinfo
    # 插入数据库
    cur = db.cursor()
    sql = "set names utf8"
    cur.execute(sql)
    info = []
    info.append(ti.encode('utf8'))
    info.append(locate.encode('utf8'))
    info.append(mapinfo.encode('utf8'))

    for val in info:
        print
        val

    sql = "insert into mapinfo values(%s,%s,%s)"
    try:
        cur.execute(sql, info)
    except:
        print
        'Insert mapinfo failed'


#########################################################
# mysql , 经度，维度
db = MySQLdb.connect('localhost', 'root', '', "zou", 3306, 'utf8')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS Location")
cursor.execute("DROP TABLE IF EXISTS mapinfo")

sql = """CREATE TABLE Location(
        Time CHAR(20),
        Latitude CHAR(15),
        Longitude CHAR(15),
        Altitude CHAR(10))"""
cursor.execute(sql)
sql = """CREATE TABLE mapinfo(
        time CHAR(20),
        local CHAR(100),
        info CHAR(100))"""
cursor.execute(sql)

'''
#mysql , 位置描述信息
#database = MySQLdb.connect('localhost','root','',"zou",3306)
#curkey = database.cursor()
#curkey.execute("DROP TABLE IF EXISTS mapinfo")
msql = """CREATE TABLE mapinfo(
        time CHAR(20),
        local CHAR(100),
        info CHAR(100))"""
curkey.execute(msql)
'''

##################################################################
Locat = []  ####
# 提取20项数据
count = 0
while count < 10:
    Info = []
    year = ''
    # 如果输出为 $GPGGA 开头，则这一行表示的是位置信息
    for val in range(0, 8):
        data = recv(ser)
        tmp = data[0:6]  # 截取前6个字符
        if cmp(tmp, '$GPRMC') == 0:
            # print data
            tmpyear = data[50:]
            year = getYear(tmpyear)
            # print year
        elif cmp(tmp, '$GPGGA') == 0:  # 条件满足的话就截取
            # print data
            Info = GetInfo(data)

    if Info == []:
        break
    value = []
    ti = year
    ti += '-'
    t = rightNum(Info[0], 't')
    ti += t
    # print ti
    value.append(ti)
    la = rightNum(Info[1], 'l')
    value.append(la)
    lo = rightNum(Info[3], 'L')
    value.append(lo)
    al = Info[8]
    value.append(al)
    # print value

    sql = "insert into Location values (%s,%s,%s,%s)"

    try:
        cursor.execute(sql, value)
        Getlocation(db, ti, la, lo)
        db.commit()
    except:
        print
        'insert error'

    count = count + 1
    # print count

db.close()
############################################################

# 关闭端口
ser.close()