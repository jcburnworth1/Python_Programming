import psycopg2
from configparser import ConfigParser
import numpy as np
import pandas

## Setup our Credentials
## Read the configuration file
config = ConfigParser()
config.read('')

## Setup Redshift Credentials
database = config.get('redshift', 'database')
user = config.get('redshift', 'user')
password = config.get('redshift', 'password')
host = config.get('redshift', 'host')
port = config.get('redshift', 'port')

## Query
query = ""

## Headers
headers = []

## Connection String
conn=psycopg2.connect(dbname= database, host=host, port=port, user=user, password=password)

## Query
cur = conn.cursor()
cur.execute(query)

## Load Data to NumPy Array
redshift_data = np.array(cur.fetchall())

## Close Connection
cur.close()
conn.close()

## Convert to data frame & write to desktop - Mostly for testing purposes
## Comparisions and build of new dataframe for upload will happen lower in this script
redshift_data_frame =  pandas.DataFrame(redshift_data, columns=headers)

## Write to a directory with the below filename
## Add directory location for specific need
redshift__file_name = ""

redshift_data_frame.to_excel(redshift_file_name, index=False)
