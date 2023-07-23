# -*- coding: utf-8 -*-

import redis
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

f = open('content.txt','w')
r = redis.Redis(host='localhost', port=6379, decode_responses=True)  
r.set('name', '中文') 
print(r['name'])
content = r.get('RT_DC')
#print(content)
#print(type(r.get('name')))
f.write(content)
f.close()
