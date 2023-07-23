from kafka import KafkaProducer
import json
import csv
import sys

kafkaHost = "localhost"
kafkaPort = 9092
producer = KafkaProducer(bootstrap_servers = kafkaHost+":"+str(kafkaPort))

def mockKafka(filePath,kafkaTopic):
    with open(filePath, 'r') as csvf: 

        csvReader = csv.DictReader(csvf) 
          
        # Convert each row into a dictionary  
        for rows in csvReader: 
            # print(rows)
            messages=json.dumps(rows,ensure_ascii=False)
            # print(messages)
            producer.send(kafkaTopic, bytes(messages.encode("utf-8")))
            producer.flush()
filePath=sys.argv[1]
kafkaTopic=sys.argv[2]
mockKafka(filePath,kafkaTopic)