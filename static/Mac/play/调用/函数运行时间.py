import time
def run_time(func):
    def new_fun(*args,**kwargs):
        t0 = time.time()
        back = func(*args,**kwargs)
        print('函数运行的时间: %s'%(time.time() - t0))
        return back
    return new_fun