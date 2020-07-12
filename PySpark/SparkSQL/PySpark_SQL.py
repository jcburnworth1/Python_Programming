##### Import Libraries #####
# from pyspark import SparkContext
from pyspark.sql import SparkSession

##### Setup Context & Session #####
# sc = SparkContext('local', 'spark_app')
spark = SparkSession.builder.getOrCreate()

##### Read in the Data #####
## Load trainsched.txt
df = spark.read.csv('PySpark/SparkSQL/trainsched.txt', header=True)

## Create temporary table called table1
df.createOrReplaceTempView('schedule')

##### Determine the column names #####
## Inspect the columns in the table df
spark.sql("DESCRIBE schedule").show()

## Convert diff_min to float


##### Window Functions #####
## Add col running_total that sums diff_min col in each group
query = """SELECT train_id, station, time, diff_min,
           SUM(diff_min) OVER (PARTITION BY train_id ORDER BY time) AS running_total
           FROM schedule"""

## Run the query and display the result
spark.sql(query).show()

##### Fix the broken query #####
query = """SELECT
           ROW_NUMBER() OVER (ORDER BY time) AS row,
           train_id,
           station,
           time,
           LEAD(time,1) OVER (ORDER BY time) AS time_next
           FROM
           schedule"""
spark.sql(query).show()

# Give the number of the bad row as an integer
bad_row = ____

# Provide the missing clause, SQL keywords in upper case
clause = '____ ____ ____'