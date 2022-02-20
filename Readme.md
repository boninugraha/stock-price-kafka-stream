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
cd /opt/kafka/bin
# create kafka topic
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic kafkatopic1

# list all kafka topic
kafka-topics.sh --list --zookeeper zookeeper:2181
```