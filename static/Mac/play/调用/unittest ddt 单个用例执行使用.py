'''
由于需要单用例执行, 而 ddt使用后不支持,显示找不到该方法 `AttributeError: type object 'xxx'(类) has no attribute 'xxx'(方法)
查看ddt源码,
可知ddt 在使用传参后会对方法名重新定义 定义格式为: 源方法名+ 入参相关数据,所以添加的时候 把改了名字的方法名传入就可以实现了.
'''

# test_xxx.py
# test_xxx.py
import unittest

import ddt


@ddt.ddt
class MyTest01(unittest.TestCase):
    # @ddt.data(["a1","a2"],["b1","b2"])
    # def dataget(self,p1,p2):
    #     print("data:{}-{}".format(p1,p2))
    @ddt.data(["a5","a2"],["b1","b2"])
    @ddt.unpack
    def test_02_aa(self,p1,p2):
        print("test02: {}-{}".format(p1,p2))


    def test_01_aa(self):
        print("test01")

    def test_03_aa(self):
        print("test03")


def mySuitePrefixAdd(MyClass,cases):
    '''
    根据前缀添加测试用例-可用于ddt数据用例
    :param MyClass:
    :param cases:
    :return:
    '''
    test_list = []
    testdict = MyClass.__dict__
    if isinstance(cases,str):
        cases = [cases]
    for case in cases:
        tmp_cases = filter(lambda cs:cs.startswith(case) and callable(getattr(MyClass,cs)),testdict)
        for tmp_case in tmp_cases:
            test_list.append(MyClass(tmp_case))
    suite = unittest.TestSuite()
    suite.addTests(test_list)
    return suite


if __name__ == "__main__":

    runner = unittest.TextTestRunner()
    runner.run(mySuitePrefixAdd(MyTest01,"test_02_aa"))

'''而pycharm 实现右键选择用例执行, 在安装目录: helpers/pycharm/_xxxx_unittest_runner.py 解析分析 targets 参数,也可以实现'''
def targetsReBuild(targets):
    target_dir_path = os.getcwd().split("\\")[-1]
    if targets:
        target_path, target_class, target_method = targets[0].split(".")
    if target_path:
        target_module = __import__("{}.{}".format(target_dir_path,target_path))
        target_class_dir = eval("dir({}.{}.{})".format('target_module',target_path,target_class))
        target_path_dit = eval("dir({}.{})".format('target_module',target_path))
        # 解析targets

        if 'ddt' in target_path_dit: #使用了ddt
            target_collect = []
            # 有ddt则使用前缀匹配
            for target_index,target in enumerate(targets):
                target_path, target_class, target_method = target.split(".")
                tm = eval("{}.{}.{}".format('target_module',target_path,target_class))
                targets_tmp = filter(lambda cs:cs.startswith(target_method+"_") \
                                               and callable(getattr(tm,cs)),\
                                     target_class_dir)
                targets_tmp = list(targets_tmp)
                # 装换成list判断是否为空
                if targets_tmp:

                    for t in targets_tmp:
                        target_collect.append("{}.{}.{}".format(target_path,target_class,t))
                else:
                    target_collect.append("{}.{}.{}".format(target_path,target_class,target_method))
            # 扫描完成
            targets = target_collect
    return targets

if __name__ == '__main__':
    path, targets, additional_args = jb_start_tests()
    targets = targetsReBuild(targets) ###########在此处添加该方法

    args = ["python -m unittest"]
#其他不变