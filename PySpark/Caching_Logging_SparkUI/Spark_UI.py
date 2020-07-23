##### Import Libraries #####
from pyspark.sql import SparkSession

##### Setup Context & Session #####
## Default UI - http://localhost:4042
spark = SparkSession.builder.getOrCreate()

##### Read in the Data #####
## Load trainsched.txt
df = spark.read.csv('PySpark/SparkSQL/trainsched.txt', header=True)
df.createOrReplaceTempView('schedule')

##### Cache the df #####
spark.catalog.cacheTable('schedule')
## This will log an event in the UI
## This will log an event and capture in storage

##### Query the df #####
## Add col running_total that sums diff_min col in each group
query = """SELECT train_id,count(*)
           FROM schedule
           GROUP BY train_id"""

## Run the query and display the result
spark.sql(query).show()