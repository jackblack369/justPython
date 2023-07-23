# -*- coding: utf-8 -*-

import redis
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

ip=sys.argv[1]

r = redis.Redis(host=ip, port=6379, decode_responses=True)
filepath = sys.argv[2]

file_name = os.path.basename(filepath)
# 输出为 test.py
file_name = file_name.split('.')[0]
print(file_name)

with open(filepath) as file_object:
    zds = file_object.readlines()
    for zd in zds:
        zd = zd.strip('\n')
        r.hset(name=file_name,key='20',value=zd)
        #print zd

