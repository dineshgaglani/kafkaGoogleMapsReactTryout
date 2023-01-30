from kafka import KafkaConsumer

TOPIC_NAME = 'my-topic-1'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print(message)
    print(message.value.decode('unicode_escape'))