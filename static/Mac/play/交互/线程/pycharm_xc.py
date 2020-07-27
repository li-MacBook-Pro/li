import time,queue
from threading import Thread,Lock

'''线程'''
'''
def fun1():
    print(123)
    time.sleep(3)
    print(456)
def fun2():
    print(789)
    time.sleep(3)
    print(123)
'''

'''线程池'''
'''
my_list=list()
def Wdata():
    for i in range(5):
        my_list.append(i)
        time.sleep(1)
    print('写入数据',my_list)
def Rdata():
    print('读取数据',my_list) 
'''

'''竞争'''
'''
a,b=0,10000
lock=Lock()# 互斥锁，单任务执行
def jia():
    lock.acquire()# 加锁,一定要解锁
    for i in range(b):
        global a
        a+=1
    print('第一次：',a)
    lock.release()# 解锁
def jia2():
    lock.acquire()# 加锁,一定要解锁
    for i in range(b):
        global a
        a+=1
    print('第二次：',a)
    lock.release()# 解锁
'''

'''队列'''
'''
q=queue.Queue(20)# 队列长度
q.put(1)# 入队
print(q.get())# 出队
q.task_done()# 类似于标记，完成出队，多加会报错
q.put(2)# 入队
print(q.get())# 出队
q.task_done()# 类似于标记，完成出队，多加会报错
q.put(3)# 入队
print(q.get())# 出队
q.task_done()# 类似于标记，完成出队，多加会报错
q.put(4)# 入队
print(q.get())# 出队
q.task_done()# 类似于标记，完成出队，多加会报错
q.join()# 全部完成出队才能执行完毕
'''

'''线程池'''
'''
lock=Lock()# 互斥锁，单任务执行
def fun1(x):
    lock.acquire()  # 加锁,一定要解锁
    print('%s一'%x)
    # print(123)
    time.sleep(3)
    print(456)
    lock.release()  # 解锁
def fun2(x):
    lock.acquire()  # 加锁,一定要解锁
    print('%s二' % x)
    # print(789)
    time.sleep(3)
    print(123)
    lock.release()  # 解锁
'''

'''线程无序'''
'''
import threading,time
def task():
    time.sleep(0)
    print('当前线程名:',threading.current_thread().name)# 获取线程名字

'''

if __name__=='__main__':
    '''
    #参数说明Thread(target：表示调用对象，即子线程要执行的程序。name：子线程名称。args：传入target函数中位置参数，是一个元组，参数后必须加逗号。daemon=True 开启守护线程。）

    # 常用实例方法:
    # Thread.run(self)：线程启动时运行的方法，由该方法调用target参数指定的参数。
    # Thread.start(self)：启用进程，start方法就是去帮你调用run方法。
    # Thread.terminate(self)：强制终止进程。
    # Thread.join(self,timeout=None)阻塞调用，主线程进行等待。添加join子线程执行完毕，主线程执行。
    # Thread.setDaemon(self,daemonic)将子线程设置为守护线程。主程序调用完毕，程序运行完毕，子程序停止执行。
    # Thread.getName(self)获取线程名称
    # Thread.setName(self,name)设置线程名称
    '''
    '''线程'''
    '''
    f1=Thread(target=fun1)# 创建子线程
    f2=Thread(target=fun2)# 创建子线程
    # print(f1.getName())# 获取子线程名称
    # f1.setName('一')# 设置子线程名称
    # print(f1.getName())  # 获取子线程名称
    # print(f2.getName())# 获取子线程名称
    # f2.setName('二')# 设置子线程名称
    # print(f2.getName())  # 获取子线程名称
    f1.setDaemon(True)# 将子线程设置为守护线程
    f2.setDaemon(True)# 将子线程设置为守护线程
    f1.start()# 使用子线程，开启
    f2.start()# 使用子线程，开启
    f1.join()# 阻塞主线程
    f2.join()# 阻塞主线程
    '''
    '''线程池'''
    '''
    # 创建写数据的线程
    wd=Thread(target=Wdata)
    rd=Thread(target=Rdata)
    wd.start()
    wd.join()
    print('开始读取数据了')
    rd.start()
    '''
    '''竞争'''
    '''
    first = Thread(target=jia)
    second = Thread(target=jia2)
    first.start()
    # first.join()
    second.start()
    '''
    '''队列'''
    '''
    q=queue.Queue(20)# 队列长度
    q.put(1)# 入队
    print(q.get())# 出队
    q.task_done()# 类似于标记，完成出队，多加会报错
    q.put(2)# 入队
    print(q.get())# 出队
    q.task_done()# 类似于标记，完成出队，多加会报错
    q.put(3)# 入队
    print(q.get())# 出队
    q.task_done()# 类似于标记，完成出队，多加会报错
    q.put(4)# 入队
    print(q.get())# 出队
    q.task_done()# 类似于标记，完成出队，多加会报错
    q.join()# 全部完成出队才能执行完毕
    '''
    '''线程池'''
    '''
    f1 = Thread(target=fun1,args=(1,))  # 创建子线程
    f2 = Thread(target=fun2,args=(3,))  # 创建子线程
    # print(f1.getName())# 获取子线程名称
    # f1.setName('一')# 设置子线程名称
    # print(f1.getName())  # 获取子线程名称
    # print(f2.getName())# 获取子线程名称
    # f2.setName('二')# 设置子线程名称
    # print(f2.getName())  # 获取子线程名称
    f1.setDaemon(True)  # 将子线程设置为守护线程
    f2.setDaemon(True)  # 将子线程设置为守护线程
    f1.start()  # 使用子线程，开启
    f2.start()  # 使用子线程，开启
    f1.join()  # 阻塞主线程
    f2.join()  # 阻塞主线程
    '''
    '''线程无序'''
    '''
    for i in range(5):
        s1=threading.Thread(target=task)
        s1.start()
    '''



print('～～～～～～～～～～～～')