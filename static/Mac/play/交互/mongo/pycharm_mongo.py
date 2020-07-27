import pymongo
class Solution:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['li']
        self.collection = self.db['s1']

    def find(self,fd=True):
        if fd:
            print(self.collection.find_one())
        else:
            for i in self.collection.find():
                print(i)

    def insert(self,data,fd=True):
        if fd:
            self.collection.insert_one(data)
        else:
            self.collection.insert_many(data)

    def updata(self,data,Ndata,fd=True):
        if fd:
            self.collection.update_one(data,{'$set':Ndata})
        else:
            self.collection.update_many(data,{'$set':Ndata})

    def remove_delete(self,data,fd=True):
        if fd:
            self.collection.delete_one(data)
        else:
            self.collection.delete_many(data)

    def s_sort(self,data,fd=True):
        if fd:
            for i in self.collection.find().sort(data):
                print(i)
        else:
            for i in self.collection.find().sort(data,-1):
                print(i)
s=Solution()
# s.insert({'_id':3,'name':'xiaoming','age':18},fd=True)
# a2=[{'_id':4,'name':'qq','age':22},
#     {'_id':5,'name':'qw','age':20},
#     {'_id':6,'name':'qe','age':18}]
# s.insert(a2,fd=False)
# s.updata({'name':'qq'},{'age':18},fd=True)
# s.updata({'age':18},{'name':'li'},fd=False)
# s.remove_delete({'name':'li'},fd=True)
# s.remove_delete({},fd=False)
s.s_sort('age',fd=True)
s.s_sort('age',fd=False)
s.find(fd=True)
s.find(fd=False)