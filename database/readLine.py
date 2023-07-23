#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

filePath = "/data/justPython/database/report_opun_list.txt"
fr = open(filePath, 'r')
lines = open(filePath).readlines()

class Opun(object):
    def __init__(self,name,id,pid):
        self.name = name
        self.id = id
        self.pid = pid
    def __str__(self):
        return "name:%s, id:%s, pid:%s" % (self.name, self.id, self.pid)
for line in lines:
    opunLine = Opun(line.split(",")[0].split(":")[1].split("--")[0], line.split(",")[1].split(":")[1], line.split(",")[2].split(":")[1])
    print(opunLine)
    # records_to_insert .append(line.split(","))
