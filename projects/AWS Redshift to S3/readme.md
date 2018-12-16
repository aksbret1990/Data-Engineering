In this project I took a few tables from the Salesforce schema in Redshift and transfered them to S3 so that these tables can queried on a daily 
basis using AWS athena service and eventually be used for Tableau reporting. Firstly I used psycopg2 library to connect to the Redshift 
and got the names of all salesforce tables. After this I used the create_engine function from sql alchemy library to create a engine which I 
then fed to pandas function read_sql_query to create a data frame. I then converted the dataframe to csv using the df.to_csv function. 
Finally using the boto3 library I dumped the csv file into a S3 bucket.   
