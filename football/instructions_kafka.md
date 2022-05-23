# kafka instructions

## zookeeper
https://www.tutorialspoint.com/zookeeper/zookeeper_installation.htm
## kafka
https://www.tutorialspoint.com/apache_kafka/apache_kafka_installation_steps.htm
NOTE: this is the wrong version, download latest

then:
start zk with
apache-zookeeper-3.6.2-bin/bin/zkServer.sh start
(change start with stop to stop)
start kafka with
kafka_2.12-2.7.0/bin/kafka-server-start.sh ./kafka_2.12-2.7.0/config/server.properties
and stop with
kafka_2.12-2.7.0/bin/kafka-server-stop.sh ./kafka_2.12-2.7.0/config/server.properties
