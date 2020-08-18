

This project uses the youtube API to ask for tech reviews videos focusing in cell phone reviews. I request the title and some statistics of the video to the API. This information is sent via kafka in a json format. 

The stream of data is read by a kafka consumer and processed with pyspark. Once in spark, the data is processed to get a dataframe with the following columns: 


datetime, company, views, likes, dislikes, comments, videoId, ChannelId


To run the consumer, I use the following line:

spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.4.4.jar --packages org.mongodb.spark:mongo-spark-connector_2.11:2.4.2 capstone_consumer.py


for the second part, I created a schema in mysql to add the data and make queries and visualizations in mysql. 

CREATE TABLE videos (
videoId VARCHAR(255),
channelId VARCHAR(255), 
creationDate DATETIME,
mobileCompany VARCHAR(255),
views INT,
comments INT,
likes INT,
dislikes INT,
userName VARCHAR(255),
language VARCHAR(255),
PRIMARY KEY (videoId)
);

I start zookeeper, kafka and create a topic: 

zookeeper-server-start.sh -daemon /home/fieldengineer/opt/kafka_2.12-2.0.0/config/zookeeper.properties

kafka-server-start.sh -daemon /home/fieldengineer/opt/kafka_2.12-2.0.0/config/server1.properties

kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.4.4.jar --packages mysql:mysql-connector-java:5.1.39,org.mongodb.spark:mongo-spark-connector_2.11:2.4.2 capstone_consumer.py

python3 producer_working.py
