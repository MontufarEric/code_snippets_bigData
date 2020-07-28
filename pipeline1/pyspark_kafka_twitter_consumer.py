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

def savetheresult( rdd ):
    if not rdd.isEmpty():
    	df = spark.createDataFrame(rdd)
    	# toSQL(df)
    	df.write.save("points_json", format="json", mode="append")

kvs = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming-consumer', {'test':1})
data = kvs.map(lambda x: json.loads(x[1]))\
.map(lambda x: json.loads(x))\
.flatMap(lambda x: x['tracks']['items'])\
.map( lambda rec: song( random.randint(1,100000) ,rec['name'], rec['popularity'], rec['explicit'], rec['duration_ms'] ) )\
.foreachRDD(lambda x: savetheresult(x))
# lines = kvs.map(lambda x: x[1])
# counts = lines.flatMap(lambda line: line.split(" ")) \
#     .map(lambda word: (word, 1)) \
#     .reduceByKey(lambda a, b: a+b)
# counts.pprint()
# data.pprint()
# print(type(data))
print()
print()
# kvs.pprint()
# print(json.dumps(data, indent=4))
ssc.start()
ssc.awaitTermination()