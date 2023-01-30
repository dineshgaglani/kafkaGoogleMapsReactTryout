from ensurepip import bootstrap
import random 
import csv
import time
from kafka import KafkaProducer
import os
import pickle
import json

TOPIC_NAME = 'my-topic-1'
KAFKA_SERVER = os.environ.get('KAFKA_SERVER')

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

def getRandomLatLong(fileName: str):
    #Randomly picks a Calgary lat long and emits to local kafka at random periods ranging from 0s to 120s
    BUYER_TYPE = 'Buyer'
    SELLER_TYPE = 'Seller'
    selectedUserType = random.choice([BUYER_TYPE, SELLER_TYPE])

    with open(fileName, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    selectedCalgaryPostalCodeLatLong = random.choice(data)
    selectedCalgaryPostalCodeLatLong.append(selectedUserType)
    return selectedCalgaryPostalCodeLatLong

def emitToKafka(dataToEmit):
    dataToEmitString = json.dumps(dataToEmit).encode('unicode_escape')
    dataToEmitBytes = pickle.dumps(dataToEmitString)
    producer.send(TOPIC_NAME, dataToEmitBytes)
    producer.flush()

MAX_EMITS = 10
currEmits = 0

while currEmits < MAX_EMITS:
    currEmits += 1
    time.sleep(random.choice(range(0, 10)))
    emitToKafka(getRandomLatLong('./data/CalgaryPostalToLatLong.csv'))

print('----/////////END//////////------')



