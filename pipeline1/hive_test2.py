

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from collections import namedtuple
import random
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("WordCountSpark")\
.config("spark.sql.warehouse.dir", "hdfs://localhost:9000/user/hive/warehouse/")\
.config("spark.sql.catalogImplementation","hive")\
.config("hive.metastore.uris", "thrift://localhost:9083")\
.enableHiveSupport()\
.getOrCreate()


df = spark.sql("select * from default.employee_table")
df.show()