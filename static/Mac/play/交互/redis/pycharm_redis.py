import redis
# class String:
#     print('～～～～～～～～～～～String类型～～～～～～～～～～～～～～～～～')
#     def __init__(self, db=2, decode_responses=False, host='127.0.0.1'):
#         self.a = redis.StrictRedis(host=host, decode_responses=decode_responses, db=db)
#     def set(self,*a,pd=True):
#         print('设置数据')
#         if pd:
#             self.a.set(*a)
#         else:
#             self.a.mset(*a)
#         # 创建多条：mset key1 value key2 key
#     def get(self,key,pd=True):
#         if pd:
#             print('key:{}-vaule:{}'.format(key,self.a.get(key)))
#         else:
#             pass
#         # 查看数据：get  key
#
#         # 查看多条：mget key2 key2 key3
#         print(self.a.keys())  # 查看db数据库里面所有的key
#         pass
#     def append(self):
#         self.a.append('a1',23)
#     def delete(self):
#         self.a.delete('a1')
# if __name__=='__main__':
#     str=String()
#     str.set('a1',21,pd=True)
#     # str.set(pd=False)
#     # str.get('a1',pd=True)

class List:
    print('～～～～～～～～～～～List类型～～～～～～～～～～～～～～～～～')
    def __init__(self,db=2,decode_responses=False,host='127.0.0.1'):
        self.a = redis.StrictRedis(host=host,decode_responses=decode_responses,db=db)
    def push(self,key,*data,pd=True):
        if pd:
            self.a.rpush(key,*data)
        else:
            self.a.lpush(key,*data)
    def get(self,key,start,stop,index,pd=True):
        if pd:
            print('key:{}个数为:{}'.format(key,self.a.llen(key)))
            print('key:{}-数据:{}'.format(key,self.a.lrange(key,start,stop)))
        else:
            print('key:{}   index:{}   value为:{}'
                  .format(key,index,self.a.lindex(key,index)))
    def set(self,key,index,value):
        print('key:{}  index:{}  修改成:{}  修改状态:{}'
              .format(key,index,value,self.a.lset(key,index,value)))
    def pop(self,key,count,value,pd):
        print('删除数据')
        if pd==0:
            print('指定删除')
            print('key:{}  pop个数:  {}  vaule:{}  修改状态:{}'
                  .format(key,count,value,self.a.lrem(key,count,value)))

        elif pd==1:
            print('头部删除')
            self.a.lpop(key)
        else:
            print('尾部删除')
            self.a.rpop(key)
if __name__=='__main__':
    l = List(decode_responses=True)
    # l.push('qw','h','3','qq',pd=True)
    # l.push('qw','q','1',pd=False)
    # l.set('qw',3,'chengzi')
    # l.pop('qw',4,'qq',0)
    # l.pop('qw',2,'qq',1)
    # l.pop('qw',2,'qq',2)
    l.get('qw', 0, 30, 0, pd=True)
    l.get('qw', 0, 30, 3, pd=False)

class Hash:
    print('～～～～～～～～～～～Hash类型～～～～～～～～～～～～～～～～～')
    def __init__(self):
        self.a = redis.StrictRedis(host='127.0.0.1',decode_responses=True,db=2)
    def hset(self,pd,name,key,values):
        if pd=='hset':
            self.a.hset(name,key,values)
        # elif pd=='hmset':
        #     self.a.hmset('h1',{'name':'qq','age':24})
    def hget(self,pd,name,*key,value):
        if pd=='hget':
            print(self.a.hget(name,key))  # 返回name值
        elif pd=='hgetall':
            print(self.a.hgetall(name))#返回值
        elif pd=='hmget':
            print(self.a.hmget(name,key,value))  # 取出值
        elif pd=='hvals':
            print(self.a.hvals(name))
        elif pd=='hkeys':
            print(self.a.hkeys(name))
    # def hdel(self):
    #     self.a.hdel()
# h=Hash()
# h.hset('hset','h1', 'name', 'aa')
# h.hget('hget','h1', 'name')

class Set():
    print('～～～～～～～～～～～Set类型～～～～～～～～～～～～～～～～～')
    def __init__(self):
        self.a = redis.StrictRedis(host='127.0.0.1',decode_responses=True,db=2)
    def sadd(self,key,*values):
        print('添加数据')
        self.a.sadd(key,*values)
    def smembers(self,key):
        print('key：{}   数据：{}'.format(key,self.a.smembers(key)))
    def pop(self,pd,key,*data):
        if pd=='spop':
            self.a.spop(key,*data)
        elif pd=='srem':
            self.a.srem(key,*data)
# set=Set()
# set.sadd('h1','name','aa')
# set.pop()
# set.smembers()

class Zset():
    print('～～～～～～～～～～～Sorted Set类型～～～～～～～～～～～～～～～～～')
    def __init__(self):
        self.a = redis.StrictRedis(host='127.0.0.1',decode_responses=True,db=2)
    def zadd(self,key,score,*member):
        self.a.zadd(key,score,*member)
    def zrange(self,key,start,stop,pd):
        if pd=='data':
            print('key{}：{}-{}   数据：{}'.format(key,start,stop,self.a.zrange(key,start,stop)))
        elif pd=='scores':
            print('key{}：{}-{}   数据：{}'.format(key, start, stop, self.a.zrange(key, start, stop)))
    def zrem(self,key,min,max,pd):
        if pd=='index':
            print('根据{}删除key:{}    状态[}'.format(pd,key,self.a.zrem(key,min,max)))
        elif pd=='scores':
            print('根据{}删除key：{}   状态{}'.format(pd,key,self.a.zremrangebyscore(key,min,max)))
# z=Zset()
# z.zadd('','',[{},{}])
# z.zrange('',0,20,'')
# z.zrem('','','','')