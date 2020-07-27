import pymongo
class Solution:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['li']  # 数据库名称
        self.collection = self.db['s1']  # 集合名称

    def find(self,fd=True):
        if fd:
            print('～～～～～这是第一条文档～～～～～')
            print(self.collection.find_one())
        else:
            print('～～～～～这是全部文档～～～～～')
            for i in self.collection.find():
                print(i)

    def insert(self,data,fd=True):
        if fd:
            print('～～～～～添加一条文档～～～～～')
            self.collection.insert_one(data)
        else:
            print('～～～～～添加多条文档～～～～～')
            self.collection.insert_many(data)

    def updata(self,data,Ndata,fd=True):
        if fd:
            print('～～～～～修改一条文档～～～～～')
            self.collection.update_one(data,{'$set':Ndata})
        else:
            print('～～～～～修改集合中所有满足条件的文档：～～～～～')
            self.collection.update_many(data,{'$set':Ndata})

    def remove_delete(self,data,fd=True):
        if fd:
            print('～～～～～删除集合中满足条件的所有文档～～～～～')
            self.collection.delete_one(data)
        else:
            print('～～～～～删除集合中所有的文档～～～～～')
            self.collection.delete_many(data)

    def s_sort(self,data,fd=True):
        if fd:
            print('～～～～～排序完成之后～～～～～')
            for i in self.collection.find().sort(data):
                print(i)
        else:
            print('～～～～～排序完成之后～～～～～')
            for i in self.collection.find().sort(data,-1):
                print(i)
s=Solution()
s.find(fd=False)#查找全部文档
s.s_sort('age',fd=True)#递增排序文档
s.s_sort('age',fd=False)#递减排序文档
# s.insert({'_id':3,'name':'xiaoming','age':18},fd=True)#添加一条文档
a2=[{'_id':4,'name':'qq','age':22},
    {'_id':5,'name':'qw','age':20},
    {'_id':6,'name':'qe','age':18}]
s.insert(a2,fd=False)#添加多条文档
s.find(fd=False)#查找全部文档
s.s_sort('age',fd=True)#递增排序文档
s.s_sort('age',fd=False)#递减排序文档
s.updata({'name':'qq'},{'age':18},fd=True)#修改一条文档
s.find(fd=False)#查找全部文档
s.s_sort('age',fd=True)#递增排序文档
s.s_sort('age',fd=False)#递减排序文档
s.updata({'age':18},{'name':'li'},fd=False)#修改集合中所有满足条件的文档
s.find(fd=False)#查找全部文档
s.s_sort('age',fd=True)#递增排序文档
s.s_sort('age',fd=False)#递减排序文档
# s.remove_delete({'name':'li'},fd=True)#删除集合中满足条件的所有文档
# s.find(fd=False)#查找全部文档
# s.remove_delete({},fd=False)#删除集合中所有的文档
s.find(fd=False)#查找全部文档
s.s_sort('age',fd=True)#递增排序文档
s.s_sort('age',fd=False)#递减排序文档
s.find(fd=True)#查找第一个文档
s.find(fd=False)#查找全部文档