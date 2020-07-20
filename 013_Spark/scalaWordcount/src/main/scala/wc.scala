import org.apache.spark.sql._
import org.apache.spark.sql.types._
import org.apache.spark.sql.SparkSession
import org.apache.spark._


object SparkWordCount {
 def main(args: Array[String]) = {
 	val spark = SparkSession.builder().appName("SparkWordCount").enableHiveSupport().getOrCreate()
	import spark.implicits._

	val tf =  spark.read.textFile("/home/fieldengineer/Documents/Shakespeare.txt")
	val counts = tf.flatMap(line => line.split(" ")).map(word => (word, 1)).toMap()
	counts.saveAsTextFile("/home/fieldengineer/Documents/data_plumbers/013_Spark/scala_spark_wc.txt")
}
}