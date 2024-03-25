# Exam Prep Standard Course: AWS Certified Data Engineer – Associate (DEA-C01)
Exam Guide: [DEA-C01](https://d1.awsstatic.com/training-and-certification/docs-data-engineer-associate/AWS-Certified-Data-Engineer-Associate_Exam-Guide.pdf)

**Data Engineer Fundamentals**
- Gets data, stores data, and prepares it for consumption by data scientists, analysts.
- Development, implementation, and maintenance of processes and systems that ingest raw data and produce high quality and consistent data to be used for analysis, machine learning.
- DE lifecycle: --> Generation --> Storage --> Ingestion --> Transformation --> Serving (Analytics, Machine Learning, Reverse ETL) -->
- Toolkit: AWS EMR, S3 bucket, Redshift, RDS, Apache Spark
- White papers:
  - [AWS Glue Best Practices](https://docs.aws.amazon.com/whitepapers/latest/aws-glue-best-practices-build-performant-data-pipeline/aws-glue-best-practices-build-performant-data-pipeline.html)
  - [Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.html)
  - [Architectural Patterns to Build End-to-End Data Driven Applications on AWS](https://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/aws-for-data.html)
  - [Modern Data Architecture Rationales on AWS](https://docs.aws.amazon.com/pdfs/whitepapers/latest/modern-data-architecture-rationales-on-aws/modern-data-architecture-rationales-on-aws.pdf)
  - [Data Warehousing on AWS](https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/data-warehousing-on-aws.html)
- FAQs:
  - [Analytics on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/)
  - [Architecture Best Practices for Analytics & Big Data](https://aws.amazon.com/architecture/analytics-big-data/)
  - [Big Data Analytics Options on AWS](https://docs.aws.amazon.com/pdfs/whitepapers/latest/big-data-analytics-options/big-data-analytics-options.pdf)

## Domain 1: Data Ingestion and Transformation
1.1 Perform data ingestion
- Data ingestion: moving data from one place to another
- Data integration: combines data from different sources
- Data ingestion pipelines:
  - Re-process: S3, Kinesis, EventBridge
  - Idempotent
  - Checkpoints
  - Versioning
  - Logging and monitoring
- Producers: DBs, Data stream, Client, Users, Mobile client --> S3 --> Consumers: EC2 instance, RDS, Lambda function
- Transactional data: DynamoDB, RDS, AWS Database Migration Service (DMS)
- Streaming data: Amazon Kinesis Data Firehouse, Data Streams, Video Steams, Data Analytics
  - Amazon Managed Service for Apache Flink (Data Analytics)
- **Kinesis Data Streams**:
  - Each stream is composed of one or more shards that provide a specific amount of capacity. As your workload grows, an application might read or write to a shard at a rate that exceeds its capacity.
  - A partition key strategy can help to take advantage of the provision capacity of Kinesis and avoid hot shards. It's important to monitor you stream metrics and set alarm thresholds to ensure that you have the visibility for your scaling decisions.
  - Solutions:
    - Use `UpdateShardCount` action to scale the stream and increase the number of shards.
    - Use random partition keys to adjust as needed and to distribute the hash key space evenly across shards.
- Amazon MSK: can replace an existing Apache Kafka cluster. Kinesis may be a better option for a new solution because Kinesis is serverless and you only pay for the data throughput. With MSK, you have to pay for the cluster whether you're sending data through it or not.
- Amazon AppFlow: use to ingest data from software as a service and transform and write the data to Amazon S3, Redshift, or write to other SaaS services.
- AWS Transfer Family: file transfer protocol, FTP, and secure file transfer protocol, SFTP directly into Amazon S3 using common file transfer protocols.
- AWS DataSync: data transfer service that simplifies, automates, and accelerates moving data between on-premises storage systems and AWS storage services, as well as between AWS storage services. It also uses common protocols such as NFS and Server Message Block, or SMB.
- AWS Snow Family: extend AWS infrastructure and services into the edge, helping customers run low-latency applications close to where originates, is processed, acted upon.
  - Ingest the large amounts of data
  - Edge compute operations using Snow devices in locations with denied, disconnected, intermittent, or limited network connectivity to AWS.
  - AWS Snowball Edge and AWS Snowcone as an IoT Hub, to run data analytics, to run image analytics and video analytics for content generated at the edge, or to run AI/ML inference at the edge.
- **Batch Data Ingestion**
  - Deal with a larger event payloads and ingesting those on an hourly, daily, or weekly basic using a scheduled job such as a CronJob.
  - AWS EMR provides ways to deploy common Hadoop frameworks and some of the tools can be used for ingesting (Spark, JDBC).
  - AWS Glue can make connections to JDBC sources (many different database engines and through those connections transfer data for further processing)
- Transactional data:
  - Stateful: Amazon ElastiCache, RDS
  - Stateless: Lambda, API Gateway, S3

1.2 Transform and process data
- Query: SQL query issued -- Parsing and conversion to bytecode -- Query planning and optimization -- Query execution -- Results returned
- Data modeling:
  - Online transaction processing (OLTP):
    - Latest state of data
    - Normalization and 3rd normal
    - Optimize for point queries
    - Query latency matters
    - Common Table Expressions (CTEs) can cause latency
  - Online analytical processing (OLAP):
    - Latest state and historical data
    - Normalization can cause slowness
    - Latency not is important
    - Optimize for GROUP BY
    - Use CTEs instead of sub queries
- Transformations: adds unification, integration, add enhancements, which increases value and adds scalability, reliability, and cost optimization.
  - Map data to the correct types
  - Put records in standard format
  - Remove bad data
  - Change the data schema
  - Apply normalization
  - Apply large-scale aggregation
- Raw data is rarely useful: calculated fields, filters, field names, and data types.
- AWS EMR: full-featured, distributed Hadoop environment. Additional frameworks and software
- AWS Glue: fully managed extract, transform, and load (ETL) service. Data cleansing, enrichment, and movement.
- Transformation scenario:
  - Code (Python, Java, Scala) --> Spark App --> EMR --> Config files --> (S3 bucket, Redshift, RDS)
  - IoT Data --> Kinesis Data Firehose --> S3 --> Lambda function
  - EC2 Instance (send the data to firehose) --> Kinesis Data Firehose --> S3 <-- AWS Glue
                       &emsp; &emsp; <br> |--> Amazon Managed for Apache Flink (streaming data analytics) --> Kinesis Firehose --> OpenSearch --> Observability
  - Clothing company stores all historical transactions in an S3 bucket that is integrated with Data Catalog to join the historical transactions with the sales report data:
    - The processing of the data is completed in an Amazon Redshift cluster <-- solution to reduce the workload of the Redshift cluster.
    - Use Redshift SQL to join the tables and Redshift Spectrum to create an external for the historical transaction data in S3.
- Troubleshooting and performance optimization:
  - Identify the following: bottlenecks, high-processing times, memory usage, or higher I/O operations. Algorithms, partition strategy, or parallel processing is needed. Resource allocation. Caching is needed.
  - Check logs, verify data, implement incremental processing, add retries, test.
- AWS Data Services:
  - Glue, EMR: data processing or transformation, cleanse, normalize, and transform the data into a usable format.
  - API Gateway: provides authentication, authorization, rate limiting, caching, and request and response transformation.
  - Lambda: used to process and serve the data for your API.
    - Can write the code to fetch data from data source, apply any additional transformations, and respond to API requests with the formatted data.
    - Can be triggered by API Gateway or other AWS services.
  - Identity and Access Management (IAM): control access and permissions for API Gateway and Lambda functions.
  - AWS Certificate Manage, API keys, OAuth: to secure API endpoints.
  - API Gateway, or ElastiCache: cache responses and reduce latency.
  - AWS CloudWatch: monitor and track the performance, latency, and usage of your data API, configure logging to capture API requests, logs, and errors for troubleshooting and analysis.
  - CodePipeline and CodeBuild: continuous integration and deployment to automate the testing and deployment process.


## Domain 2: Data Store Management
## Domain 3: Data Operations and Support
## Domain 4: Data Security and Governance