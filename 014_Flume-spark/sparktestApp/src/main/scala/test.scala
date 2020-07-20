package guru.learningjournal.examples

import org.apache.spark.sql._
import org.apache.spark.sql.types._

object SparkTestApp {
 def main(args: Array[String]) = {
  val spark = SparkSession.builder()
  .appName("SparkTestApp")
  .enableHiveSupport()
  .getOrCreate()

  val df = spark.read.json(args(0))
  df.createTempView("surveys")
  spark.sql("""select age, count(*) as frequency from surveys where age between 20 and 65 group by age """)
   .write
   .saveAsTable("survey_frequency")

   spark.stop()
  }
 }
