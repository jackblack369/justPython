import pandas as pd
import os
import sys
import math

# 根据excel内容，生产starrocks语句
# 单个表单个sheet，只保留主题字段信息, 
# 如果表有分区，那字段固定为 DAY_ID，且需要设置为主键（维度表无需设置分区字段）
# 主键必须列在表格的前面
# 执行语句：python genFlinkSQL2.py {source_directory} {sink_directory} {jdbc_url} {scan_url} {load_url} 
# 执行语句：python3 genFlinkSQL2.py /input /output 172.18.244.74:19030 172.18.244.74:18030 172.18.244.74:18030,172.18.244.75:18030,172.18.244.76:18030  

args = sys.argv


def generate_ddl_from_excel(excel_file):
    # Read the Excel file into a pandas DataFrame
    # 检查文件名是否包含排除的特定符号和指定格式的文件
    excluded_formats = [".xlsx", ".xls"]
    file_name = excel_file.split("/")[-1]
    file_format = os.path.splitext(excel_file)[1]
    if "~" in excel_file:
        print("!!! " + file_name + " has illegal character in file name !!!\n")
        return
    if file_format not in excluded_formats:
        print("!!! " + file_name + " has illegal format, file should be xlsx or xls !!!\n")
        return

    df = pd.read_excel(excel_file)
    last_index = len(df) - 1

    # Generate the CREATE DDL statements
    dbname = "rtdsp"
    tableName = os.path.splitext(os.path.basename(excel_file))[0]

    # tableName = "demo1"
    preDDL = "CREATE TABLE IF NOT EXISTS " + tableName

    ddl_statements = []
    ddl_statements.append(preDDL)
    ddl_statements.append("(")
    primKeys = []
    orderKeys = []

    partitionFlag = False

    for i, row in df.iterrows():
        field_name = row['字段名称']

        data_type = row['字段类型']
        if data_type in ['STRING', 'CHAR']:
            data_type = 'varchar' + "(" + str(int(row['长度'])) + ")"
        if data_type == 'DECIMAL':
            decimal_precision = 0 if math.isnan(row['精度']) else row['精度']
            data_type = 'decimal' + \
                "(" + str(int(row['长度'])) + "," + \
                str(int(decimal_precision)) + ")"
        
        if field_name == 'DAY_ID':
            data_type = 'date'
            partitionFlag = True
        
        field_desc = row['注释']
        prim_key = row['主键']
        if '排序' in df.columns:
            order_key = row['排序']
            if order_key is not None and order_key == 1:
                orderKeys.append(field_name)

        if not math.isnan(prim_key) :
            primKeys.append(field_name)

        # Create the DDL statement for the current field
        ddl_statement = f"    {field_name} {data_type} COMMENT '{field_desc}',"
        ddl_statements.append(ddl_statement)

    # todo
    primContent = ",".join(primKeys)

    ddl_statements.append("    PRIMARY KEY(" + primContent + ") NOT ENFORCED")

    ddl_statements.append(")")

    ddl_statements.append("WITH(\n"
    + "    'connector'='starrocks', \n"
    + "    'jdbc-url'='jdbc:mysql://" + args[3] + "', \n" 
    + "    'scan-url'='" + args[4] + "', \n" # 读
    + "    'load-url'='" + args[5] + "', \n" # 写
    + "    'username'='root', \n"
    + "    'password'='datacanvas', \n"
    + "    'database-name'='rtdsp', \n"
    + "    'table-name'='" + tableName + "' \n"
    ");")

    "\n".join(ddl_statements)

    # 将 DDL 语句输出到文件
    print("generate " + tableName + " ddl sql ......")
    output_file = output_directory + "/flink_ddl_" + tableName + ".sql"
    with open(output_file, 'w') as f:
        for ddl_statement in ddl_statements:
            f.write(ddl_statement + '\n')
            print(ddl_statement)
    print("====== success generate " + tableName + " ddl sql ======\n")

    return ddl_statements


if __name__ == "__main__":
    input_directory = args[1]
    output_directory = args[2]
    # excel_file = "./file/demo2.xlsx"  # Replace with the actual path to your Excel file
    # output_file = "./file/output_ddl.sql"
    for item in os.listdir(input_directory):
        item_path = os.path.join(input_directory, item)
        if os.path.isfile(item_path):
            # 获取文件的完整路径
            print("begin read file_path:" + item_path)
            ddl_statements = generate_ddl_from_excel(item_path)
            # Print the DDL statements
            # for ddl_statement in ddl_statements:
            #     print(ddl_statement)
