# 第一题https://www.somd5.com/
# import base64,hashlib
# def get_md5_value(str):
#     my_md5 = hashlib.md5()  # 获取一个MD5的加密算法对象
#     my_md5.update(str)  # 得到MD5消息摘要
#     hash = my_md5.hexdigest()  # 以16进制返回消息摘要，32位
#     return hash
# img_path = '/Users/li/Desktop/1.jpg'
# with open(img_path, 'rb') as f:
#     image_data = f.read()
#     base64_data = base64.b64encode(image_data)  # base64编码
# strs=str(base64_data)
# imgData = base64.b64decode(strs)
# md5 = get_md5_value(imgData)
# print('imgData：' + md5, len(md5))
#
# # 答案
# m = hashlib.md5()
# with open('/Users/li/Desktop/1.jpg', 'rb') as f:
#     for i in f:
#         m.update(i)
#     '''
#     m.update(f.read(i))
#     '''
# print(m.hexdigest())
# # 第二题
# import  pymysql
# connection = pymysql.connect(**{'host':'127.0.0.1','port':3306,'user': 'root','password': 'qwe123','db': 'student','charset': 'utf8'})
# cursor=connection.cursor()
# for i in range(10000):
#     cursor.execute("insert tb values(%s,'lanyu',30)"%i)
# # cursor.execute("insert tb values(10,'lanyu',30)")
# # cursor.execute("delete from tb where id=8")
# connection.commit()#提交事务（服务器在非事务回滚状态下传递）
# print(cursor.fetchmany(cursor.execute('select * from tb')))#获取表中全部数据结果
# cursor.close()#关闭游标
# connection.close()#关闭链接对象
# # 第三题
# import logging
# logger=logging.getLogger('test')#创建对象过滤后剩下的名字
# logger.setLevel(logging.DEBUG)#创建对象等级
# #定义handlers日志处理器
# sh=logging.StreamHandler()#在控制台输出
# sh.setLevel(logging.DEBUG)#对象等级
# fh=logging.FileHandler('test.log',encoding='utf-8')#在文件输出
# fh.setLevel(logging.DEBUG)#对象等级
# #Filters日志过滤器  定义对象logger=logging.getLogger('文件名字')
# F=logging.Filter(name='')##创建对象过滤后剩下的名字
# sh.addFilter(F)
# fh.addFilter(F)
# #Handlers日志处理器：将记录的日志发送到指定的位置
# logger.addHandler(sh)#hangler添加到logger创建对象里面
# logger.addHandler(fh)#hangler添加到logger创建对象里面
# #Formatter(日志控制器)用于控制日志信息的输出格式
# fromatter=logging.Formatter('日志时间：%(asctime)s \n'
#                            '日志级别：%(levelname)s\n'
#                            '日志内容：%(message)s \n'
#                            '调用日志记录函数的代码所在的行号：%(lineno)d\n',)#内容#级别、格式化输出
# sh.setFormatter(fromatter)#控制台输出
# fh.setFormatter(fromatter)#文件输出
# try:
#     a
# except Exception as e:
#     logger.error(e)
# # 第四题
import datetime
def print_inport():
    # input_date =input('Enter (Y M D H S)Separated by spaces: ')
    input_date='2019 10 31 20 00 30'
    sd='2019 12 25 00 00 00'
    try:
        input_date = [int(i) for i in input_date.split()]
        sd = [int(i) for i in sd.split()]
        c=datetime.datetime(input_date[0], input_date[1], input_date[2], input_date[3], input_date[4], input_date[5])
        print('输入日期为:',c)
        if input_date[1]==12 and input_date[2]==25:
            print('输入的日期就是输入日期当年的圣诞节哦')
        elif input_date[1]==12 and input_date[2]>25:
            a = datetime.datetime(input_date[0], input_date[1], input_date[2], input_date[3], input_date[4],
                                  input_date[5])
            b = datetime.datetime((input_date[0]+1), sd[1], sd[2], sd[3], sd[4], sd[5])
            print(b - a)
        elif input_date[1]<=12:
            a = datetime.datetime(input_date[0], input_date[1], input_date[2], input_date[3], input_date[4],
                                  input_date[5])
            b = datetime.datetime((input_date[0]), sd[1], sd[2], sd[3], sd[4], sd[5])
            print('距离圣诞节剩余',b - a)

# def get_days():
#     brithday=datetime.datetime.strptime(brith,'%Y-%m-%d')
#     now_birth=datetime.datetime(2020,12,25)
#     days=now_birth-brithday
#     print(days.days)
#
# brith=input('请输入时间：')
# get_days()



        # birth_data = datetime.date(input_date[0], input_date[1], input_date[2])
        # na = datetime.timedelta(days=1, seconds=4, minutes=3, hours=2)

        # print(time_diff)
        # print('Your age is: {} year and {} days ,Alive time：{}'. format(
        # time_diff.days // 365, time_diff.days % 365,time_diff.days))
    except :
        print('Please use the format Y M D')
print_inport()
'''
# MySQL：
# MySQL是一种关系型数据库管理系统，由于性能高、成本低、可靠性好，是最流行的开源数据库之一，
# 被广泛应用在互联网上的中小型网站中。可以运行于多个系统上，并且支持多种编程语言，包括C、C++、Python、Java、Perl、PHP、Ruby等
#
# Redis：
# 1. 不支持SQL语法
# NoSQL的世界中没有一种通用的语言，每种nosql数据库都有自己的语法，以及擅长的业务场景
# 2. 读写性能高
# NoSQL数据库都具有非常高的读写性，尤其是在海量数据下，它的表现非常优秀
#  3. 灵活的数据模型
# NoSQL的存储方式十分灵活，存储方式可以是JSON文档、键值对或者其他方式
# Redis是由意大利人开发的一款内存高速缓存数据库，是一个高性能的键值对存储数据库。
# Redis全称是Remote Dictionary Server(远程数据服务），使用C语言编写，并以内存作为数据存储介质，所以读写数据的效率极高。
# Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
# Redis不仅仅支持简单的key-value类型的数据，同时还把value分为list，set，zset，hash等数据结构存储。
# 因为Redis交换数据快，所以在服务器中常用来存储一些需要频繁调取的数据，提高效率。
#
# MonggoDB：
# 1、无模式
# 2、查询与索引方式灵活，是最像SQL的Nosql
# 3、支持复制集、主备、互为主备、自动分片等特性
#
#
#
# mongodb与关系型数据库相比的优缺点
# ①弱一致性（最终一致），更能保证用户的访问速度：
# 举例来说，在传统的关系型数据库中，一个COUNT类型的操作会锁定数据集，这样可以保证得到“当前”情况下的较精确值。
# 这在某些情况下，例 如通过ATM查看账户信息的时候很重要，但对于Wordnik来说，数据是不断更新和增长的，
# 这种“较精确”的保证几乎没有任何意义，反而会产生很大的延 迟。他们需要的是一个“大约”的数字以及更快的处理速度。
# 但某些情况下MongoDB会锁住数据库。如果此时正有数百个请求，则它们会堆积起来，造成许多问题。我们使用了下面的优化方式来避免锁定：
# 每次更新前，我们会先查询记录。查询操作会将对象放入内存，于是更新则会尽可能的迅速。在主/从部署方案中，从节点可以使用“-pretouch”参数运行，这也可以得到相同的效果。 
# 使用多个mongod进程。我们根据访问模式将数据库拆分成多个进程。 
# ②文档结构的存储方式，能够更便捷的获取数据。
# 对于一个层级式的数据结构来说，如果要将这样的数据使用扁平式的，表状的结构来保存数据，这无论是在查询还是获取数据时都十分困难。
# ③内置GridFS，支持大容量的存储。
#   GridFS是一个出色的分布式文件系统，可以支持海量的数据存储。
#   内置了GridFS了MongoDB，能够满足对大数据集的快速范围查询。
# ④内置Sharding。
# 提供基于Range的Auto Sharding机制：一个collection可按照记录的范围，分成若干个段，切分到不同的Shard上。
# Shards可以和复制结合，配合Replica sets能够实现Sharding+fail-over，不同的Shard之间可以负载均衡。
# 查询是对 客户端是透明的。客户端执行查询，统计，MapReduce等操作，这些会被MongoDB自动路由到后端的数据节点。
# 这让我们关注于自己的业务，适当的 时候可以无痛的升级。MongoDB的Sharding设计能力较大可支持约20 petabytes，足以支撑一般应用。
# 这可以保证MongoDB运行在便宜的PC服务器集群上。PC集群扩充起来非常方便并且成本很低，避免了“sharding”操作的复杂性和成本。
# ⑤第三方支持丰富。(这是与其他的NoSQL相比，MongoDB也具有的优势)
# 现在网络上的很多NoSQL开源数据库完全属于社区型的，没有官方支持，给使用者带来了很大的风险。
# 而开源文档数据库MongoDB背后有商业公司10gen为其提供供商业培训和支持。
# 而且MongoDB社区非常活跃，很多开发框架都迅速提供了对MongDB的支持。不少知名大公司和网站也在生产环境中使用MongoDB，越来越多的创新型企业转而使用MongoDB作为和Django，RoR来搭配的技术方案。
# ⑥性能优越：
# 在使用场合下，千万级别的文档对象，近10G的数据，对有索引的ID的查询不会比mysql慢，而对非索引字段的查询，则是全面胜出。
# mysql实际无法胜任大数据量下任意字段的查询，而mongodb的查询性能实在让人惊讶。
# 写入性能同样很令人满意，同样写入百万级别的数 据，mongodb比我以前试用过的couchdb要快得多，基本10分钟以下可以解决。补上一句，观察过程中mongodb都远算不上是CPU杀手。
#
#
# Mongodb与redis相比较：
# mongoDB 源码语言是C++,redis也是C或C++,
# mongodb 文件存储是BSON格式类似JSON，或自定义的二进制格式。
# mongodb与redis性能都很依赖内存的大小，mongodb 有丰富的数据表达、索引；最类似于关系数据库，支持丰富的查询语言，redis数据丰富，较少的IO ，这方面mongodb优势明显。
# mongodb不支持事物，靠客户端自身保证，redis支持事物，比较弱，仅能保证事物中的操作按顺序执行，这方面 redis优于mongodb。
# mongodb对海量数据的访问效率提升，redis 较小数据量的性能及运算,这方面 mongodb性能优于redis .monbgodb 有mapredurce功能，提供数据分析，redis 没有 ，这方面 mongodb优于redis 。
# '''