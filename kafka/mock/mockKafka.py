from kafka import KafkaProducer
import random
import json

# Define the Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Define the column array and data types
columns = ['id', 'name', 'age']
data_types = ['int', 'str', 'int']

# Define the data length
data_length = 10

# Mock the topic record based on the column array, data types, and data length
for i in range(data_length):
    record = {}
    for j in range(len(columns)):
        if data_types[j] == 'int':
            record[columns[j]] = random.randint(1, 100)
        elif data_types[j] == 'str':
            record[columns[j]] = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    producer.send('test_topic', json.dumps(record).encode('utf-8'))



