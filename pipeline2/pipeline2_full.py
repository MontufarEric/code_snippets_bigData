from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from collections import namedtuple
from pyspark.sql import SparkSession
import re 
import random

spark = SparkSession.builder.appName("WordCountSpark").getOrCreate()

sc = SparkContext.getOrCreate()
ssc = StreamingContext(sc, 25)



fields = ("id","hashtag", "count", "length" )
Tweet = namedtuple( 'Tweet', fields )

def toSQL(df):
	df.show()
	df.write.format("jdbc")\
	.mode("overwrite")\
	.option("url", "jdbc:mysql://localhost:3306/dp") \
	.option("dbtable", "hashtgs") \
	.option("user", "sqoop_user") \
	.option("password", "Password1234!") \
	.option("driver", "com.mysql.jdbc.Driver") \
	.save()


def savetheresult( rdd ):
    if not rdd.isEmpty():
    	df = spark.createDataFrame(rdd)
    	toSQL(df)
    	df.write.save("songs_json", format="json", mode="append")
 

lines = ssc.textFileStream("hdfs://localhost:9000//user/twitter_data")


counts = lines.flatMap( lambda text: text.split( " " ))\
.filter( lambda word: word.lower().startswith("#") )\
.map(lambda word: word.replace('#',''))\
.map(lambda word: word.lower())\
.filter(lambda word: re.sub('[^a-z]+', '', word))\
.filter(lambda word: len(word)>1)\
.map( lambda word: ( word, 1 ) )\
.reduceByKey( lambda a, b: a + b )\
.map( lambda rec: Tweet( random.randint(1,100000) ,rec[0], rec[1], len(rec[0]) ) )\
.foreachRDD(lambda x: savetheresult(x))
# savetheresult(counts)
# .foreachRDD( lambda rdd: rdd.toDF().sort( desc("count") ))
# df = spark.createDataFrame(counts)
# df = counts.toDF()
# words = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
print("--------------------------------------------------")
# print(counts.take(20))
# counts.pprint()
print('--------------------------------------------------')
# df.orderBy(df['count'].desc()).show()
# df.printSchema()



# counts.saveAsTextFiles("/home/fieldengineer/Documents/data_plumbers/pipeline2/hashtag_counts/tw")

ssc.start()
ssc.awaitTermination()