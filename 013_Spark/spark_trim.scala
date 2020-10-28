val sourceDF = spark.createDF(
  List(
    ("  a     "),
    ("b     "),
    ("   c"),
    (null)
  ), List(
    ("word", StringType, true)
  )
)

val actualDF = sourceDF.withColumn(
  "trimmed_word",
  trim(col("word"))
)
actualDF.show()
