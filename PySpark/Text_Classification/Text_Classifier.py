##### Import Libraries #####
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, length, udf, lit
from pyspark.sql.types import BooleanType, StringType, FloatType, ArrayType
from pyspark.ml.classification import LogisticRegression

##### Setup Context & Session #####
spark = SparkSession.builder.getOrCreate()

##### Read in the Data #####
df_pqt = spark.read.load('PySpark/SparkSQL/sherlock.parquet') ## Parquet version - Not formatted for below yet

##### Practicing Creating a UDF #####
# Returns true if the value is a nonempty vector
nonempty_udf = udf(lambda x:
    True if (x and hasattr(x, "toArray") and x.numNonzeros())
    else False, BooleanType())

# Returns first element of the array as string
s_udf = udf(lambda x: str(x[0]) if (x and type(x) is list and len(x) > 0)
    else '', StringType())

##### Practicing Array Column #####
# Show the rows where doc contains the item '5'
df_before.where(array_contains('doc', '5')).show()

# UDF removes items in TRIVIAL_TOKENS from array
rm_trivial_udf = udf(lambda x:
                     list(set(x) - TRIVIAL_TOKENS) if x
                     else x,
                     ArrayType(StringType()))

# Remove trivial tokens from 'in' and 'out' columns of df2
df_after = df_before.withColumn('in', rm_trivial_udf('in'))\
                    .withColumn('out', rm_trivial_udf('out'))

# Show the rows of df_after where doc contains the item '5'
df_after.where(array_contains('doc','5')).show()

##### Creating a UDF for vector Data #####
# Selects the first element of a vector column
first_udf = udf(lambda x:
            float(x.indices[0])
            if (x and hasattr(x, "toArray") and x.numNonzeros())
            else 0.0,
            FloatType())

# Apply first_udf to the output column
df.select(first_udf("output").alias("result")).show(5)

##### Applying a UDF to vector data #####
# Add label by applying the get_first_udf to output column
df_new = df.withColumn('label', get_first_udf('output'))

# Show the first five rows
df_new.show(5)

##### Transforming text to vector format
# Transform df using model
result = model.transform(df.withColumnRenamed('in', 'words'))\
        .withColumnRenamed('words', 'in')\
        .withColumnRenamed('vec', 'invec')
result.drop('sentence').show(3, False)

# Add a column based on the out column called outvec
result = model.transform(result.withColumnRenamed('out', 'words'))\
        .withColumnRenamed('words', 'out')\
        .withColumnRenamed('vec', 'outvec')
result.select('invec', 'outvec').show(3,False)

##### Label the data #####
# Select the rows where endword is 'him' and label 1
df_pos = df.where("endword = 'him'")\
           .withColumn('label', lit(1))

# Select the rows where endword is not 'him' and label 0
df_neg = df.where("endword <> 'him'")\
           .withColumn('label', lit(0))

# Union pos and neg in equal number
df_examples = df_pos.union(df_neg.limit(df_pos.count()))
print("Number of examples: ", df_examples.count())
df_examples.where("endword <> 'him'").sample(False, .1, 42).show(5)

##### Split the data #####
# Split the examples into train and test, use 80/20 split
df_trainset, df_testset = df_examples.randomSplit((0.80, 0.20), 42)

# Print the number of training examples
print("Number training: ", df_trainset.count())

# Print the number of test examples
print("Number test: ", df_testset.count())

##### Train the classifier #####
# Instantiate logistic setting elasticnet to 0.0
logistic = LogisticRegression(maxIter=100, regParam=0.4, elasticNetParam=0.0)

# Train the logistic classifer on the trainset
df_fitted = logistic.fit(df_trainset)

# Print the number of training iterations
print("Training iterations: ", df_fitted.summary.totalIterations)

##### Evaluate the classifier #####
# Score the model on test data
testSummary = df_fitted.evaluate(df_testset)

# Print the AUC metric
print("\ntest AUC: %.3f" % testSummary.areaUnderROC)

##### Predict the test data #####
# Apply the model to the test data
predictions = df_fitted.transform(df_testset).select(fields)

# Print incorrect if prediction does not match label
for x in predictions.take(8):
    print()
    if x.label != int(x.prediction):
        print("INCORRECT ==> ")
    for y in fields:
        print(y,":", x[y])