from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


sc = SparkContext(appName="WordCountSpark")
ssc = StreamingContext(sc, 1)

lines = ssc.textFileStream("hdfs://localhost:9000//user/twitter_data/")
words = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
#wordCounts.print()
words.saveAsTextFiles("/home/fieldengineer/Documents/data_plumbers/013_Spark/wc_pyspark_hdfs_twitter")
ssc.start()
ssc.awaitTermination()
