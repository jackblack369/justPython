from sqlalchemy import create_engine, inspect

# 创建数据库引擎
engine = create_engine('mysql+pymysql://root:123123@172.20.61.102:3307/jarvex')

# 创建Inspector对象
inspector = inspect(engine)

# 获取指定表的建表语句
table_name = 'RESOURCE'
table_create_statement = inspector.get_table_create_statement(table_name)

print(table_create_statement)
