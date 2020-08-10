from pyspark import SparkContext
import json
from collections import namedtuple
import random
from pyspark.sql import SparkSession
import re 
import pyspark.sql.types as st 
from datetime import datetime, date, timedelta

spark = SparkSession.builder.appName("capstone")\
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/test.testYoutube") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/test.testYoutube") \
	.getOrCreate()

sc = SparkContext.getOrCreate()


df2 = spark.read.csv("users.csv",header=True,inferSchema=True)
df2.show()

yesterday = datetime.now() - timedelta(weeks=+14)

df = spark.read.format("mongo").load()
df.show()

innerJoinDf = df.join(df2,"channelId")
innerJoinDf.show()
# df.filter(df.date >= yesterday).show()


df.printSchema()