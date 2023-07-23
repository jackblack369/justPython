#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import pymysql

class Opun(object):
    def __init__(self,name,id,pid):
        self.name = name
        self.id = id
        self.pid = pid
    def __str__(self):
        return "name:%s, id:%s, pid:%s" % (self.name, self.id, self.pid)

filePath = "/data/justPython/database/report_opun_list.txt"
fr = open(filePath, 'r')
lines = open(filePath).readlines()

try:
    connection = pymysql.connect(host='127.0.0.1',
                                         database='linyi',
                                         user='root',
                                         password='123456',
                                         charset='utf8')

    mySql_insert_query = """INSERT INTO opun (name, id, pid) 
                           VALUES (%s, %s, %s) """
    
    records_to_insert = []

    for line in lines:
        opunLine = Opun(line.split(",")[0].split(":")[1].split("--")[0], line.split(",")[1].split(":")[1], line.split(",")[2].split(":")[1])
        print(opunLine)
        records_to_insert .append(opunLine)

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into opun table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")