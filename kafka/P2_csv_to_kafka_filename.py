#coding=utf-8
from kafka import KafkaProducer
import json
import csv
import sys
from os import walk

reload(sys)
sys.setdefaultencoding('utf8')

kafkaHost = "localhost"
kafkaPort = 9092
producer = KafkaProducer(bootstrap_servers = kafkaHost+":"+str(kafkaPort))

def loadFiles(mypath):
    for (dirpath, dirnames, filenames) in walk(mypath):
        filepath=""
        for file in filenames:
            topic=file[:-4]
            filepath = dirpath + "/"+ file
            mockKafka(filepath,topic)
            print("finish push topic:"+topic)

def readFieldNames(filePath):
    with open(filePath, 'r') as csvsource: 
        lines = csvsource.readlines()  # 读取所有行
        first_line = lines[0].replace('\n', '').replace('\r', '').replace('\"','').split(",") # 取第一行
        return tuple(first_line)

def mockKafka(filePath,kafkaTopic):
    # fieldnames=("PROD_CODE","PROD_NAME","PROD_TYPE")
     with open(filePath, 'r') as csvf: 
        fieldnames=readFieldNames(filePath)
        print(fieldnames)
        next(csvf, None)
        csvReader = csv.DictReader(csvf, fieldnames)
        # Convert each row into a dictionary
        for rows in csvReader: 
            # print(rows)
            messages=json.dumps(rows,ensure_ascii=False)
            print(messages)
            producer.send(kafkaTopic, bytes(messages.encode("utf-8")))
            producer.flush()
fileDirectory=sys.argv[1]
loadFiles(fileDirectory)