#coding=utf-8
from confluent_kafka import Producer
import json
import sys
import time
from os import walk

reload(sys)
sys.setdefaultencoding('utf8')

conf = {
    'bootstrap.servers': '10.110.18.214:9092,10.110.16.96:9092,10.110.19.242:9092',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.mechanisms': 'SCRAM-SHA-256',
    'sasl.username': 'admin',
    'sasl.password': 'admin'
}

producer = Producer(**conf)


def loadFiles(mypath, topic):
    for (dirpath, dirnames, filenames) in walk(mypath):
        filepath = ""
        for file in filenames:
            filepath = dirpath + "/" + file
            mockKafka(filepath, topic)
            print("finish push topic:"+topic)


def mockKafka(filePath, kafkaTopic):
    with open(filePath, 'r') as jsonf:
        # Convert each row into a dictionary
        for rows in jsonf:
            rows = rows.replace('\n', '').replace('\r', '')
            print(rows)
            producer.produce(kafkaTopic, (json.dumps(rows)).encode(), callback=delivery_report)
        producer.flush()

fileDirectory = sys.argv[1]
topic = sys.argv[2]

loadFiles(fileDirectory, topic)
