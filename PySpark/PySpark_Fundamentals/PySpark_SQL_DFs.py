##### Import Libraries #####
from pyspark import SparkContext
from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt

##### Setup Context & Session #####
sc = SparkContext('local', 'spark_app')
spark = SparkSession.builder.getOrCreate()

##### Setup the DataFrame from List #####
## Create a list of tuples
sample_list = [('Mona',20), ('Jennifer',34), ('John',20), ('Jim',26)]

## Create a RDD from the list
rdd = sc.parallelize(sample_list)

## Create a PySpark DataFrame
names_df = spark.createDataFrame(rdd, schema=['Name', 'Age'])

## Check the type of names_df
print("The type of names_df is", type(names_df))

##### Setup the DataFrame from File #####
file_path = 'PySpark/PySpark_Fundamentals/people.csv'

## Create an DataFrame from file_path
people_df = spark.read.csv(file_path, header=True, inferSchema=True)

## Check the type of people_df
print("The type of people_df is", type(people_df))

##### Inspect the People Data Frame #####
## Print the first 10 observations
people_df.show(10)

## Count the number of rows
print("There are {} rows in the people_df DataFrame.".format(people_df.count()))

## Count the number of columns and their names
print("There are {} columns in the people_df DataFrame and their names are {}".format(len(people_df.columns), people_df.columns))

##### De-dupe the DataFrame #####
## Select name, sex and date of birth columns
people_df_sub = people_df.select('name', 'sex', 'date of birth')

## Print the first 10 observations from people_df_sub
people_df_sub.show(10)

## Remove duplicate entries from people_df_sub
people_df_sub_nodup = people_df_sub.dropDuplicates()

# Count the number of rows
print("There were {} rows before removing duplicates, and {} rows after removing duplicates".format(people_df_sub.count(), people_df_sub_nodup.count()))

##### Filtering a DataFrame #####
## Filter people_df to select females
people_df_female = people_df.filter(people_df.sex == "female")

## Filter people_df to select males
people_df_male = people_df.filter(people_df.sex == "male")

## Count the number of rows
print("There are {} rows in the people_df_female DataFrame and {} rows in the people_df_male DataFrame".format(people_df_female.count(), people_df_male.count()))

##### Temporary Tables & SQL #####
## Create a temporary table "people"
people_df.createOrReplaceTempView("people")

## Construct a query to select the names of the people from the temporary table "people"
query = '''SELECT name FROM people'''

## Assign the result of Spark's query to people_df_names
people_df_names = spark.sql(query)

## Print the top 10 names of the people
people_df_names.show(10)

##### Filtering with SQL #####
## Filter the people table to select female sex
people_female_df = spark.sql('SELECT * FROM people WHERE sex=="female"')

## Filter the people table DataFrame to select male sex
people_male_df = spark.sql('SELECT * FROM people WHERE sex=="male"')

## Count the number of rows in both DataFrames
print("There are {} rows in the people_female_df and {} rows in the people_male_df DataFrames".format(people_female_df.count(), people_male_df.count()))

##### Plotting in PySpark #####
## Check the column names of names_df
print("The column names of names_df are", names_df.columns)

## Convert to Pandas DataFrame
df_pandas = names_df.toPandas()

# Create a horizontal bar plot
df_pandas.plot(kind='barh', x='Name', y='Age', colormap='winter_r')
plt.show()

##### Plotting from CSV #####
file_path = 'PySpark/PySpark_Fundamentals/Fifa2018_dataset.csv'

## Load the Dataframe
fifa_df = spark.read.csv(file_path, header=True, inferSchema=True)

## Check the schema of columns
fifa_df.printSchema()

## Show the first 10 observations
fifa_df.show(10)

## Print the total number of rows
print("There are {} rows in the fifa_df DataFrame".format(fifa_df.count()))

##### Queries on a DataFrame #####
## Create a temporary view of fifa_df
fifa_df.createOrReplaceTempView('fifa_df_table')

## Construct the "query"
query = '''SELECT age FROM fifa_df_table WHERE nationality == "Germany"'''

## Apply the SQL "query"
fifa_df_germany_age = spark.sql(query)

## Generate basic statistics
fifa_df_germany_age.describe().show()

##### Plot the Result #####
# Convert fifa_df to fifa_df_germany_age_pandas DataFrame
fifa_df_germany_age_pandas = fifa_df_germany_age.toPandas()

# Plot the 'Age' density of Germany Players
fifa_df_germany_age_pandas.plot(kind='density')
plt.show()
