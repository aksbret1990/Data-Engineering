This project is the implementation of the video below by BharatiDWConsultancy:

https://www.youtube.com/watch?v=Vzaa6meNf_k&list=PLyD1XCIRA3gTRt80JsG782VDx0K7VbKst

This project shows a real time end-to-end data pipleine. We take data that is coming from website clickstream or sensor data and then feed it to kinesis stream. From kinesis streams we process it with kinesis analytics and then feed it to kinesis firehose. Kinesis stream is a real time data acquisition platform. Kinesis analytics has the ability to discover schema and hence enabling SQL queries on it. Then we feed data to Kinesis Firehose which is a data orchestration service which can be used to trasnfer data into S3, Redshift, Elastic Search.
