#!/usr/bin/env python

import pyhs2
import sys

default_encoding = 'utf-8'

conn = pyhs2.connect(host='$hs2host',
                                  port=$hs2port,
                                  authMechanism='PLAIN',
                                  user='hadoop',
                                  password='',
                                  database='default',)


tablename = 'HiveByPython'
cur = conn.cursor()
print 'show the databases: '
print cur.getDatabases()

print "\n"
print 'show the tables in default: '
cur.execute('show tables')
for i in cur.fetch():
        print i

cur.execute('drop table if exists ' + tablename)
cur.execute('create table ' + tablename + ' (key int,value string)')

print "\n"
print 'show the new table: '
cur.execute('show tables ' +"'" +tablename+"'")
for i in cur.fetch():
        print i

print "\n"
print "contents from " + tablename + ":";
cur.execute('insert into ' + tablename + ' values (42,"hello"),(48,"world")')
cur.execute('select * from ' + tablename)
for i in cur.fetch():
        print i