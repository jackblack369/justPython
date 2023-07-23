#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re

expression=',"[^,]'

all_line=[]
filePath = "/data/justPython/source_info"

fr = open(filePath, 'r')
lines = open(filePath).readlines()
for line in lines:
    print("原始line:"+line)
    if re.match(r'\,\"[^\,]', line):
        print("符合正则")
        all_line.append(line.replace('\n',''))
    else:
        print("不符合正则")
        all_line.append(line)

    # count_colon = line.count('\"')
    # if count_colon%2 == 0 :
    #     if re.match(r',"[^,]', line):
    #         all_line.append(line.replace('\n',''))
    #     else:
    #      all_line.append(line)
    #     # print("直接输出:"+line)
    # else:
    #     if not re.match(r',"[^,]', line):
    #         all_line.append(line)


    # split_arrays = len(line.split(",\""))
    # if split_arrays > 1 and split_arrays%2 == 0:
    #     all_line.append(line.replace('\n',''))
    #     # print("替换输出:"+line.replace('\n',''))
    # else:
    #     # print("直接输出:"+line)
    #     all_line.append(line)
fr.close() 

fw=open(filePath,'w')
for line in all_line:
    # print("替换line:"+line)
    fw.write(line)
fw.close()