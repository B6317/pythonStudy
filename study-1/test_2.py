# coding=utf-8
# create by toonew at 2018/1/28
import MySQLdb
from test_1 import active_code

db = MySQLdb.connect("localhost", "root", "root", "python_test")
# 使用cursor()方法获取操作游标
cursor = db.cursor()

try:
    sql = "SELECT * FROM EMPLOYEE"
    cursor.execute(sql)
except Exception as e:
    print(e)
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # 创建数据表SQL语句
    sql = """CREATE TABLE EMPLOYEE (
              id INT PRIMARY KEY  AUTO_INCREMENT,
              active_code VARCHAR(16)
            )"""
    cursor.execute(sql)

# 插入数据
activeCodes = active_code(200, 16)

for activeCode in activeCodes:
    sql = "INSERT INTO EMPLOYEE VALUES(0,'%s')" % activeCode
    cursor.execute(sql)

db.commit()

# 关闭数据库
db.close()
