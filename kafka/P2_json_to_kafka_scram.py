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

def loadFiles(mypath, topic):
    for (dirpath, dirnames, filenames) in walk(mypath):
        filepath=""
        for file in filenames:
            filepath = dirpath + "/"+ file
            mockKafka(filepath,topic)
            print("finish push topic:"+topic)

def mockKafka(filePath,kafkaTopic):
    # fieldnames=("PROD_CODE","PROD_NAME","PROD_TYPE")
     with open(filePath, 'r') as jsonf: 
        # csvReader = csv.DictReader(csvf, fieldnames)
        # Convert each row into a dictionary
        for rows in jsonf: 
            rows=rows.replace('\n', '').replace('\r', '') 
            print(rows)
            producer.send(kafkaTopic, bytes(rows.encode("utf-8")))
            producer.flush()
fileDirectory=sys.argv[1]
topic=sys.argv[2]

loadFiles(fileDirectory, topic)