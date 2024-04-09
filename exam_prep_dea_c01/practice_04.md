1. Kinesis Data Streams has retry functionality in the event of a processing error.
- Kinesis Data Firehose can transfer the data directly to an S3 bucket, but does not have the necessary retry functionality.
2. Lambda has a maximum run time of 15 minutes.
- AWS Glue can handle large datasets, perform data quality checks and to partition data. Also, supports JDBC connections to many database engines.
- AWS Batch can run ETL jobs on a fleet of EC2 instances that can scale up or down based on data volume and complexity.
3. SQS queues do not push messages. Instead, the message consumers retrieve a message by using the `ReceiveMessage` API.
4. AWS DMS can captures ongoing changes after running initial migration to a supported target data store.
- Full load plus CDC task migrates existing data, and then updates the target based on changes to the source database.
5. The AWS DMS task needs to run constantly run with ongoing replication.
- AWS Glue bookmarks can ensure that only new data is loaded from the tables.
6. DataSync moves large amounts of data online between on-premises and multiple AWS services.
56. Database creator permission in Lake Formation: The allowed permissions on the tables that can create in the database. Also, it can grant permission to other principals in the same AWS account to create tables in the database.
57. Create multiple tables Glue Data Catalog that point to each S3 prefix for each department.
- Lake Formation connects IAM resources to Data Catalog objects
58. AWS KMS can create and manage data encryption keys.
- The modifying an existing cluster to apply encryption after the cluster's creation --> don't need to create a new cluster and copy data.
59. Redshift dynamic data masking supports different levels of masking for different roles. It Also provides complex masking rules based on values in other columns.
60. Maice can only detect sensitive data stored in S3.
- Glue Studio can detect PII from various datasets. Also, it can implement data masking.
- Glue DataBrews can detect and redact PII data. Also can do data masking and supports a variety of file formats.
61. CloudWatch Logs Insights can interactively search and analyze the log data in CloudWatch Logs.
62. UltraWarm storage for OpenSearch provides cost reduction when compared to hot storage.
63. Redshift data sharing allows to live-share data across Redshift clusters without replication data.
- Lake Formation can grant the new Redshift cluster access to only the non-PII columns.
64. S3 Object Look helps prevent objects from being deleted or overwritten. The compliance mode that no users can remove the lock. Not even the root account can remove the lock
65. Redshift dynamic data masking (DDM) is used to mask and protect PII data (not identifies)
- The built-in Detect PII transform method of Glue can choose the PII entities to identify. The method used to scan the data, and how to handle the PII after it has been identified.