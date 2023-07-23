#! /usr/bin/python
# -*- coding: utf-8 -*
import os
import os.path
import time
import datetime


logdir = "/opt/apache-tomcat-9.0.46/logs"
nDayAgo = (datetime.datetime.now() - datetime.timedelta(days=7))  # 当前时间的n天前的时间
timeStamp = int(time.mktime(nDayAgo.timetuple()))

for parent, dirnames, filenames in os.walk(logdir):
    for filename in filenames:
        # fullname = parent + "/" + filename  # 文件全称
        fullname = os.path.join(parent, filename)
        createTime = int(os.path.getctime(fullname))  # 文件创建时间
        print("fullname:"+fullname + ",  createTime:"+str(createTime))
        if createTime < timeStamp:  # 创建时间在n天前的文件删除
            os.remove(fullname)
            print("===remove "+fullname+" success !!! ===")
