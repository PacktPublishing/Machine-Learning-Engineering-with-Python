#Note - reuses some code from chapter 3
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql import functions as f


# Create spark context
sc = SparkContext("local", "Ch6BasicExampleApp")
# Get spark session
spark = SparkSession.builder.getOrCreate()

# Get the data and place it in a spark dataframe
data = spark.read.format("csv").option("sep", ";").option("inferSchema", "true").option("header", "true").load(
    "../chapter1/stream-classifier/data/bank/bank.csv")

# map target to numerical category
data = data.withColumn('label', f.when((f.col("y") == "yes"), 1).otherwise(0))

data.show()