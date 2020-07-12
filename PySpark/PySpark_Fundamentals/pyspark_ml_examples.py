## Build a model that predicts whether or not a flight will be delayed based on the flights data we've been working with
##### Import Libraries #####
import numpy as np
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler  ## Setup elements for modeling
from pyspark.ml import Pipeline  ## Combines Estimators & Transformers for a reusable modeling process
from pyspark.ml.classification import LogisticRegression
import pyspark.ml.evaluation as evals  ## Evaluation Module
import pyspark.ml.tuning as tune  ## Tune the model

##### Setup Spark Session #####
## Create my_spark
my_spark = SparkSession.builder.getOrCreate()

## Create the DataFrame flights
flights = my_spark.table("flights")

## Create the DataFrame planes
planes = my_spark.table("planes")

##### Join the data sets #####
# Rename year column
planes = planes.withColumnRenamed("year", "plane_year")

# Join the DataFrames
model_data = flights.join(flights, on="tailnum", how="leftouter")

##### Casting to Integers #####
## Now you'll use the .cast() method you learned in the previous exercise to convert all the appropriate
## columns from your DataFrame model_data to integers! To convert the type of a column using the
## .cast() method, you can write code like this:
## dataframe = dataframe.withColumn("col", dataframe.col.cast("new_type"))

## Cast the columns to integers
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast("integer"))
model_data = model_data.withColumn("air_time", model_data.air_time.cast("integer"))
model_data = model_data.withColumn("month", model_data.month.cast("integer"))
model_data = model_data.withColumn("plane_year", model_data.plane_year.cast("integer"))

## In the last exercise, you converted the column plane_year to an integer. This column holds
## the year each plane was manufactured. However, your model will use the planes' age, which is
## slightly different from the year it was made!
## Create the column plane_age
model_data = model_data.withColumn("plane_age", model_data.year - model_data.plane_year)

## Consider that you're modeling a yes or no question: is the flight late? However, your data contains
## the arrival delay in minutes for each flight. Thus, you'll need to create a boolean column which
## indicates whether the flight was late or not!

# Create is_late
model_data = model_data.withColumn("is_late", model_data.arr_delay > 0)

# Convert to an integer
model_data = model_data.withColumn("label", model_data.is_late.cast("integer"))

# Remove missing values
model_data = model_data.filter(
    "arr_delay is not NULL and dep_delay is not NULL and air_time is not NULL and plane_year is not NULL")

##### Handling Strings #####
## Encode the carrier column for modeling
## Create a StringIndexer
carr_indexer = StringIndexer(inputCol="carrier", outputCol="carrier_index")

## Create a OneHotEncoder
carr_encoder = OneHotEncoder(inputCol="carrier_index", outputCol="carrier_fact")

## Encode the destination column for modeling
# Create a StringIndexer
dest_indexer = StringIndexer(inputCol="dest", outputCol="dest_index")

# Create a OneHotEncoder
dest_encoder = OneHotEncoder(inputCol="dest_index", outputCol="dest_fact")

##### Build the VectorAssembler
## Make a VectorAssembler
vec_assembler = VectorAssembler(inputCols=["month", "air_time", "carrier_fact", "dest_fact", "plane_age"],
                                outputCol="features")

##### Make the pipeline #####
## Make the pipeline
flights_pipe = Pipeline(stages=[dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler])

##### Transform the Data #####
## Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)

##### Transformation Example #####
# +-------+----+-----+---+--------+---------+--------+---------+-------+------+------+----+--------+--------+----+------+----------+--------------------+--------------+-----------+-------+-----+-----+---------+---------+-------+-----+----------+---------------+-------------+--------------+--------------------+
# |tailnum|year|month|day|dep_time|dep_delay|arr_time|arr_delay|carrier|flight|origin|dest|air_time|distance|hour|minute|plane_year|                type|  manufacturer|      model|engines|seats|speed|   engine|plane_age|is_late|label|dest_index|      dest_fact|carrier_index|  carrier_fact|            features|
# +-------+----+-----+---+--------+---------+--------+---------+-------+------+------+----+--------+--------+----+------+----------+--------------------+--------------+-----------+-------+-----+-----+---------+---------+-------+-----+----------+---------------+-------------+--------------+--------------------+
# | N846VA|2014|   12|  8|     658|       -7|     935|       -5|     VX|  1780|   SEA| LAX|     132|     954|   6|    58|      2011|Fixed wing multi ...|        AIRBUS|   A320-214|      2|  182|   NA|Turbo-fan|      3.0|  false|    0|       1.0| (68,[1],[1.0])|          7.0|(10,[7],[1.0])|(81,[0,1,3,77,80]...|
# | N559AS|2014|    1| 22|    1040|        5|    1505|        5|     AS|   851|   SEA| HNL|     360|    2677|  10|    40|      2006|Fixed wing multi ...|        BOEING|    737-890|      2|  149|   NA|Turbo-fan|      8.0|   true|    1|      19.0|(68,[19],[1.0])|          0.0|(10,[0],[1.0])|(81,[0,1,21,70,80...|
# | N847VA|2014|    3|  9|    1443|       -2|    1652|        2|     VX|   755|   SEA| SFO|     111|     679|  14|    43|      2011|Fixed wing multi ...|        AIRBUS|   A320-214|      2|  182|   NA|Turbo-fan|      3.0|   true|    1|       0.0| (68,[0],[1.0])|          7.0|(10,[7],[1.0])|(81,[0,1,2,77,80]...|
# | N360SW|2014|    4|  9|    1705|       45|    1839|       34|     WN|   344|   PDX| SJC|      83|     569|  17|     5|      1992|Fixed wing multi ...|        BOEING|    737-3H4|      2|  149|   NA|Turbo-fan|     22.0|   true|    1|       7.0| (68,[7],[1.0])|          1.0|(10,[1],[1.0])|(81,[0,1,9,71,80]...|
# | N612AS|2014|    3|  9|     754|       -1|    1015|        1|     AS|   522|   SEA| BUR|     127|     937|   7|    54|      1999|Fixed wing multi ...|        BOEING|    737-790|      2|  151|   NA|Turbo-jet|     15.0|   true|    1|      22.0|(68,[22],[1.0])|          0.0|(10,[0],[1.0])|(81,[0,1,24,70,80...|
# | N646SW|2014|    1| 15|    1037|        7|    1352|        2|     WN|    48|   PDX| DEN|     121|     991|  10|    37|      1997|Fixed wing multi ...|        BOEING|    737-3H4|      2|  149|   NA|Turbo-fan|     17.0|   true|    1|       2.0| (68,[2],[1.0])|          1.0|(10,[1],[1.0])|(81,[0,1,4,71,80]...|
# | N422WN|2014|    7|  2|     847|       42|    1041|       51|     WN|  1520|   PDX| OAK|      90|     543|   8|    47|      2002|Fixed wing multi ...|        BOEING|    737-7H4|      2|  140|   NA|Turbo-fan|     12.0|   true|    1|       8.0| (68,[8],[1.0])|          1.0|(10,[1],[1.0])|(81,[0,1,10,71,80...|
# | N361VA|2014|    5| 12|    1655|       -5|    1842|      -18|     VX|   755|   SEA| SFO|      98|     679|  16|    55|      2013|Fixed wing multi ...|        AIRBUS|   A320-214|      2|  182|   NA|Turbo-fan|      1.0|  false|    0|       0.0| (68,[0],[1.0])|          7.0|(10,[7],[1.0])|(81,[0,1,2,77,80]...|
# | N309AS|2014|    4| 19|    1236|       -4|    1508|       -7|     AS|   490|   SEA| SAN|     135|    1050|  12|    36|      2001|Fixed wing multi ...|        BOEING|    737-990|      2|  149|   NA|Turbo-jet|     13.0|  false|    0|      10.0|(68,[10],[1.0])|          0.0|(10,[0],[1.0])|(81,[0,1,12,70,80...|
# | N564AS|2014|   11| 19|    1812|       -3|    2352|       -4|     AS|    26|   SEA| ORD|     198|    1721|  18|    12|      2006|Fixed wing multi ...|        BOEING|    737-890|      2|  149|   NA|Turbo-fan|      8.0|  false|    0|      11.0|(68,[11],[1.0])|          0.0|(10,[0],[1.0])|(81,[0,1,13,70,80...|
# | N323AS|2014|   11|  8|    1653|       -2|    1924|       -1|     AS|   448|   SEA| LAX|     130|     954|  16|    53|      2004|Fixed wing multi ...|        BOEING|    737-990|      2|  149|   NA|Turbo-jet|     10.0|  false|    0|       1.0| (68,[1],[1.0])|          0.0|(10,[0],[1.0])|(81,[0,1,3,70,80]...|
# | N305AS|2014|    8|  3|    1120|        0|    1415|        2|     AS|   656|   SEA| PHX|     154|    1107|  11|    20|      2001|Fixed wing multi ...|        BOEING|    737-990|      2|  149|   NA|Turbo-jet|     13.0|   true|    1|       4.0| (68,[4],[1.0])|          0.0|(10,[0],[1.0])|(81,[0,1,6,70,80]...|
# | N433AS|2014|   10| 30|     811|       21|    1038|       29|     AS|   608|   SEA| LAS|     127|     867|   8|    11|      2013|Fixed wing multi ...|        BOEING|  737-990ER|      2|  222|   NA|Turbo-fan|      1.0|   true|    1|       3.0| (68,[3],[1.0])|          0.0|(10,[0],[1.0])|(81,[0,1,5,70,80]...|
# | N765AS|2014|   11| 12|    2346|       -4|     217|      -28|     AS|   121|   SEA| ANC|     183|    1448|  23|    46|      1992|Fixed wing multi ...|        BOEING|    737-4Q8|      2|  149|   NA|Turbo-fan|     22.0|  false|    0|       5.0| (68,[5],[1.0])|          0.0|(10,[0],[1.0])|(81,[0,1,7,70,80]...|
# | N713AS|2014|   10| 31|    1314|       89|    1544|      111|     AS|   306|   SEA| SFO|     129|     679|  13|    14|      1999|Fixed wing multi ...|        BOEING|    737-490|      2|  149|   NA|Turbo-jet|     15.0|   true|    1|       0.0| (68,[0],[1.0])|          0.0|(10,[0],[1.0])|(81,[0,1,2,70,80]...|
# | N27205|2014|    1| 29|    2009|        3|    2159|        9|     UA|  1458|   PDX| SFO|      90|     550|  20|     9|      2000|Fixed wing multi ...|        BOEING|    737-824|      2|  149|   NA|Turbo-fan|     14.0|   true|    1|       0.0| (68,[0],[1.0])|          4.0|(10,[4],[1.0])|(81,[0,1,2,74,80]...|
# | N626AS|2014|   12| 17|    2015|       50|    2150|       41|     AS|   368|   SEA| SMF|      76|     605|  20|    15|      2001|Fixed wing multi ...|        BOEING|    737-790|      2|  151|   NA|Turbo-jet|     13.0|   true|    1|       9.0| (68,[9],[1.0])|          0.0|(10,[0],[1.0])|(81,[0,1,11,70,80...|
# | N8634A|2014|    8| 11|    1017|       -3|    1613|       -7|     WN|   827|   SEA| MDW|     216|    1733|  10|    17|      2014|Fixed wing multi ...|        BOEING|    737-8H4|      2|  140|   NA|Turbo-fan|      0.0|  false|    0|      30.0|(68,[30],[1.0])|          1.0|(10,[1],[1.0])|(81,[0,1,32,71],[...|
# | N597AS|2014|    1| 13|    2156|       -9|     607|      -15|     AS|    24|   SEA| BOS|     290|    2496|  21|    56|      2008|Fixed wing multi ...|        BOEING|    737-890|      2|  149|   NA|Turbo-fan|      6.0|  false|    0|      24.0|(68,[24],[1.0])|          0.0|(10,[0],[1.0])|(81,[0,1,26,70,80...|
# | N215AG|2014|    6|  5|    1733|      -12|    1945|      -10|     OO|  3488|   PDX| BUR|     111|     817|  17|    33|      2001|Fixed wing multi ...|BOMBARDIER INC|CL-600-2C10|      2|   80|   NA|Turbo-fan|     13.0|  false|    0|      22.0|(68,[22],[1.0])|          2.0|(10,[2],[1.0])|(81,[0,1,24,72,80...|
# +-------+----+-----+---+--------+---------+--------+---------+-------+------+------+----+--------+--------+----+------+----------+--------------------+--------------+-----------+-------+-----+-----+---------+---------+-------+-----+----------+---------------+-------------+--------------+--------------------+
# only showing top 20 rows
#######################################################################################################################

##### Split Into Test & Train #####
# Split the data into training and test sets
training, test = piped_data.randomSplit([.6, .4])

##### Create the Modeler #####
## Create a LogisticRegression Estimator
lr = LogisticRegression()

##### Create the Evaluator #####
## Create a BinaryClassificationEvaluator
evaluator = evals.BinaryClassificationEvaluator(metricName="areaUnderROC")

##### Setup Hyperparameter Tuning #####
## Create the parameter grid
grid = tune.ParamGridBuilder()

## Add the hyperparameter
grid = grid.addGrid(lr.regParam, np.arange(0, .1, .01))
grid = grid.addGrid(lr.elasticNetParam, [0, 1])

## Build the grid
grid = grid.build()

##### Create the Validator #####
## Create the CrossValidator
cv = tune.CrossValidator(estimator=lr,
                         estimatorParamMaps=grid,
                         evaluator=evaluator
                         )

##### Fit the Model #####
#3 Call lr.fit()
best_lr = lr.fit(training)

## Print best_lr
print(best_lr)

##### Evaluate the Model #####
## Use the model to predict the test set
test_results = best_lr.transform(test)

## Evaluate the predictions
print(evaluator.evaluate(test_results))