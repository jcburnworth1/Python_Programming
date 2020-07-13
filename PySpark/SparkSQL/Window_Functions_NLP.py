##### Import Libraries #####
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode

##### Setup Context & Session #####
spark = SparkSession.builder.getOrCreate()

##### Read in the Data #####
df_txt = spark.read.text('PySpark/SparkSQL/sherlock.txt') ## Text version
df_pqt = spark.read.load('PySpark/SparkSQL/sherlock.parquet') ## Parquet version

## Show the first 5 rows
# df.where('id > 70').____(____, truncate=False)
df_pqt.where('id > 70').show(5, truncate=False)

##### Split & Explode a text column #####
## Split the clause column into a column called words
split_df = df_pqt.select(split('word', ' ').alias('words'))
split_df.show(5, truncate=False)

## Explode the words column into a column called word
exploded_df = split_df.select(explode('words').alias('word'))
exploded_df.show(10)

# Count the resulting number of rows in exploded_df
print("\nNumber of rows: ", exploded_df.count())

##### Creating context window feature data #####
##### These do not work with df_pqt
## Word for each row, previous two and subsequent two words
query = """SELECT
           part,
           LAG(word, 2) OVER(PARTITION BY part ORDER BY id) AS w1,
           LAG(word, 1) OVER(PARTITION BY part ORDER BY id) AS w2,
           word AS w3,
           LEAD(word, 1) OVER(PARTITION BY part ORDER BY id) AS w4,
           LEAD(word, 2) OVER(PARTITION BY part ORDER BY id) AS w5
           FROM
           text"""
spark.sql(query).where("part = 12").show(10)

##### Repartitioning #####
## Repartition text_df into 12 partitions on 'chapter' column
repart_df = df_pqt.repartition(numPartitions=12, cols='chapter')

## Prove that repart_df has 12 partitions
repart_df.rdd.getNumPartitions()

##### Finding Common Word Sequences #####
## Find the top 10 sequences of five words
query = """SELECT w1, w2, w3, w4, w5,
           COUNT(*) AS count
           FROM (SELECT
                 word AS w1,
                 LEAD(word,1) OVER(PARTITION BY part ORDER BY id ) AS w2,
                 LEAD(word,2) OVER(PARTITION BY part ORDER BY id ) AS w3,
                 LEAD(word,3) OVER(PARTITION BY part ORDER BY id ) AS w4,
                 LEAD(word,4) OVER(PARTITION BY part ORDER BY id ) AS w5
                 FROM
                 text)
            GROUP BY w1, w2, w3, w4, w5
            ORDER BY count DESC
            LIMIT 10"""
df = spark.sql(query)
df.show()

##### Unique Tuples in sorted order #####
## Unique 5-tuples sorted in descending order
query = """SELECT DISTINCT w1, w2, w3, w4, w5
           FROM (SELECT
                 word AS w1,
                 LEAD(word,1) OVER(PARTITION BY part ORDER BY id ) AS w2,
                 LEAD(word,2) OVER(PARTITION BY part ORDER BY id ) AS w3,
                 LEAD(word,3) OVER(PARTITION BY part ORDER BY id ) AS w4,
                 LEAD(word,4) OVER(PARTITION BY part ORDER BY id ) AS w5
                 FROM
                 text)
           ORDER BY w1 DESC, w2 DESC, w3 DESC, w4 DESC, w5 DESC
           LIMIT 10"""
df = spark.sql(query)
df.show()

##### Most Frequent Tuples #####
## Subquer for later utlization
subquery = """SELECT chapter, w1, w2, w3, COUNT(*) as count
              FROM (SELECT
                    chapter,
                    word AS w1,
                    LEAD(word, 1) OVER(PARTITION BY chapter ORDER BY id ) AS w2,
                    LEAD(word, 2) OVER(PARTITION BY chapter ORDER BY id ) AS w3
                    FROM
                    text)
              GROUP BY
              chapter, w1, w2, w3
              ORDER BY
              chapter, count DESC"""

## Most frequent 3-tuple per chapter
query = """SELECT chapter, w1, w2, w3, count
           FROM (SELECT
                 chapter,
                 ROW_NUMBER() OVER (PARTITION BY chapter ORDER BY count DESC) AS row,
                 w1, w2, w3, count
                 FROM ( %s ))
            WHERE row = 1
            ORDER BY chapter ASC""" % subquery

spark.sql(query).show()