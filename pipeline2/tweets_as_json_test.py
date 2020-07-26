from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession

spark = SparkSession.builder \
.master("local") \
.appName("Word Count") \
.config("spark.some.config.option", "some-value") \
.getOrCreate()

# sc = SparkContext(appName="WordCountSpark")
# ssc = StreamingContext(sc, 40)

# firstDF = ("hdfs://localhost:9000/user/twitter_data/FlumeData.1595783845749.json")

#read table data into a spark dataframe
jdbcDF = spark.read.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/dp") \
    .option("dbtable", "Persons") \
    .option("user", "sqoop_user") \
    .option("password", "Password1234!") \
    .option("driver", "com.mysql.jdbc.Driver") \
    .load()



aDf = [(1,"perez","jose","nogales","nogales"), 
(2,"lopez","caste","matamoros","Tamaulipas"),
(3,"limon","esteban","Los Angeles","California")]

data = [{'PersonID': l[0], 'LastName': l[1], 'FirstName': l[2], 'Address': l[3], 'City': l[4]} for l in aDf]
df = spark.createDataFrame(data)
# df_2.write().mode(SaveMode.Append).jdbc(connectionProperties.getProperty("url"), "family", connectionProperties);
# data = [ {'dob': r[0], 'age': r[1], 'is_fan': r[2]} for r in data_list  ]
# connectionProperties =  Properties();
# connectionProperties.put("driver", "com.mysql.jdbc.Driver");
# connectionProperties.put("url", "jdbc:mysql://localhost:3306/dp");
# connectionProperties.put("user", "sqoop_user");
# connectionProperties.put("password", "Password1234!");
df.show()
# jdbcDF = spark.read().jdbc(connectionProperties.getProperty("url"), "Persons", connectionProperties);
jdbcDF.show();
jdbcDF.printSchema();

df.write.format("jdbc")\
.mode("overwrite")\
.option("url", "jdbc:mysql://localhost:3306/dp") \
.option("dbtable", "Persons") \
.option("user", "sqoop_user") \
.option("password", "Password1234!") \
.option("driver", "com.mysql.jdbc.Driver") \
.save()

print("DOOOOOOOOOONEEEEEEEEEEEEEEEE")