import os
import mysql.connector

# 数据库连接配置
db_host = '172.20.61.102'
db_name = 'jarvex_baowu'
db_user = 'root'
db_password = '123123'

# SQL 文件所在目录
sql_directory = 'xxx'

# 建立数据库连接
conn = mysql.connector.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password,
    port=3307
)
cursor = conn.cursor()

# 遍历目录下的 SQL 文件
for file_name in os.listdir(sql_directory):
    if file_name.endswith('.sql'):
        file_path = os.path.join(sql_directory, file_name)
        with open(file_path, 'r') as sql_file:
            sql_statements = sql_file.read()
            cursor.execute(sql_statements)
            conn.commit()

# 关闭数据库连接
cursor.close()
conn.close()