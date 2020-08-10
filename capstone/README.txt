

This project uses the youtube API to ask for tech reviews videos focusing in cell phone reviews. I request the title and some statistics of the video to the API. This information is sent via kafka in a json format. 

The stream of data is read by a kafka consumer and processed with pyspark. Once in spark, the data is processed to get a dataframe with the following columns: 


datetime, company, views, likes, dislikes, comments, videoId, ChannelId


To run the consumer, I use the following line:

spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.4.4.jar --packages org.mongodb.spark:mongo-spark-connector_2.11:2.4.2 capstone_consumer.py


