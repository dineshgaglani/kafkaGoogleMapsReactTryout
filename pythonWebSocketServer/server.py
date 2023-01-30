#!/usr/bin/env python

from asyncio.events import get_event_loop
from asyncio.futures import Future
from functools import partial
import asyncio
import logging
from re import L
from kafka import KafkaConsumer
import threading
import websockets
import os

def run_consumer(shutdown_flag, clients, lock):
    print("Starting Kafka Consumer.")

    KAFKA_SERVER = os.environ.get('KAFKA_SERVER')

    print('KAFKA SERVER is ------------ %s', KAFKA_SERVER)
    TOPIC_NAME = 'my-topic-1'

    consumer = KafkaConsumer(bootstrap_servers=KAFKA_SERVER, value_deserializer=lambda m: m.decode('unicode_escape'))   
    consumer.subscribe(TOPIC_NAME)
    # for message in consumer:
    #     print(message)
    #     print(message.value.decode('unicode_escape'))
    while not shutdown_flag.done():
        msg = consumer.poll(200)

        if not msg:
            print("Waiting...")
        # elif msg.error():
        #     print(f"ERROR: {msg.error()}")
        else:
            print("msg: %s", msg)
            # value = msg.value()
            #formatted = simplejson.dumps(msg)
            print(f"Sending {msg} to {clients}")

            with lock:
                websockets.broadcast(clients, str(msg))

    print("Closing Kafka Consumer")
    consumer.close()

async def handle_connection(clients, lock, connection, path):
    print("connected clients %s", str(len(clients)))
    with lock:
        clients.add(connection)

    await connection.wait_closed()

    with lock:
        clients.remove(connection)


async def main():
    shutdown_flag = Future()
    clients = set()
    lock = threading.Lock()

    get_event_loop().run_in_executor(None, run_consumer, shutdown_flag,
                                     clients, lock)

    print("Starting WebSocket Server.")
    try:
        async with websockets.serve(partial(handle_connection, clients, lock),
                                    "0.0.0.0", 9696):
            await Future()
    finally:
        shutdown_flag.set_result(True)


asyncio.run(main())