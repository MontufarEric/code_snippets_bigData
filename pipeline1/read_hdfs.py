
# import findspark
# findspark.init("/home/fieldengineer/opt/spark-2.4.4")
from pyspark import SparkContext
sc = SparkContext(appName="WordCountSpark")


text_file = sc.textFile("hdfs://localhost:9000//user/twitter_data/FlumeData.1595613066799")

counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

counts.saveAsTextFile("/home/fieldengineer/Documents/data_plumbers/013_Spark/wc_pyspark_hdfs_tw")
