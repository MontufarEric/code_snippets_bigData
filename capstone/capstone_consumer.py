from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from collections import namedtuple
import random
from pyspark.sql import SparkSession
import re 
import pyspark.sql.types as st 
from datetime import datetime

spark = SparkSession.builder.appName("capstone")\
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/test.testYoutube") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/test.testYoutube") \
	.getOrCreate()
sc = SparkContext.getOrCreate()


listOfCompanies=['apple', 'samsung', 'huawei', 'xiaomi', 'vivo', 'oppo', 'motorola', 'realme', 'sony', 'oneplus']

fields = ("videoId","channelId", "date" , "mobileCompany", "views", "commnets", "likes", "dislikes" )
video = namedtuple("video", fields)

video_schema = st.StructType([
		st.StructField("videoId", st.StringType(), True),
		st.StructField("channelId", st.StringType(), True),
		st.StructField("date", st.TimestampType(), True ),
		st.StructField("mobileCompany", st.StringType(), True),
		st.StructField("views", st.IntegerType(), True),
		st.StructField("comments", st.IntegerType(), True),
		st.StructField("likes", st.IntegerType(), True),
		st.StructField("dislikes", st.IntegerType(), True)
	])


def  getCompany(t):
	t = t.lower()
	t = re.sub('[^a-z ]+', '', t)
	t = t.split()
	t = list(filter(lambda word: word in listOfCompanies, t))
	if len(t)>0:
		return t[0]
	else:
		return 'Null'


def savetheresult( rdd ):
    if not rdd.isEmpty():
    	df = spark.createDataFrame(rdd, video_schema)
    	df.show()
    	df.printSchema()
    	df.write.format("mongo").mode("append").save()
    	# toSQL(df)
    	# df.write.save("songs_json", format="json", mode="append")



# people = spark.createDataFrame([("Bilbo Baggins",  50), ("Gandalf", 1000), ("Thorin", 195), ("Balin", 178), ("Kili", 77),
#    ("Dwalin", 169), ("Oin", 167), ("Gloin", 158), ("Fili", 82), ("Bombur", None)], ["name", "age"])



#------------------------------STREAMING------------------------------------------------

ssc = StreamingContext(sc, 5)

kvs = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming-consumer', {'test':1})
data = kvs.map(lambda x: json.loads(x[1]))\
.map(lambda x: json.loads(x))\
.map(lambda x: video(x['videoId'], x['channelId'], datetime.strptime(x['date'],'%Y-%m-%dT%H:%M:%SZ' ), 
	getCompany(x['title']), int(x['stats']['viewCount']), int(x['stats']['commentCount']), 
	int(x['stats']['likeCount']), int(x['stats']['dislikeCount'])))\
.foreachRDD(lambda x: savetheresult(x))

# data.pprint()

ssc.start()
ssc.awaitTermination()