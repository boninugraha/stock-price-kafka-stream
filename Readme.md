# Stock Price Pub/Sub System with Kafka

This app will simulate the kafka cluster using the docker container and can be scaled into a bigger system. The main idea is to reduce the amount of requests to financial resources that may have additional price if consumed multiple times. With this approach the `Producer` can consume data once, and multiple `Consumer`s can stream the data.
## Environment Setup
Run this command to setup the system:
```bash
docker-compose -f docker-composer.yml up -d
```

## Setup the Kafka System
Once containers created, we need to enter the kafka container, using this command:
```bash
docker exec -t kafka /bin/sh
```

Inside the cluster, we can use run these commands to manage topics:
```bash
# Go to kafka application folder
cd /opt/kafka/bin

# create kafka topic
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic kafkatopic1

# list all kafka topic
kafka-topics.sh --list --zookeeper zookeeper:2181

# get detail info about a topic
kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic kafkatopic1

# delete a topic
kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic kafkatopic1

```

## Produce and Consume Message from Console
Once we created a topic we can send and receive message directly from a console.
This app will try to produce and consume message from a python script, so we are not going to use these commands.
```bash
# run topic producer
kafka-console-producer.sh --broker-list kafka:9092 --topic kafkatopic1

# run topic consumer when it produced
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic kafkatopic1

# see the produced message history
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic kafkatopic1 --from-beginning
```

# Further Plan:
This is an ongoing project, and I will add more features:

- [ ] Read information directly from life sources instead of historical data.
- [ ] Deploy the setup on AWS.
- [ ] Create a data consumer that will update dashboard everytime there is a new record.
    - [ ] Create a better pipeline on the `Consumer` part.
    - [ ] Create multiple topics, can be: stock ticker, or industry category.
        - [ ] Ability to create a topic on the fly.
        - [ ] Ability to delete a topic on the fly.
- [ ] etc.