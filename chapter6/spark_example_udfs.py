#Note - reuses some code from chapter 3
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import StringType
from pyspark.sql import functions as f


# Create spark context
sc = SparkContext("local", "Ch6BasicExampleApp")
# Get spark session
spark = SparkSession.builder.getOrCreate()

# Get the data and place it in a spark dataframe
data = spark.read.format("csv").option("sep", ";").option("inferSchema", "true").option("header", "true").load(
    "../chapter1/stream-classifier/data/bank/bank.csv")

# map target to numerical category
#data = data.withColumn('label', f.when((f.col("y") == "yes"), 1).otherwise(0))

data.printSchema()

data.show()

# UDF
import datetime
def create_date(day, month):
    month_number = datetime.datetime.strptime(month, "%b").month
    return datetime.datetime(2020, month_number, day).strftime("%Y-%m-%d")

spark.udf.register("CreateDate", create_date, StringType())


