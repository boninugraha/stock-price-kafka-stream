# Setup

This app will simulate the kafka cluster using the docker container. Run this command to setup the system:
```bash
docker-compose -f docker-composer.yml up -d
```

Once container created, we need to enter the kafka container, using this command:
```bash
docker exec -t kafka /bin/sh
```

Inside the cluster, we can use these commands:
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

# run topic producer
kafka-console-producer.sh --broker-list kafka:9092 --topic kafkatopic1

# run topic consumer when it produced
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic kafkatopic1

# see the produced message history

```