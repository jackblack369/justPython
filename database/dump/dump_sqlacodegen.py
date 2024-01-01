import io, os
from sqlalchemy import create_engine
from sqlalchemy.sql.schema import MetaData, Table


# 创建数据库引擎
#engine = create_engine('mysql+pymysql://root:123123@172.20.61.102:3307/jarvex')

# Use reflection to fill in the metadata
engine = create_engine('mysql+pymysql://root:123123@172.20.61.102:3307/nacos')
metadata = MetaData(engine)
tables = ['CHAT_QU_DATA', 'CHAT_SE_DATA', 'COMMENT_BASE_INFO', 'CREATIVE_BASE_INFO', 'CREATIVE_QU_DATA', 'CREATIVE_SE_DATA', 'DATA_FILE', 'DATA_FILE_EXPERTISE', 'DATA_FILEFT', 'DATA_FILESET', 'DATA_FT_LIST', 'DATASET_DINGO', 'DATASET_FT_LIST', 'DEPARTMENT', 'MODEL_BASE_INFO', 'OPERATION', 'PERMISSION', 'PERMISSIONGROUP', 'REL_PGROUP_PERMISSION', 'REL_ROLE_PERMISSION', 'REL_ROLE_PGROUP', 'REL_USER_PERMISSION', 'REL_USER_ROLE', 'REL_USERGROUP_ROLE', 'REL_USERGROUP_USER', 'RESOURCE', 'ROLE', 'USER', 'USER_BASE', 'USERGROUP', 'VECTOR_DATA']
metadata.reflect(engine, tables)

# Write the generated model code to the specified file or standard output
# 获取指定表的元数据（包括列信息和约束）
table_name = 'roles'
table = Table(table_name, metadata, autoload=True, autoload_with=engine)

# 生成表的建表语句
ddl_statement = table.create(bind=engine, checkfirst=True)

print(str(ddl_statement))