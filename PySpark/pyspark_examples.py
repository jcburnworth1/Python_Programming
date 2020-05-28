## Spark Reference - http://spark.apache.org/docs/2.1.0/api/python/pyspark.html
##### Import Libraries #####
import pandas as pd
import numpy as np
from pyspark.sql import SparkSession

##### Basics #####
## Create my_spark
my_spark = SparkSession.builder.getOrCreate()

## Print my_spark
print(my_spark)

## Print Spark version
print(my_spark.version)

## Print the tables in the catalog
print(my_spark.catalog.listTables())

##### Query #####
## Query
query = "FROM flights SELECT * LIMIT 10"

## Get the first 10 rows of flights
flights10 = my_spark.sql(query)

## Show the results
flights10.show()

##### Query to Pandas #####
# Don't change this query
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"

# Run the query
flight_counts = my_spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

# Print the head of pd_counts
print(pd_counts.head())

##### Pandas to Spark #####
## Create pd_temp
pd_temp = pd.DataFrame(np.random.random(10))

# Create spark_temp from pd_temp
spark_temp = my_spark.createDataFrame(pd_temp)

# Examine the tables in the catalog
print(my_spark.catalog.listTables())

# Add spark_temp to the catalog
spark_temp.createOrReplaceTempView("temp")

# Examine the tables in the catalog again
print(my_spark.catalog.listTables())

##### CSV to Spark DF Directly #####
## Read in the csv
file_path = "/usr/local/share/datasets/airports.csv"

## Read in the airports data
airports = my_spark.read.csv(file_path, header=True)

## Show the data
airports.show()

##### Manipulating Spark DF #####
# Create the DataFrame flights
flights = my_spark.table("flights")

# Show the head
flights.show()

# Add duration_hrs
flights = flights.withColumn("duration_hrs", flights.air_time / 60)


