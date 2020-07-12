##### Import Libraries #####
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.mllib.clustering import KMeans ## KMeans Clustering

##### Setup Context & Session #####
sc = SparkContext('local', 'spark_app')
spark = SparkSession.builder.getOrCreate()

##### Load the Spam Dataset ####
file_path_spam = 'PySpark/spam.txt'