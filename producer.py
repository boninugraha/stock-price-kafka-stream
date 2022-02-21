import time
import json
import logging
from data_generator import generate_message
from kafka import KafkaProducer

logging.basicConfig(level=logging.INFO, format="%(asctime)s :: %(message)s")
logging.basicConfig(level=logging.INFO)

SERVER_ADDRESS = "localhost:9092"


def serializer(message):
    return json.dumps(message).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=[SERVER_ADDRESS], value_serializer=serializer
)

if __name__ == "__main__":
    while True:
        message_data = generate_message()
        logging.info(str(message_data))

        producer.send("message", message_data)

        time.sleep(1)
