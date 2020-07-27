import  pymysql
connection = pymysql.connect(**{'host':'127.0.0.1','port':3306,'user': 'root','password': 'qwe123','db': 'student','charset': 'utf8'})

cursor=connection.cursor()#创建游标对象
# print(cursor)#打印游标位置

# #执行SQL语句
print(cursor.execute('select * from tb'))#查询语句
# print(cursor.execute("insert tb values(5,'bb',6)"))#插入数据提交事务操作
# print(cursor.execute("delete from tb where id=5"))#删除数据提交事务操作

# connection.commit()#提交事务（服务器在非事务回滚状态下传递）

#获取数据
print(cursor.fetchall())#获取表中全部数据结果
# print(cursor.fetchone())#显示表中一条数据
# print(cursor.fetchmany(3))#显示size条数据/显示指定数据

cursor.close()#关闭游标
connection.close()#关闭链接对象