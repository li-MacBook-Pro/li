from multiprocessing.pool import ThreadPool
import time
from threading import Thread,Lock
from queue import Queue
'''内置线程池'''
'''
lock=Lock()# 互斥锁，单任务执行
def fun1(x,y):
    # lock.acquire()  # 加锁,一定要解锁
    print('%s好好学习'%x)
    # print(123)
    time.sleep(3)
    print('天天向上')
    # lock.release()  # 解锁
def fun2(x):
    # lock.acquire()  # 加锁,一定要解锁
    print('%shello' % x)
    # print(789)
    time.sleep(3)
    print('world')
    # lock.release()  # 解锁
def p1():
    time.sleep(1)
    print('时间')
    pool.terminate()# 终止线程，时间到了之后，等线程结束之后再关闭
pool=ThreadPool(9)# 创建线程数量
pool.apply_async(fun1,args=(1,2,))# 添加任务
pool.apply_async(p1)
pool.apply_async(fun2,args=(3,))# 添加任务
pool.apply_async(fun1,args=(2,2,))# 添加任务
pool.apply_async(fun2,args=(4,))# 添加任务
pool.close()# 关闭任务，自带阻塞线程
# pool.terminate()# 终止线程，线程运行完成时结束，类似于循环break，线程不能被终止，只能等待线程执行完毕。
pool.join()
print('这是最后一行')
'''
'''自定义线程池'''
''''''
class TPool:
    def __init__(self,n):# n线程数
        self.queen=Queue()# 定义队列/任务长度
        Thread(target=self.worker,daemon=True).start()# 工作 daemon=True 开启守护线程
        # for i in range(n):
        #     Thread(target=self.worker, daemon=True).start()  # 工作 daemon=True 开启守护线程
    def worker(self):# 工作
        while True:
            func,args,kwargs=self.queen.get()# 取任务
            func(*args,**kwargs)# 拆包，执行函数
            self.queen.task_done()# 确认/标记任务完成
    def apply_async(self,targer,args=(),kwargs={}):# 接收任务
        self.queen.put(targer,args,kwargs)# 入队
    def join(self):# 阻塞
        self.queen.join()# 队列

def funb(x):
    print('%s好好学习'%x)
    time.sleep(3)
    print('天天向上')

tp=ThreadPool(2)   # 创建线程数量
tp.apply_async(funb,args=(2,))# 添加任务
# for i in range(10):
#     tp.apply_async(funb, args=(2,))  # 添加任务
tp.close()
tp.join()


''''''