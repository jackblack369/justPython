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

def mockKafka(filePath,kafkaTopic):
    with open(filePath, 'r') as csvf: 
        csvReader = csv.DictReader(csvf)
        # Convert each row into a dictionary
        for rows in csvReader: 
            # print(rows)
            messages=json.dumps(rows,ensure_ascii=False)
            print(messages)
            producer.send(kafkaTopic, bytes(messages.encode("utf-8")))
            producer.flush()
fileDirectory=sys.argv[1]
loadFiles(fileDirectory)