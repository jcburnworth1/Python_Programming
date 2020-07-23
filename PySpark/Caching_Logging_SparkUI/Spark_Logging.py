##### Logging Primer #####
# import logging
# import sys
#
# logging.basicConfig(stream=sys.stdout, level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
# logging.info("Hello %s", "world")
# logging.debug("Hello, tage %d", 2)

##### Basic logging #####
import logging

# Log columns of text_df as debug message
logging.debug("text_df columns: %s", text_df.columns)

# Log whether table1 is cached as info message
logging.info("table1 is cached: %s", spark.catalog.isCached(tableName="table1"))

# Log first row of text_df as warning message
logging.warning("The first row of text_df:\n %s", text_df.first())

# Log selected columns of text_df as error message
logging.error("Selected columns: %s", text_df.select("id", "word"))

##### Explaining Query Plans #####
# Run explain on text_df
text_df.explain()

# Run explain on "SELECT COUNT(*) AS count FROM table1"
spark.sql("SELECT COUNT(*) AS count FROM table1").explain()

# Run explain on "SELECT COUNT(DISTINCT word) AS words FROM table1"
spark.sql("SELECT COUNT(DISTINCT word) AS words FROM table1").explain()