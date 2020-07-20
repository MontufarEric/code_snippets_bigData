import findspark
import json
import csv

findspark.init("/home/fieldengineer/opt/spark-2.4.4")
from pyspark.streaming.flume import FlumeUtils
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext(appName="flumeSPark")
ssc = StreamingContext(sc, 10)

stream = FlumeUtils.createStream(ssc,"localhost" ,9999)
lines = stream.map(lambda x: x[1])
print(lines)

ssc.start()
ssc.awaitTermination()
