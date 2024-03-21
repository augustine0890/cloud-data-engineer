# AWS Certified Data Engineer Associate (DEA-C01)
- The exam validates a candidate's ability to complete the following tasks:
  - Ingest and transform data, and orchestrate data pipelines while applying programming concepts (Data Ingestion and Transformation).
  - Choose an optimal data store, design data models, catalog data schemas, and manage data lifecycles (Data Store Management).
  - Operational, maintain, and monitor data pipelines. Analyze data and ensure data quality (Data Operations and Support).
  - Implement appropriate authentication, authorization, data encryption, privacy, and governance. Enable logging (Data Security and Governance).


## Amazon Kinesis
- High `IteratorAge` implies that the last record that is read from the Kinesis data stream is increasing in age:
  - It could mean that the data is not being processed in a timely manner.
  - By default, Lambda will create one concurrent instance of the Lambda function for each shard (Kinesis Data Stream)
  - To re-shard is to increase the number of shards for Kinesis Data Streams. If there are more shards, there will be more Lambda function invocations that concurrently process data.
  - One way to increase throughput when you use Kinesis Data Streams and Lambda is to increase the parallelization factor. This solution can cause multiple Lambda function invocation to concurrently process one shard.
- The `ProvisionedThroughputExceededException` is caused by the capacity quotas of the data stream exceeding its provisioned amount. A sustained rise of the stream's output data rate can cause this issue.
  - Increase the number of shards with your stream to provide enough capacity for the read data calls to consistently succeed.
  - Make the Application retry to read data from the stream --> eventually lead to completions of the requests.
- Kinesis Data Firehose to deliver log files to S3 with the least operational overhead.
  - Can use a data-transformation Lambda function with Kinesis Data Firehose --> can convert log files to the correct format before the log files are delivered to S3

## AWS Lake Formation
- Helps centrally govern, secure, and globally share data for analytics and machine learning
- Can manage fine-grained access control for your data lake on Amazon S3 and its metadate in AWS Glue Data Catalog
- You can use Lake Formation to implement security at the database, table, column, row, and cell levels.
  - To implement security at these levels, you can create data filters --> this solution would be reliable and scalable (ensure apply the correct permissions)


## Amazon S3
- The S3 Infrequent Access storage class will ensure that data is cost effectively made available for occasional analysis by using SQL with Athena.
  - A lifecycle rule that migrates data to the S3 Glacier Flexible Retrieval storage class will ensure that data is available for compliance evaluation with 12 hours. Configure the lifecycle rule to delete the data after 10 years.
  - S3 Glacier Flexible Retrival: archives where portions of the data might need to be retrieved in minutes
- S3 Glacier Instant Retrieval: archiving data that is rarely accessed and requires milliseconds retrieval.
- S3 Glacier Deep Archive: archiving data that rarely needs to be accessed. Data stored has a minimum storage duration period of 180 days and a default retrieval time of 12 hours.
- S3 Select: allows retrieval of only a subset of data from an object, using simple SQL expressions. S3 Select improves the performance of applications by retrieving only the needed data from an S3 object.
- Convert the data in S3 to Parquet can reduce the number of bytes that Athena needs to read, which can significantly impact the performance of queries, especially those that do not need to scan entire tables.


## AWS Lambda
- Lambda provides runtimes for Python that run your code to process events.
  - Your code runs in an environment that includes the SDK for Python to access various AWS services, including S3 buckets.

## Redshift
- Fully managed, petabyte-scale data warehouse service in the cloud, allowing users to analyze data using standard SQL and existing BI tools.
- Data Distribution Styles:
  - Even Distribution: Distributes tables rows evenly across all slices and nodes.
  - Key Distribution: Distributes rows based on the values of the specified column.
  - All Distribution: Copies the entire table to every node, beneficial for smaller dimension tables.
- Redshift data sharing gives you the ability to share live data across Redshift clusters and Redshift Serverless endpoints at no additional cost.
- Redshift Serverless automatically provisions and scales data warehouse capacity to run the test workloads. You pay only for the compute capacity provisioned. There are no compute costs when no workloads are running.
- Redshift materialized views to speed up queries that are predictable and repeated.
  - Runs SQL REFRESH on the materialized view would ensure that the latest data from the current sales table is included in the report.
- Redshift's Query Optimizer can utilize the materialized views to deliver faster query performance since data has already been aggregated and stored. Particularly effective for repetitive and predictable query patterns, as it saves the cost of re-running the same join operations with each query.
- Redshift Spectrum resides on dedicated AWS Redshift servers that are independent of your cluster.
  - It pushes many compute-intensive tasks --> predicate filtering and aggregation, down to the Redshift Spectrum layer.
  - It can access and query S3 data from AWS Redshift. (Do not need to keep data over 3 months old in Redshift. Instead, you can unload the data to S3, then use Spectrum for the yearly analysis. S3 Glacier Deep Archive provides the most cost-effective option for long-term data storage). This enables them to perform analysis across their entire datasets (both historical in S3 an real-time in Redshift) using standard SQL
- VACUUM Command: used to reclaim space and resort rows in tables where data has been updated and deleted, optimizing storage efficiency and query performance.
  - In Redshift, when rows are deleted or updated, the old versions of rows are logically marked for deletion but not physically removed. Over time, this can lead to inefficient use of disk space and can degrade query performance. 
- Redshift Data API: enables running SQL queries on data in Redshift asynchronously and retrieving the results through a simple API call (without the need to manage database connections), useful for integrating with web services and AWS Lambda.

## Amazon Glue
- AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy to prepare and load data analytics.
  - Glue is serverless as you only pay for the compute resources consumed while the jobs are running.
- Glue Data Catalog: acts as a centralized metadata repository for all your data assets, regardless of where they are stored. It integrates with Athena, EMR, Redshift Spectrum, and Lake Formation.
  - It provides a persistent metadata store for storing tables definitions, schemas, and other properties.
  - It offers the capability to automatically detect and reflect schema changes.
  - Glue Crawlers can be used to update the schema in the Data Catalog. This updated schema is then automatically available to Athena.
  - Single source of truth for metadata and schema information, facilitating efficient data management and query execution in a dynamic data environment.
  - Provides metadata store that is integrated with AWS EMR, serving as a fully managed Hive metastore compatible with Apache Hive
- AWS Glue DataBrew is a visual data preparation tool that gives you the ability to clean and normalize data without the need to write code. DataBrew provides data masking mechanisms to obfuscate PII data during the data preparation process.
- You need to grant your IAM role permissions that AWS Glue can assume when calling other services on your behalf.
  - Includes access S3 for any sources, targets, scripts, and temporary directories that you use with AWS Glue.
  - Permission is needed by crawlers, jobs, and development endpoint.
- You can use the job run monitoring section of the AWS Glue console to determine the appropriate DPU capacity for this scenario. The job monitoring section of the AWS Glue console use the result of previous job runs to determine the appropriate DPU capacity.
- ETL Jobs: allows to author and orchestrate ETL jobs. These jobs can be triggered on a schedule or in response ot event.
  - Can also set up triggers to call a Lambda function before or after a Glue job runs --> low-management overhead solution for orchestrating tasks that involve both Lambda functions and Glue jobs, as it relies on Glue's native scheduling and dependency resolution features.
- FLEX execution: cost-optimization option for non-critical ETL workloads like:
  - Pre-production data processing
  - Data cleansing and validation for testing purposes.
  - One-time data loads


## Amazon Athena
- An interactive query service that makes it easy to analyze data in S3 using standard SQL. Athena is serverless --> no infrastructure to manage --> pay only for the queries you run
  - Directly works with data stored in S3. It's commonly used for querying log files, click stream data, and other unstructured, semi-structured data.
- Athena's partition projection can help manage many partitions by projecting them into the query results as if they were there, without the need to perform operations on the actual metadata in the Glue Data Catalog --> speeds up query execution time because Athena spends less time reading the partition metadata.


## Amazon SageMaker
- SageMaker ML Lineage Tracking creates and stores information about the steps of an ML workflow.
  - It gives you the ability to establish model governance and audit standards. And helps to ensure that the data being used to run ML decisions is accurate, complete, and trustworthy.

## Amazon Simple Queue Service (SQS)
- AWS SQS is a message queue services. An SQS queue adds a highly available buffer between data producers and consumers.
  - A `DeleteMessage API` call is the typical method to remove message from a queue. A consumer application receives the messages, processes the message, and then tells the queue to delete the message.
  - The `maxReceiveCount` is a property of a queue that indicates how many times a message can be received before the message is deleted and added to a dead-letter queue. If a message is received repeatedly but not deleted, then the issue could originate in the data in the queue rather in the consumers.
  - To purge a queue removes all messages from the queue without the deletion of the queue. You can purge a queue as a troubleshooting step to reset an application.


## Amazon AppFlow
- AWS AppFlow, a flow transfer data between a source and a destination. Amazon AppFlow supports many AWS services and SaaS applications as sources or destinations. A solution that use Amazon AppFlow can continuously send data from the SaaS application to Redshift with the least operational overhead. 
- Ideal for migrating data to AWS, consolidating data from multiple sources for analytics, and keeping SaaS application data synchronized with AWS services


## Amazon Data Exchange
- A service that helps AWS easily share and manage data entitlements from other organizations at scale.
- As a data receiver: you can track and manage all of your data grants and AWS Marketplace data subscriptions in one place.
  - Access third-party data for market research, financial analysis, or customer insights.
- As data senders: eliminates the need to build and maintain any data delivery and entitlement infrastructure.
  - Share your own data (e.g., anonymized customer data) with partners for collaborative analytics.

## Amazon DataSync
- Data transfer service that simplifies, automates, and accelerates moving data between on-premises storage systems and AWS storage services, as well as between storage services.
  - It provides the ability to schedule periodic or one-time sync tasks, handles incremental changes to keep data in sync, and can be used both initial migrations and ongoing replication tasks.
  - The scheduling feature ensures that data is kept up to date after the initial migration with minimal manual intervention, which aligns with the team's requirements for regular, ongoing data transfers.

## Amazon Macie
- Data security service that discovers sensitive data by using machine learning and pattern matching, provides visibility into data security risks, and enables automated protection against those risks.
- Macie can analyze data in S3 buckets and determine if the data contains sensitive data like PII (personally identifiable information):
  - Macie creates findings based on its analysis. User can view the findings as a report in the AWS Management Console.
  - Macie can also create events that are sent to the default event bus for EventBridge. You can create a rule that filters the findings being generated by Macie. Then, EventBridge can invoke the masking application. This solution meets all requirements and has the lowest operational overhead.

## Amazon Elastic File System (EFS)
- AWS EFS is a scalable file storage service that you can integrate with Lambda or other compute options.
  - Lambda can access the data by using NFS. Additionally, the data is accessible from all concurrently running Lambda functions.

## Amazon Elastic Block Store (EBS)
- Provides block-level storage volumes for use with Amazon EC2 instances. EBS volumes are highly available and reliable storage volumes that can be attached to any running instance in the same Availability Zone
- Volume Types: General Purpose (SSD), Provisioned IOPS (SSD), and Magnetic.
- EBS allows to change the volume type of existing volumes with no downtime using the AWS Management Console or the AWS Command Line Interface.

##  Amazon EventBridge Scheduler
- A serverless scheduler that allows you to create, run, and manage tasks from one central, managed service.

## AWS Secrets Manager
- Manage, retrieve, and rotate database credentials, application credentials, OAuth tokens, API keys, and other secrets throughout their lifecycles.
- Rotation is the process of periodically updating a secret. When you rotate a secret, you update the credentials in both the secret and the database or service.

## Some AWS Services and Features
- AWS Identity and Access Management (IAM)
- AWS Key Management Service (AWS KMS)
[Reference](https://docs.aws.amazon.com/)