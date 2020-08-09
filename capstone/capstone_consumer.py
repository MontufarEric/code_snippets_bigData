from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from collections import namedtuple
import random
from pyspark.sql import SparkSession
import re 


spark = SparkSession.builder.appName("capstone").getOrCreate()
sc = SparkContext.getOrCreate()




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
    	df = spark.createDataFrame(rdd)
    	df.show()
    	# toSQL(df)
    	# df.write.save("songs_json", format="json", mode="append")


listOfCompanies=['apple', 'samsung', 'huawei', 'xiaomi', 'vivo', 'oppo', 'motorola', 'realme', 'sony', 'oneplus']

fields = ("videoId","channelId", "date", "mobileCompany", "views", "commnets", "likes", "dislikes" )
video = namedtuple("video", fields)

#------------------------------STREAMING------------------------------------------------

ssc = StreamingContext(sc, 5)

kvs = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming-consumer', {'test':1})
data = kvs.map(lambda x: json.loads(x[1]))\
.map(lambda x: json.loads(x))\
.map(lambda x: video(x['videoId'], x['channelId'], x['date'], getCompany(x['title']), x['stats']['viewCount'], x['stats']['commentCount'], x['stats']['likeCount'], x['stats']['dislikeCount']))


# data.pprint()

ssc.start()
ssc.awaitTermination()