import pymysql
import os
import datetime

# 建立数据库连接
connection = pymysql.connect(
    host='172.20.61.102',
    port=3307,
    user='root',
    password='123123',
    db='jarvex',
    cursorclass=pymysql.cursors.DictCursor
)


#connection = pymysql.connect(
#    host='127.0.0.1',
#    port=3306,
#    user='root',
#    password='1qaz2wsx',
#    db='uumsx',
#    cursorclass=pymysql.cursors.DictCursor
#)

# 创建游标对象
cursor = connection.cursor()

# 获取所有表名
cursor.execute("SHOW TABLES")

tables = [table["Tables_in_JARVEX"] for table in cursor.fetchall()]
print(tables)
# 生成备份数据
data = ""
for table in tables:
    # 获取创建表的 SQL 语句
    show_sql = "SHOW CREATE TABLE `{}`;".format(table.upper())
    print(show_sql)
    cursor.execute(show_sql)
    create_table_sql = cursor.fetchone()['Create Table']
    data += "DROP TABLE IF EXISTS `{}`;\n".format(table)
    data += create_table_sql + ";\n\n"

    # 获取表中的数据并生成插入语句
    cursor.execute("SELECT * FROM `{}`;".format(table))
    rows = cursor.fetchall()
    for row in rows:
        columns = ', '.join("`{}`".format(col) for col in row.keys())
        values = ', '.join("'{}'".format(val) for val in row.values())
        data += "INSERT INTO `{}` ({}) VALUES ({});\n".format(table, columns, values)
    data += "\n"

# 关闭游标和数据库连接
cursor.close()
connection.close()

# 生成备份文件路径
now = datetime.datetime.now()
filename = os.path.join(os.getenv("HOME"), "backup_{}.sql".format(now.strftime("%Y-%m-%d_%H:%M")))

# 写入备份数据到文件
with open(filename, "w") as file:
    file.write(data)