import logging
# logging.basicConfig(filename='exam.log',level=logging.DEBUG)#放在文件 默认waring开始
# logging.basicConfig(format='日志级别：%(levelname)s\n'
#                            '日志时间：%(asctime)s、'
#                            '日志内容：%(message)s、'
#                            '日志器名称：%(name)s、'
#                            '调用日志记录函数的文件的全路径：%(pathname)s、'
#                            '调用日志记录函数的文件：%(filename)s、'
#                            '调用日志记录函数的函数名：%(funcName)s、'
#                            '调用日志记录函数的代码所在的行号：%(lineno)d\n',
#                     level=logging.DEBUG)
# logging.debug('This is a debug log')
# logging.info('This is a info log')
# logging.warning('This is a warning log')
# logging.error('This is a error log')
# logging.critical('This is a critical log')

# 日志记录器
logger=logging.getLogger('test')#创建对象过滤后剩下的名字
logger.setLevel(logging.DEBUG)#创建对象等级
#定义handlers日志处理器
sh=logging.StreamHandler()#在控制台输出
sh.setLevel(logging.DEBUG)#对象等级
fh=logging.FileHandler('test.log',encoding='utf-8')#在文件输出
fh.setLevel(logging.DEBUG)#对象等级

#Filters日志过滤器  定义对象logger=logging.getLogger('文件名字')
F=logging.Filter(name='test')#Filters日志过滤器#创建对象过滤后剩下的名字
F2=logging.Filter(name='test2')#创建对象过滤后剩下的名字
F3=logging.Filter(name='')##创建对象过滤后剩下的名字
sh.addFilter(F3)
fh.addFilter(F3)

#Handlers日志处理器：将记录的日志发送到指定的位置
logger.addHandler(sh)#hangler添加到logger创建对象里面
logger.addHandler(fh)#hangler添加到logger创建对象里面

#Formatter(日志控制器)用于控制日志信息的输出格式
fromatter=logging.Formatter('日志级别：%(levelname)s\n'
                           '日志时间：%(asctime)s \n'
                           '日志内容：%(message)s \n'
                           '日志器名称：%(name)s \n'
                           '调用日志记录函数的文件的全路径：%(pathname)s \n'
                           '调用日志记录函数的文件：%(filename)s \n'
                           '调用日志记录函数的函数名：%(funcName)s \n'
                           '调用日志记录函数的代码所在的行号：%(lineno)d\n',)#内容#级别、格式化输出
sh.setFormatter(fromatter)#控制台输出
fh.setFormatter(fromatter)#文件输出
try:
    a
except Exception as e:
    logger.error(e)