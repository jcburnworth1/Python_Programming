##### Import Libraries #####
from pyspark.sql import SparkSession
from pyspark.sql.functions import lead, unix_timestamp
from pyspark.sql import Window

##### Setup Context & Session #####
spark = SparkSession.builder.getOrCreate()

##### Read in the Data #####
## Load trainsched.txt
df = spark.read.csv('PySpark/SparkSQL/trainsched.txt', header=True)

## Create temporary table called table1
df.createOrReplaceTempView('schedule')

##### Determine the column names #####
## Inspect the columns in the table df
spark.sql("DESCRIBE schedule").show()

##### Window Functions #####
## Add col running_total that sums diff_min col in each group
query = """SELECT train_id, station, time, diff_min,
           SUM(float(diff_min)) OVER (PARTITION BY train_id ORDER BY time) AS running_total
           FROM schedule"""

## Run the query and display the result
spark.sql(query).show()

##### Fix the broken query #####
query = """SELECT ROW_NUMBER() OVER (ORDER BY time) AS row, train_id,
           station, time, LEAD(time,1) OVER (ORDER BY time) AS time_next
           FROM schedule"""
spark.sql(query).show()

# Give the number of the bad row as an integer
bad_row = 8

# Provide the missing clause, SQL keywords in upper case
clause = 'PARTITION BY train_id'

##### Dot Notation #####
##### Aggregation Step by Step
## Give the identical result in each command
spark.sql('SELECT train_id, MIN(time) AS start FROM schedule GROUP BY train_id').show() ## SQL
df.groupBy('train_id').agg({'time':'min'}).withColumnRenamed('min(time)', 'start').show() ## Dot Notation

## Print the second column of the result
spark.sql('SELECT train_id, MIN(time), MAX(time) FROM schedule GROUP BY train_id').show() ## SQL
result = df.groupBy('train_id').agg({'time':'min', 'time':'max'}) ## Dot Notation
result.show()
print(result.columns[1])

##### Aggregating the same column twice #####
## Recreate this dot notation with SQL
## from pyspark.sql.functions import min, max, col
## expr = [min(col("time")).alias('start'), max(col("time")).alias('end')]
## dot_df = df.groupBy("train_id").agg(*expr)
## dot_df.show()
## +--------+-----+-----+
## |train_id|start|  end|
## +--------+-----+-----+
## |     217|6:06a|6:59a|
## |     324|7:59a|9:05a|
## +--------+-----+-----+

## Write a SQL query giving a result identical to dot_df above
query = "SELECT train_id, min(time) AS start, max(time) AS end FROM schedule GROUP BY train_id"
sql_df = spark.sql(query)
sql_df.show()

##### Aggregate dot SQL #####
## Recreate this SQL with dot notation
# df = spark.sql("""
# SELECT *,
# LEAD(time,1) OVER(PARTITION BY train_id ORDER BY time) AS time_next
# FROM schedule
# """)
# +--------+-------------+-----+---------+
# |train_id|      station| time|time_next|
# +--------+-------------+-----+---------+
# |     217|       Gilroy|6:06a|    6:15a|
# |     217|   San Martin|6:15a|    6:21a|
# |     217|  Morgan Hill|6:21a|    6:36a|
# +--------+-------------+-----+---------+

## Obtain the identical result using dot notation
dot_df = df.withColumn('time_next', lead('time', 1)
        .over(Window.partitionBy('train_id')
        .orderBy('time')))
dot_df.show()

##### Convert window function from dot to SQL #####
## Recreate this dot notation with SQL #####
window = Window.partitionBy('train_id').orderBy('time')
dot_df = df.withColumn('diff_min',
                    (unix_timestamp(lead('time', 1).over(window),'H:m')
                     - unix_timestamp('time', 'H:m'))/60)
# +--------+-------------+-----+--------+
# |train_id|      station| time|diff_min|
# +--------+-------------+-----+--------+
# |     217|       Gilroy|6:06a|     9.0|
# |     217|   San Martin|6:15a|     6.0|
# |     217|  Morgan Hill|6:21a|    15.0|
# +--------+-------------+-----+--------+

## Create a SQL query to obtain an identical result to dot_df
query = """SELECT *, 
           (UNIX_TIMESTAMP(LEAD(time, 1) OVER (PARTITION BY train_id ORDER BY time),'H:m') - UNIX_TIMESTAMP(time, 'H:m'))/60 AS diff_min 
           FROM
           schedule """
sql_df = spark.sql(query)
sql_df.show()