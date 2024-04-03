1. In Amazon SQS, there are several events can lead to the removal of messages:
- A `DeleteMessage` API call is a direct method to remove a message from the queue, typically after it has processed by a consumer.
- Reaching the `maxReceiveCount` for a message is another way messages are removed. This occurs when a message has been received a specified number of times out but not deleted. The results in the message being sent to a dead-letter queue.
- Performing a purge operation on the queue instantly clears all messages, useful for resetting or troubleshooting the queue.
2. Server-Side Encryption with AWS KMS (SSE-KMS) is feature where AWS manages both the encryption process and the cryptographic keys.
   - Data is automatically encrypted as it is written to S3 and decrypted when accessed, using keys managed in KMS. This process provides an additional layer of security by involving the management of encryption keys.
- AWS Glue DataBrew is a visual data preparation tool that simplifies the process of cleaning and normalizing data. It features data masking capabilities, which are crucial for handling PII.
  - DataBrew can be configured to identify and mask PII, ensuring that sensitive information is obscured or removed from datasets before they rae used in machine learning models or analytics.
3. AWS Cost Explorer is a tool designed to provide a comprehensive view of your AWS costs and usage over time:
   - Custom reporting: gain insights into your spending patterns.
   - Cost optimization: provides visibility into your usage at different levels, which helps you identify opportunities to optimize costs, reducing the usage of underutilized resources.
   - Trend analysis: helps understand fluctuations and plan budgets accordingly.
   - Resource level data: provides cost attribution down to the individual resource level, pinpoint expensive resources consuming the most costs.
4. Amazon Redshifts data sharding provides two powerful capabilities:
   - Read-only access to data across multiple Redshift clusters.
   - Read live data without manually moving or copying data.
- Redshift Serverless is ideal for workloads that are intermittent and short-lived, such as bi-weekly, 2 hours intensive data analysis.
5. Amazon Redshift's Concurrency Scaling feature allows you to automatically add additional cluster capacity to handle an increase in concurrent queries.
- Redshift workload management (WLM) for the long-running query. WLM assigns the query to a queue according to the user's user group or by matching a query group that is listed in the queue configuration with a query group label that the use sets at runtime.
6. With AWS Glue, you only charged an hourly rate based on the number of Data Processing Units (DPU) to run your ETL jobs.
- A Data Processing Unit can also be referred to as a worker, which is the processing power of your ETL job.
- Job bookmarks do not serve the purpose of tracking DPU consumption. Instead, job bookmarks are used to enable Glue jobs to process only new or updated data in subsequent runs by maintaining state information about the data previously processed.
7. Amazon EMR uses an external database to store metadata about the tables, schema, and other Hive data structures.
- Hive metastore is a central repository of Hive metadata. It persists metadata for Hive tables and partitions in a relational database, and provides high availability, and ease of use.
- Hive uses JDBC to connect to the metastore database. Set JDBC configuration values in hive-site.xml. This file specifies the JDBC connection parameters that Hive uses to connect to the metastore databases.
8. The requirements are:
- Regular analytics on the most recent three months of data.
- Periodic queries for quarterly reports, encompassing both historical and recent data.
- The optimal solution: Migrate historical data to Amazon S3. Set up a daily transfer of current data from RDS to Redshift. Use Redshift for regular queries and Redshift Spectrum to join the historical data in S3 with current data.
- Redshift Spectrum would be a more streamlined and cost-effective solution since it can query data directly in S3 without the need for additional data movement.
9. S3 Standard-Infrequent Access is designed for data accessed less frequently but requires rapid access. Query the records in place on S3 using Athena.
- Create a lifecycle rule to migrate the records to S3 Glacier Flexible retrieval after five years. Create another rule to delete the records automatically after 15 years.
10. Glue crawlers automatically detect schemas for data sources. Glue crawlers scan data sources, detect schemas, and store the associated metadata in the Glue Data Catalog. The crawlers run periodically to detect new or changed data.
- Glue jobs can be used to process the data. Glue jobs are defined using Python or Scala scripts that reference the schemas and metadata in the AWS Glue Data Catalog.
11. Amazon Elastic Kubernetes Service (EKS): orchestrates container deployment on nodes, which can be EC2 instances or managed through AWS Fargate. Ephemeral volumes, tied to the pod's lifecycle, can swiftly access the node's local resources like drives or RAM for achieving the lowest latency.
12. Glue DataBrew is a visual data preparation tool that helps data analysts with data preparation tasks such as data profiling, cleaning, and normalizing all without the need to write any code.
- Deequ Spark library is an open-source library built on top of Apache Spark to verify data quality at scale.
13. S3 Glacier storage classes are purposely built for data archiving that provides the highest performance and the lowest cost archive storage in the cloud.
- Create an automated job that loads current data from the data lake to Amazon Redshift. We then use Amazon Redshift for running analytics. 
- Create a job that automatically copies the last three months of data to Amazon Redshift and unloads data older than three months to Amazon S3. Use Amazon Redshift Spectrum to include the 6 months of data for semi-annual analysis.
14. The `UNLOAD` command in Redshift allows unloading the result of query to S3.This command is particularly useful for exporting data that is not frequently accessed, thereby saving storage space in Redshift and reducing costs.
- It supports exporting data in various formats, including CSV, JSON, and Parquet. Parquet is an efficient open columnar storage format for analytics. It is up to 2x faster to unload and consumes up to 6x less storage in Amazon S3 compared to text formats. This makes Parquet a good choice for storing large volumes of infrequently accessed data.