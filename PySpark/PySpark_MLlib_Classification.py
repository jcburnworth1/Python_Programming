##### Import Libraries #####
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.mllib.recommendation import ALS, Rating ## Ordinary Least Squares
# from pyspark.mllib.classification import LogisticRegressionWithLBFGS ## Logistic Regression
# from pyspark.mllib.clustering import KMeans ## KMeans Clustering

##### Setup Context & Session #####
sc = SparkContext('local', 'spark_app')
spark = SparkSession.builder.getOrCreate()

##### Load the Movies Dataset ####