This pipeline creates a stream of data from the Spotify API to a SQL database. 
First, we initialize our kafka service: 



zookeeper-server-start.sh -daemon /home/fieldengineer/opt/kafka_2.12-2.0.0/config/zookeeper.properties

kafka-server-start.sh -daemon /home/fieldengineer/opt/kafka_2.12-2.0.0/config/server1.properties

kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

kafka-topics.sh --describe --zookeeper localhost:2181 --topic test


Once kafka is running, we can initialize our pyspark consumer (pipeline1_full_mysql_WORKING.py) including the kafka-spark jar file and the mysql connector package. 

At this point, you have to be sure to have a table in mysql to store the data: 

mysql -u sqoop_user -p
Password1234!
USE dp;

CREATE TABLE songs (
id INT NOT NULL,
title VARCHAR(255) NOT NULL,
popularity INT NOT NULL,
explicit VARCHAR(25) NOT NULL,
duration_ms INT NOT NULL,
PRIMARY KEY (id)
);

spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.4.4.jar --packages mysql:mysql-connector pyspark_kafka_twitter_consumer.py

Once the consumer is running, we can proceed to initialize our kafka producer and input a title for the songs we want to browse in spotify and add to our database. The name, port, driver and table of the database should match with the consumer code. Also be sure to match the schema of the table with the dataframe you're sending. 