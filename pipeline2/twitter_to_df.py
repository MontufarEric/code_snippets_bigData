

from pyspark import SparkContext
from pyspark.sql import SparkSession
import re 


spark = SparkSession.builder.appName("WordCountSpark").getOrCreate()



sc = SparkContext.getOrCreate()


text_file = sc.textFile("hdfs://localhost:9000/user/twitter_data/FlumeData.1595783845749.json")

# counts = text_file.flatMap(lambda line: line.split(" ")) \
             # .map(lambda word: (word, 1)) \
             # .reduceByKey(lambda a, b: a + b)


from collections import namedtuple
fields = ("tag", "count", "length" )
Tweet = namedtuple( 'Tweet', fields )

# Use Parenthesis for multiple lines or use \.
counts = text_file.flatMap( lambda text: text.split( " " ))\
.filter( lambda word: word.lower().startswith("#") )\
.map(lambda word: word[1:])\
.filter(lambda word: re.sub('[^A-Za-z0-9]+', '', word))\
.filter(lambda word: len(word)>1)\
.map( lambda word: ( word.lower(), 1 ) )\
.reduceByKey( lambda a, b: a + b )\
.map( lambda rec: Tweet( rec[0], rec[1], len(rec[0]) ) )\
# .foreachRDD( lambda rdd: rdd.toDF().sort( desc("count") ))
df = spark.createDataFrame(counts)


print("--------------------------------------------------")
print(counts.take(50))
print('--------------------------------------------------')
df.orderBy(df['count'].desc()).show()
df.printSchema()

df.withColumn('cleanTweet',df['tag'].str.encode('ascii', 'ignore').str.decode('ascii')).show()




# counts.saveAsTextFile("/home/fieldengineer/Documents/data_plumbers/013_Spark/wc_pyspark_hdfs_tw")