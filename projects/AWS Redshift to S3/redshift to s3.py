
# coding: utf-8

# In[2]:


import psycopg2
import psycopg2.extras

conn = psycopg2.connect( dbname='imports', host='', port='', user='', password='')

cursor = conn.cursor()
cursor.execute('select id, name from salesforce.opportunity limit 10')
rows = cursor.fetchall()
for row in rows:
    print(row)


# In[3]:


#actual code
import sys
import io
import boto3
from sqlalchemy import create_engine
import pandas as pd
import psycopg2
import psycopg2.extras


conn = psycopg2.connect( dbname='', host='', port='', user='', password='')
cursor = conn.cursor()
cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'salesforce'""")
rows = cursor.fetchall()
tables = []
for row in rows:
    #print(row)
    tables.append(row[0])
#print(tables)
#tables = ['account_feed', 'opportunity']
#print(tables)

engine = create_engine('postgresql://:@:/imports')
reload(sys)
sys.setdefaultencoding('utf8')
csv_buffer = io.BytesIO()

for table in tables:
    df = pd.read_sql_query("SELECT * FROM salesforce."+ table +" limit 1", engine)
    csv_buffer = io.BytesIO()
    df.to_csv(csv_buffer, index=False)
    s3_resource = boto3.resource('s3',aws_access_key_id='', aws_secret_access_key='')
    s3_resource.Object('redshift-to-s3-st', table+'.csv').put(Body=csv_buffer.getvalue())

