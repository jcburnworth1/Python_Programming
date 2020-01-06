from suds.client import Client
from suds.wsse import *
from suds.transport.https import HttpAuthenticated
import xml.etree.ElementTree as ET
import datetime
import psycopg2
from configparser import ConfigParser
# import pandas

start_time = datetime.datetime.utcnow()

config = ConfigParser()
config.read('config.conf')

## Headers
headers = [<headers go here>]

## Setup IPS Credentials
username = config.get('ips', 'username')
password = config.get('ips', 'password')
mainWSDL = config.get('ips', 'wsdl')

transport = HttpAuthenticated(username=username, password=password)
client = Client(mainWSDL,transport=transport)
security = Security()
token = UsernameToken(username, password)
security.tokens.append(token)
client.set_options(wsse=security)

# Retrieve Employee Census Report
result = client.service.runReport_ByName(1, [report category], [report name], [saved as name], 'XML')
# Parse the XML
tree = ET.ElementTree(ET.fromstring(result[0]))
body = tree.find('body')
data = []
for child in body:
    data_row = []
    for i in range(0,10):
        data_row.append(child[i].text)
    data_row.append(datetime.datetime.utcnow())
    # data  = [(), (), () ....]
    data_row = tuple(data_row)
    data += (data_row,)
    # print(data)

## To Excel for testing and verfication
# report = pandas.DataFrame(data, columns = headers)
# report.to_excel("testing.xlsx", index=False)

## Setup Redshift Credentials
database = config.get('redshift', 'database')
user = config.get('redshift', 'user')
password = config.get('redshift', 'password')
host = config.get('redshift', 'host')
port = config.get('redshift', 'port')

## Connection String
conn=psycopg2.connect(dbname= database, host=host, port=port, user=user, password=password)

## Clear out the ips_employee_census table for new data
cur = conn.cursor()
cur.execute("TRUNCATE [table]")

# ## Load the current data from IPS
args_str = ','.join(['%s'] * len(data))
insert_query = 'INSERT INTO [table] VALUES {0}'.format(args_str)
cur.execute(insert_query, data)

## Close Connection
cur.close()
conn.close()

end_time = datetime.datetime.utcnow()
print(start_time)
print(end_time)
print(end_time-start_time)
