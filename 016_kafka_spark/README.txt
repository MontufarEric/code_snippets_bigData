In this project, it was posible to create a data pipeline that consumes data from the spotifi API, send that data by using a kafka producer and consume it again with a spark streaming app. Once in spark, it is possible to create a dataframe and process the data. 

The first step to take is to start a zookeeper service 

zookeper-server-start.sh -daemon /home/opt/kafka_2_12/config/zookeeper1.properties

Then we start a kafka broker 

kafka-server-start.sh -daemon /home/fieldengineer/opt/kafka_2.12-2.0.0/config/server1.properties

Once kafka is up, we can create a topic 

kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test


and describe that topic 

kafka-topics.sh --describe --zookeeper localhost:2181 --topic test


Then we can create out kafka producer ---> kafka_producer_working.ipynb

create the pyspark consumer ---> pyspark_consumer_kafka.py 

and run them by using the proper assembly file. For this step you have to be sure to have the proper spark-streaming-kafka assembly including the right versions of karka, scala and spark. You can find this in the website: https://mvnrepository.com/artifact/org.apache.spark/spark-streaming-kafka-0-8-assembly_2.11/2.4.4


To run the app,you can first start the pyspark consumer with 

spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.4.4.jar spark_consumer.py
