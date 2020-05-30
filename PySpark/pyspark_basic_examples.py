## Spark Reference - http://spark.apache.org/docs/2.1.0/api/python/pyspark.html
##### Import Libraries #####
import pandas as pd
import numpy as np
from pyspark.sql import SparkSession
import pyspark.sql.functions as F ## This submodule contains many useful functions for computing things like standard deviations

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
## Create the DataFrame flights
flights = my_spark.table("flights")

## Show the head
flights.show()

## Add duration_hrs
flights = flights.withColumn("duration_hrs", flights.air_time / 60)

##### Filtering Spark DF #####
## Filter flights by passing a string
long_flights1 = flights.filter("distance > 1000")

## Filter flights by passing a column of boolean values
long_flights2 = flights.filter(flights.distance > 1000)

## Print the data to check they're equal
print(long_flights1.show())
print(long_flights2.show())

##### Selecting Spark DF I #####
## Select the first set of columns
selected1 = flights.select("tailnum","origin","dest")

## Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)

## Define first filter
filterA = flights.origin == "SEA"

## Define second filter
filterB = flights.dest == "PDX"

## Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)

##### Selecting Spark DF II #####
## Define avg_speed
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")

## Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)

## Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")

##### Spark Aggregating Data I #####
## Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()

## Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()

##### Spark Aggregating Data II #####
## Average duration of Delta flights
flights.filter(flights.carrier == "DL").filter(flights.origin == "SEA").groupBy().avg("air_time").show()

## Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()

##### Grouping & Aggregating Data I #####
## Group by tailnum
by_plane = flights.groupBy("tailnum")

## Number of flights each plane made
by_plane.count().show()

## Group by origin
by_origin = flights.groupBy("origin")

## Average duration of flights from PDX and SEA
by_origin.avg("air_time").show()

##### Grouping & Aggregating Data II #####
## Group by month and dest
by_month_dest = flights.groupBy("month","dest")

## Average departure delay by month and destination
by_month_dest.avg().show()

## Standard deviation of departure delay
by_month_dest.agg(F.stddev("dep_delay")).show()

##### Joining Data #####
## Examine the data
print(airports.show())

## Rename the faa column
airports = airports.withColumnRenamed('faa','dest')

## Join the DataFrames
flights_with_airports = flights.join(airports, on='dest', how='leftouter')

## Examine the new DataFrame
print(flights_with_airports.show())