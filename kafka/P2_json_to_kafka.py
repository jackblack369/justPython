#coding=utf-8
from kafka import KafkaProducer
import json
import csv
import sys
import time
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
            topic=file[:-5]
            filepath = dirpath + "/"+ file
            mockKafka(filepath,topic)
            print("finish push topic:"+topic)

def mockKafka(filePath,kafkaTopic):
    # fieldnames=("PROD_CODE","PROD_NAME","PROD_TYPE")
     with open(filePath, 'r') as csvf: 
        # csvReader = csv.DictReader(csvf, fieldnames)
        # Convert each row into a dictionary
        for rows in csvf: 
            # print(rows)
            rows=rows.replace('\n', '').replace('\r', '') # 取第一行
            print(rows)
            producer.send(kafkaTopic, bytes(rows.encode("utf-8")))
            producer.flush()
fileDirectory=sys.argv[1]

def scheduleSend(directory):
    while True:
        loadFiles(directory)
        print(time.time())
        time.sleep(5)

scheduleSend(fileDirectory)