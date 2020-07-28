# from pyspark.streaming.kafka import KafkaUtils

# ssc = StreamingContext(sc, 2)
# kafkaStream = KafkaUtils.createStream(ssc, [ZK quorum], [consumer group id], [per-topic number of Kafka partitions to consume])


from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from collections import namedtuple
import random
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("WordCountSpark").getOrCreate()
sc = SparkContext.getOrCreate()
ssc = StreamingContext(sc, 10)

fields = ("id","title", "popularity", "explicit", "duration_ms" )
song = namedtuple("song", fields)



def toSQL(df):
	df.show()
	df.write.format("jdbc")\
	.mode("append")\
	.option("url", "jdbc:mysql://localhost:3306/dp") \
	.option("dbtable", "songs") \
	.option("user", "sqoop_user") \
	.option("password", "Password1234!") \
	.option("driver", "com.mysql.jdbc.Driver") \
	.save()

def savetheresult( rdd ):
    if not rdd.isEmpty():
    	df = spark.createDataFrame(rdd)
    	toSQL(df)
    	df.write.save("points_json", format="json", mode="append")

kvs = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming-consumer', {'test':1})
data = kvs.map(lambda x: json.loads(x[1]))\
.map(lambda x: json.loads(x))\
.flatMap(lambda x: x['tracks']['items'])\
.map( lambda rec: song( random.randint(1,100000) ,rec['name'], rec['popularity'], str(rec['explicit']), rec['duration_ms'] ) )\
.foreachRDD(lambda x: savetheresult(x))


ssc.start()
ssc.awaitTermination()