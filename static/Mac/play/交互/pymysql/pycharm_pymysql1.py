import  pymysql
db_config = {
    'host':'127.0.0.1',
    'port':3306,
    'user': 'root',
    'password': 'qwe123',
    'db': 'student',
    'charset': 'utf8',
}
connection = pymysql.connect(**db_config)
cursor=connection.cursor()
print(cursor)

sql='select * from tb'
aa=cursor.execute(sql)
'''cursor.execute(select * from 表名字)'''
print(aa)

#执行SQL语句
# sql="insert tb values(5,'bb',6)"#插入数据提交事务操作
# aa=cursor.execute(sql)
# '''cursor.execute(select * from 表名字)'''
# print(aa)#返回生效行数

#执行SQL语句
# sql="delete from tb where id=5"#删除数据提交事务操作
# aa=cursor.execute(sql)
# '''cursor.execute(select * from 表名字)'''
# print(aa)#返回生效行数

# connection.commit()#提交事务（服务器在非事务回滚状态下传递）

bb=cursor.fetchall()#获取表中全部数据结果
# cc=cursor.fetchone()#显示表中一条数据
# dd=cursor.fetchmany(3)#显示size条数据/显示指定数据
print(bb)#打印获取数据

cursor.close()#关闭游标
connection.close()#关闭链接对象