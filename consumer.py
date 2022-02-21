import json
from kafka import KafkaConsumer

if __name__ == "__main__":
    consumer = KafkaConsumer("message", bootstrap_servers="localhost:9092")
    for message in consumer:
        print(json.loads(message.value))
