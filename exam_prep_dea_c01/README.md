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
### Lab: Data Ingestion and Transformation using EMR and Spark
- In this lab, you read data from Amazon Simple Storage Service (S3) and implement data transformation as an Apache Spark job on an Amazon EMR cluster.
- Upload and review the dataset in S3
- Connect to an EMR cluster by using AWS CLI
- Use Spark to process the data.
### Questions
1. You can use AWS DMS to migrate databases or data warehouses to AWS. You can disable Multi-AZ to eliminate the I/O and network activity invlolved in replicating storage blocks from one Availability Zone to another. Therefore, you can preserve underlying storage throughput and the related network bandwidth. This preservation would be useful for the I/O activity related to the data load or data migration.
- Disables or drops all referential integrity constraints during the full load migration will reduce associated overhead. If you enable these constraints during the data load, every child record will be validated with its parent table, thereby saving migration time.
- Disables or drops all table-level triggers (row-level or statement-level triggers) during the full load migration will reduce associated overhead. This solution will prevent triggers from repeatedly activating for every row or multiple rows loaded.
2. EventBridge is a highly scalable, serverless event bus service. You can use EventBridge to build event-driven architectures by using a publish and subscribe model.
- EventBridge supports the integration of various AWS services to create event-driven workflows, including Step Functions. Lambda is a serverless compute service that you can use to run code without the need to provision or manage servers. You can use EventBridge to run data transformations and load the data into the cloud data warehouse. You can combine these services to create a highly scalable, serverless data pipeline that processes data in near real time.
3. A JSON dataset might include nested structures, arrays, and lists. You can use the SUPER data type to store semi-structured data. You can query the SUPER data type by using dots and bracket notations, also known as PartiQL query language.
- [Semi-structured in Redshift](https://docs.aws.amazon.com/redshift/latest/dg/super-overview.html)
4. Athena notebook is a fully managed solution that you can use to query data that is stored in Amazon S3 and other sources. You can register data in Amazon S3 by using Data Catalog. Then, you can query data in Amazon S3 with no additional infrastructure by using Spark and SQL.
- [Spark in Athena](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark.html)
5. Configure the applications to send the log files to Kinesis Data Streams. Install the Kinesis Client Library (KCL) on a group of EC2 instances. Use the EC2 to read the stream records and convert the log files to Parquet and store the Parquet files in S3.
6. Create materialized views in Redshift for aggregated sales. Run queries against the materialized views instead of the sales table.

## Domain 2: Data Store Management
### Lab: Data Store Management that Uses DynamoDB and AWS Glue
- In this lab, you create DynamoDB table by importing data from S3 bucket. You then create a crawler in Glue that detects the schema from DynamoDB and populates the Glue Data Catalog with the metadata. Finally, you create and run Glue job that extracts the data from the DynamoDB table and stores the data in S3.
- [Arizona House Dataset](https://www.kaggle.com/datasets/antoniong203/arizona-houses-2021)
- Import data from S3 to DynamoDB
- Create an AWS Glue crawler
- Create and run an AWS Glue extract, transform, and load (ETL) job that extracts data from DynamoDB and stores the data in an S3 bucket.
- [Adding Glue crawler](https://docs.aws.amazon.com/glue/latest/dg/tutorial-add-crawler.html)
- [Visual ETL with AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/edit-nodes-chapter.html)

### Questions
1. Configures S3 Transfer Acceleration can ensure fast, secure, and private file transfers across long geographic distances.
- S3 Transfer Acceleration uses the globally distributed edge locations of CloudFront. Additionally, it uses AWS backbone networks. You can configure it in S3. This solution is private and is suitable to use with data that constantly changes. This solution effectively minimizes latency calls by distance. Therefore, customers from various locations can experience improved upload and download speeds.
- A solution that uses S3 presigned URLs would allow customers to interact with Amazon S3 in a private way.
2. Unload data that is older than 2 weeks daily to S3 bucket. Delete the data from the Redshift tables. Use Redshift Spectrum for the quarterly queries. Create a lifecycle management policy to delete data from the S3 bucket after 6 months.
- You can unload older, infrequently queried data from Amazon Redshift to Amazon S3 to reduce data storage costs. You can use Redshift Spectrum to run complex queries directly on the data in the S3 bucket. You can use a lifecycle management configuration to delete data that is no longer needed.
3. Glue crawler can automatically populate the Data Catalog with metadata about tables the crawler discovers on S3.
- The incremental crawl feature gives an AWS Glue crawler the ability to crawl only the folders that have been added since the previous crawl. Without this feature, the crawler would re-crawl all the previously cataloged files and folders.
- A solution that specifies a sample size for the crawler allows you to control the number of files in each folder that will be crawled. If you do not specify a sample size, then all the files in the folder will be crawled.
- You can configure crawlers to use S3 events to identify any changes in an S3 location. This solution provides a significantly faster crawler runtime because you no longer need the listing of S3 objects in a specific path. When a crawler runs in event mode, the crawler will consume S3 events from an Amazon Simple Queue Service (Amazon SQS) queue to find any changes that were made to an S3 path.
4. Data Catalog is a metadata catalog. This metadata catalog contains references to data that are used as the source and the targets of extract, transform, and load (ETL) jobs in AWS Glue.
- You can use indexes to improve query performance, especially in scenarios when an AWS Glue table has thousands of partitions. Indexes help reduce the time that it takes to query a table by fetching a subset of partitions rather than loading all partitions in a table. This expression will increase query performance. The expression passes Region and uses supported operators.
5. DynamoDB gives you the ability to create a timestamp for each item as a number attribute. After the time has passed, DynamoDB deletes these unnecessary items without the use of write throughput.
- [DynamoDB TTL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/time-to-live-ttl-before-you-start.html)
6. An Object Lock legal hold prevents an object version from being overwritten or deleted. A legal hold remains in effect until the hold is removed. Legal holds do not have a retention period.
- A deny bucket policy specifies an action that cannot be performed. A deny policy on the bucket would prevent files from being deleted if Delete Action is part of the actions in the policy.
7. The most suitable partition columns are those that are frequently used in queries and have low cardinality. Low cardinality means the columns possess a limited number of distinct values. To partition based on a column with high cardinality would result in an overly fine-grained partitioning scheme, which is generally not efficient. After you identify an appropriate partition column, you should use the column as a filter in queries to reduce the amount of data that Athena scans.
- Parquet is suitable for analytics use cases including Athena. Parquet files are splittable and offer better compression ratios for data on Amazon S3. Parquet files also reduce the I/O necessary to run queries. You can also perform predicate pushdown so that Athena queries will fetch only the blocks needed by the query. A solution that uses Parquet leads to significantly better performance for Athena queries and reduces cost.
### Additional Resources
- [What is cloud storage](https://aws.amazon.com/what-is/cloud-storage/)
- [Storage Best Practices for Data and Analytics Applications](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/building-data-lake-aws.html)
- [Amazon S3 Tutorials](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorials.html)

## Domain 3: Data Operations and Support
### Lab: Analyzing Data by Using Athena
- AnyCompany Consulting wants to analyze Arizona’s real estate because of the current surge of demand for Arizona houses. As a data engineer at AnyCompany, you must use Amazon Athena, a serverless interactive query service, to analyze data on Arizona houses in an Amazon Simple Storage Service (Amazon S3) bucket by using standard SQL.
- In this lab, you create a table in Athena by using the Athena create table form. You then write and run SQL queries to analyze data in Amazon S3 by using Athena.
- Create a table in Athena by using the Athena create a table form.
- Run SQL queries to analyze data in Amazon S3 by using Athena.
- [Adding a Table using a Form](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html#data-sources-glue-manual-table)
- [Aggregate Functions: Count](https://trino.io/docs/current/functions/aggregate.html#count)
### Questions
1. Create an AWS Glue ETL job to convert the input data to Parquet. Create a second Glue ETL job that calculates the aggregated statistics. Use Glue Data Catalog to register both datasets for use with Athena and QuickSight. Build a data pipeline in Amazon MWAA that specifies the Verbose=True parameter. Schedule the directed acyclic graphs (DAGs) to run hourly.
- A solution that catalogs the data that is created by the conversion and calculation job makes these datasets available to both Athena and QuickSight. Amazon MWAA is a managed orchestration service for Apache Airflow that gives you the ability to build data pipelines in the cloud.
- The Verbose=True parameter exposes the AWS Glue logs to Amazon MWAA and provides enhanced observability through the Amazon MWAA dashboard.
2. You can use Athena to directly query data in Amazon S3. Athena is serverless. Therefore, you do not need to select the infrastructure necessary to run the queries for the monthly process. You can use Athena tables and views to query a subset of the data and to combine multiple tables and datasets into one query.
- You can use Redshift Serverless to run analytics workloads without the need to choose and select the necessary infrastructure and compute to run the workloads. You can use Redshift Spectrum in Redshift Serverless to perform analysis on data in Amazon S3 without the need to previously ingest the data in Amazon Redshift.
3. DataBrew is a visual data preparation service designed for data analysts and data scientists. DataBrew has over 350 pre-built data transformations. You can create a profile job in AWS DataBrew to infer the schema of the data with rich insights. Then, you can create a recipe to apply the data transformations. Additionally, you can reuse DataBrew recipes.
- [DataBrew](https://docs.aws.amazon.com/databrew/latest/dg/projects.html)
- [DataBrew and Amazon QuickSight](https://docs.aws.amazon.com/databrew/latest/dg/projects.html)
4. The JVMMemoryPressure error signifies that there is an unbalanced shard allocation across nodes. Therefore, there are too many shards in the cluster.
- When you choose the number of shards, you must distribute an index evenly across all data nodes in the cluster. However, these shards should not be too large or too numerous. A general guideline is to keep shard size between 10–30 GiB for workloads where search latency is a key performance objective. Keep shard size between 30–50 GiB for write-heavy workloads such as log analytics.
- [Choosing the number of shards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sizing-domains.html#bp-sharding)
5.  AWS Batch is a fully managed solution that you can use to run batch computing workloads. AWS Batch can automatically provision compute resources. AWS Batch can manage job priorities by using queue priorities. AWS Batch can run jobs on top of Amazon ECS. Therefore, this solution meets the requirement to use existing containerization skills on the team.
- Step Functions is a serverless state machine service that you can use to orchestrate and coordinate many AWS services including AWS Batch.
- [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/job_scheduling.html)
6. Configure the trail to send the logged events to AWS CloudTrail Lake in an event data store. Query the log data in the data store by using SQL.
- CloudTrail can send logs to CloudTrail Lake without the need to develop a custom solution. CloudTrail Lake automatically converts the JSON event type to Apache ORC format, and stores the data in an event data store. CloudTrail Lake gives you the ability to run SQL queries across multiple event data stores automatically. You can use this solution to analyze the event data automatically.
7. DataBrew can implement data quality rules as part of a ruleset without the need to configure the transient EMR cluster with Apache Spark. Additionally, with DataBrew, you do not need to create a custom job with PyDeequ to perform data quality validations. DataBrew can implement data quality rules as part of a ruleset.
- DataBrew allows you to create a data quality ruleset that automatically performs data quality validations as part of a profiling job. You can use DataBrew in combination with a Step Functions state machine to automate data validation in an ingestion pipeline. 

## Domain 4: Data Security and Governance
### Lab: Managing Amazon S3 Access by Using S3 Access Points and VPC Endpoints
- AnyCompany Consulting uses Amazon Simple Storage Service (Amazon S3) to store shared datasets for their analytics use cases. These datasets are accessed by different applications that run in an Amazon Virtual Private Cloud (Amazon VPC). AnyCompany is also working on their data governance, ensuring both their people and applications only have access to the appropriate data. As a data engineer at AnyCompany, you want to simplify the data access process for the applications. You also want to ensure that the applications that run inside the VPC only have access to specific S3 buckets.
- In this lab, you create an S3 VPC-only access point, a feature of Amazon S3, and then use it in the VPC endpoint policy to manage access to the data in the S3 bucket. You also create bucket policies to firewall S3 bucket access to VPCs only.
- Create a VPC-only access point for the S3 bucket.
- Create an S3 gateway endpoint in the VPC and add a VPC endpoint policy.
- Add a bucket policy to the S3 bucket to only allow access from the VPC.
- [Creating an Access Point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-access-points.html)
- [Gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#create-gateway-endpoint-s3)
- [Control access using bucket policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#bucket-policies-s3)
### Questions
1. Create Glue custom transformation to encrypt columns that contain PII. Load the data into Redshift. Store the encryption key in Secrets Manager. Configure Lambda function to decrypt the columns that contain PII and register a Lambda user-defined functions (UDF). Grant permission to unauthorized users on the UDF.
- You need to implement column-level encryption. Column-level encryption is not a native feature of Amazon Redshift. You can use an AWS Glue custom transformation to encrypt the PII data. A solution that controls access to the encryption key will limit access to authorized users.
- [Redshift UDFs](https://docs.aws.amazon.com/redshift/latest/dg/user-defined-functions.html)
2. The `glue:PutResourcePolicy` action is missing the permission policy that is attached to the role that the data team account uses.
- The error occurs because AWS Glue invokes glue:PutResourcePolicy when the grantee account accepts the resource share invitation. To resolve the issue, allow the glue:PutResourcePolicy action by the assumed role that the grantor account uses.
- [Troubleshooting Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/troubleshooting.html#trouble-cross-account)
3. Use Amazon S3 server-side encryption with AWS KMS keys (SSE-KMS)
- This solution meets the server-side encryption requirement. This solution gives users the ability to manage the object access permissions independently from the encryption keys. The key and the object each have a different policy. A user must be authorized on both policies to be able to perform GetObject and PutObject operations.
- [AWS KMS keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)
4. Enable CloudTrail Lake. Create an event data store and enable logging for all accounts in the company. Run queries on the logs by using the CloudTrail Lake query editor.
- CloudTrail Lake simplifies CloudTrail analysis workflows by integrating collection, storage, preparation, and optimization for analysis and querying in the same product. This solution removes the need to maintain separate data processing pipelines that span across teams and products to analyze CloudTrail events.
- [CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html)
5. Create Redshift datashares for the business units. Grant the appropriate permissions to each businees unit.
- Amazon Redshift datashares provide live access to data that you store in your data warehouse. With this feature, you can securely share live data with Redshift clusters in the same or different AWS accounts. This feature is available within Amazon Redshift. 
- An IAM role is an identity that you can use to provide specific permissions to users, applications, or services. A solution that grants an IAM role is not sufficient to support collaboration without moving the data.
- [Share data in Redshift](https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html)
6. Run a profile job by using AWS Glue DataBrew. Create an AWS Lambda function that reads the profiling job results. If PII is detected, configure the function to run a second DataBrew job that mask any columns that contain PII and sends the data to a results bucket in Amazon S3.
- DataBrew provides data profiling and data masking capabilities that give you the ability to create an automated process to identify and mask PII by using a Step Functions state machine.
7. Use Amazon Macie to identify sensitive data. Use AWS Glue Studio to transform and mask the findings.
- Macie is a fully-managed data security and data privacy service. Macie uses machine learning and pattern matching to help you discover, monitor, and protect sensitive data. AWS Glue Studio can compose data transformations that perform complex tasks including to detect and mass sensitive data. 