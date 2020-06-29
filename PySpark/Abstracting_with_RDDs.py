##### Import Libraries #####
from pyspark import SparkContext

## Create my_spark
sc = SparkContext('local', 'Simple App')

# Create an RDD from a list of words
RDD = sc.parallelize(["Spark", "is", "a", "framework", "for", "Big Data processing"])

# Print out the type of the created object
print("The type of RDD is", type(RDD))