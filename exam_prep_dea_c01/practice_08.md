1. Use an AWS Glue DataBrew Recipe to perform the `REMOVE_OUTLIERS` operation
- Glue DataBrew can be used for data sanitization and normalization. Several parameters should be specified when running the operation to remove outliers including the source column, outlier strategy, and threshold.
2. Create an AWS Glue Job with a pushdown predicate specified that filters by date.
- Using a pushdown predicate enables filter data in Glue Data Catalog by a partition. Pushdown predicates do not require the entire dataset to be read, whereas the filter transform does.
- Using SelectsFields would return a DynamicFrame with only the date column. However, the entire record is required so the records can update.
3. The create-table-as-select (CTAS) query is used to create a new based on the output of a SELECT statement.
4. Create a Kinesis Firehose delivery stream to ingest data and output it to an S3 bucket. Configure a Glue crawler that runs on-demand for data discovery. Create a new QuickSight data set that can be directly queried using Athena and create visualization. Once the initial visualization is developed, add another visualization of anomaly insights to the sheet.
- Kinesis Firehouse can deliver streaming data directly to S3, unlike Kinesis Data Streams, which would require an intermediate stage before data output.
- Quicksight has an anomaly insights feature, removing the need to write custom code.
5. Add a new reader instance with a different AZ to the cluster to make it a multi-AZ deployment. Simulate an instance crash using the ALTER SYSTEM CRASH fault injection query and run the failover-db-cluster CLI command for the DB to failover.
6. The reads are exceeding the limits for the shard. To resolve, increase the number of shards in the data stream. Increasing the number of shards also increases the rate at which data flows through the stream.
7. Create Lake Formation personas for data lake administrators, analysts, and their IAM permissions. Label sensitive data in Lake Formation, anonymize raw data using Athena and restrict access to any non-anonymized data for analysts.
- Lake Formation provides access according to user personas in conjunction with IAM permissions. The required personas consist of an IAM administrator, data lake administrator, and workflow role. The data engineer and data analyst personas are optional. Athena support data anonymization using hashing. The data analyst personas should not access non-anonymized data.
8. Use Kinesis Data Streams to capture data. Create a table in the Glue Data Catalog with the Kinesis stream configured as the source. Configure a Glue job using PySpark for transformations with the newly created table as the source. Set the job's data target to create tables in S3.
9. Create a CloudTrail trail with CloudWatch Logs enabled.
- Create a CloudWatch metric filter to select IAM policy change API entries in CloudTrail logs and use the metric filter to create a CloudWatch Alarm.
10. The Amazon Athena Federated Query feature, which supports a variety of datastore, enables data to be queried in place using SQL.
11. Deploy a DynamoDB VPC endpoint in the data analysis application's private subnet, and a DynamoDB VPC endpoint in the public website's public subnet.
- Configure and implement separate VPC endpoint policies for each application.
- DynamoDB VPC endpoints are Gateway endpoints. You can configure multiple gateway endpoints in a single VPC for the same AWS service, and route different resources to different gateways with different policies based on the specific permissions granted to those resources.
12. Use AWS DMS for database replication and write transactions to Amazon S3 as un-partitioned parquet files. Create partitioned and sorted parquet files using an AWS Glue job, and run a crawler to update the Data Catalog. Load the target table using an Amazon Redshift stored procedure.
13. Enable audit logging using the Redshift Console and configure the logging on the associated S3 bucket. Analyze the logs using Redshift Spectrum.
- Amazon Redshift's audit logging feature writes audit logs to S3. Redshift Spectrum can be used to query the S3 data in place.
14. Migrate the high-risk data to new S3 buckets and enable object locks. Configure a retention mode of compliance mode.
15. Create an object lifecycle with a non-current version expiration action. Provide a filter element.
- The specific expiration action is a non-current version expiration action, and a filter element is required to specify how many object versions should be retained.
16. Use the Relationalize transform to change the data format.
- Glue's relationalize transformation can be used to convert data in a DynamicFrame into a relational data format. Once relationalized, the data can be written to an Amazon Redshift cluster form the Glue job using a JDBC connection.
17. Implement Transparent Data Encryption (TDE) for the Amazon RDS for Oracle DB and leverage CloudHSM integration.
- TDE is a service available for Oracle and SQL Server databases. For Oracle, it is integrated with AWS CloudHSM offering, which is a single-tenant Hardware Security Module (HSM) for the AWS cloud.
18. Amazon DynamoDB Encryption Client is a software library that enables you to protect your data in transit and at rest. With DynamoDB Encryption library, you add encryption features to your application and this provides end-to-end protection for your data from its source to its destination in DynamoDB.
- Use Amazon DynamoDB Encryption Client to enable encryption of data in transit.
19. Verify that the VPC's route table includes inbound and outbound routes for the S3 VPC gateway endpoint.
20. Register the S3 bucket as a data lake location in AWS Lake Formation. Use the Lake Formation row-level security features to enforce the company's access policies.
- Lake Formation can control fine-grained permissions at db, table, column, row, cell level.
21. Use API calls to access and integrate third-party datasets from AWS Data Exchange.
22. Use Amazon S3 for data storage. Use Amazon Athena for data analysis.
- Use AWS Lake Formation for centralized data governance and access control.
23. Package the custom Python scripts into Lambda layers. Apply the Lambda layers to the Lambda functions.
24. Create an Athena workgroup for each use case. Apply tags to the workgroup. Create an IAM policy that uses the tags to apply appropriate permissions to the workgroup.
25. Choose the `FLEX` execution class in the Glue job properties.
26. Create an S3 event notification that has an event type of `s3:ObjectCreated:*`. Use a filter rule to generate notifications only when the suffix includes .csv. Set the Amazon Resource Name (ARN) of the Lambda function as the destination for the event notification.
27. Change the data format from .csv to Apache Parquet. Apply Snappy compression.
28. Use Amazon Managed Service for Apache Flink (previously known as Amazon Kinesis Data Analytics) to process the sensor data. Use a connector for Apache Flink to write data to an Amazon Timestream database. Use the Timestream database as a source to create a Grafana dashboard.
29. Create an IAM role that includes the AWSGlueServiceRole policy. Associate the role with the crawler. Specify the S3 bucket path of the source data as the crawler's data store. Create a daily schedule to run the crawler. Specify a database name for the output.
30. Use the Amazon Redshift Data API to publish an event to Amazon EventBridge. Configure an EventBridge rule to invoke the Lambda function.
31. Turn on concurrency scaling at the workload management (WLM) queue level in the Redshift cluster.
32. EMR managed cluster platform that simplifies running big data frameworks e.g., hadoop, spark, hive, oozie, pig etc. → process vast amounts of data.
33. Create a Pipeline in AWS CodePipeline using the default location for the artifact store. Add a source stage and set the provider as the primary CodeCommit repository. Skip the build stage. Add a deployment stage with CloudFormation as the provider and the action as "Create or update a stack." In the Output filename, enter 'outputs.' Use the parameter overrides field to enter the DocumentDB's required information. Edit the deploy stage in the Pipeline to include a deployment action that will create a change set for the previously deployed stack.
34. Use the Detect PII transform in AWS Glue Studio to identify the PII. Create a rule in AWS Glue Data Quality to obfuscate the PII. Use an AWS Step Functions state machine to orchestrate a data pipeline to ingest the data into the S3 data lake.
35. Enable audit logging using the Redshift Console and configure the logging on the associated S3 bucket. Analyze the logs using Redshift Spectrum.
36. A company maintains multiple extract, transform, and load (ETL) workflows that ingest data from the company's operational databases into S3 based data lake. The ETL workflows use Glue and EMR to process data --> use `AWS Glue workflows` for automated orchestration.
37. Transition objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 6 months. Transfer objects to S3 Glacier Flexible Retrieval after 2 years.
38. Set up the sales team BI cluster as a consumer of the ETL cluster by using Redshift data sharing.
39. If you have data in sources other than Amazon S3, you can use Athena Federated Query to query the data in place or build pipelines that extract data from multiple data sources and store them in Amazon S3. With Athena Federated Query, you can run SQL queries across data stored in relational, non-relational, object, and custom data sources.
40. Create an Amazon Managed Streaming for Apache Kafka cluster (Amazon MSK). Create a Amazon Managed Service for Apache Flink application to read from MSK, process the data, and write the output to the data lake.
- MSK is a managed service that reduces the effort required to use Kafka for stream data processing in AWS environment. It integrates with Apache Flink, and together the services can enable a streaming ETL solution.
41. Amazon EMR cluster that runs Spark jobs to perform big data analysis:
- Use Graviton instances for core nodes and task nodes.
- Use Amazon S3 as a persistent data store.
42. Implement Transparent Data Encryption for the Amazon RDS for Oracle DB and leverage CloudHSM integration. <- The information security office has tasked the database specialist with encrypting all DB instances at rest and ensuring the keys are managed on single-tenant hardware.
- TDE is a service available for Oracle and SQL Server databases. For Oracle it is integrated with the AWS CloudHSM offering, which is a single-tenant Hardware Security Module (HSM) for the AWS cloud.
43. Connect Kinesis Data Streams to Amazon Kinesis Data Firehose. Use Kinesis Data Firehose to stage the data in Amazon S3. Use the COPY command to load the data from S3 to a table in Redshift.
44. Partition the data in the S3 bucket. Organize the data by year, month, and day.
- Increase the AWS Glue instance size by scaling up the worker type.
45. Write an AWS Glue extract, transform, and load (ETL) job. Use the FindMatches machine learning (ML) transform to transform the data to perform data deduplication.
46. Amazon Redshift Spectrum to query the data in S3:
- Use a columnar storage file format.
- Partition the data based on the most common query predicates.
47. The company runs an RDS DB instance in a private subnet. The developer needs to allow the Lambda function to connect to the DB instance privately without using the public internet:
- Update the security group of the DB instance to allow only Lambda function invocations on the database port.
- Configure the Lambda function to run in the same subnet that the DB instance uses.
48. Create an AWS Lambda Python function with provisioned concurrency.
49. Create a destination data stream in the security AWS account. Create an IAM role and a trust policy to grant CloudWatch Logs the permission to put data into the stream. Create a subscription filter in the production AWS account.
50. S3 to store semi-structured data in a transactional data lake. The data source sends a full snapshot as a JSON file every data and ingest teh changed data into the data lake:
- Use an open source data lake format to merge the data source with the S3 data lake to insert the new data and update the existing data.
51. The ETL jobs process data from RDS and MongoDB into Redshift. The data updates must occur every hour:
- Configure AWS Glue triggers to run the ETL jobs every hour.
- Use AWS Glue connections to establish connectivity between the data sources and Redshift.
52. Orchestrate a series of Athena queries that will run every day. Each query can run for more than 15 minutes:
- Use an AWS Lambda function and the Athena Boto3 client start query execution API call to invoke the Athena queries programmatically.
- Create an AWS Step Functions workflow and add two states. Add the first state before the Lambda function. Configure the second state as a Wait state to periodically check whether the Athena query has finished using the Athena Boto3 get query execution API call. Configure the workflow to invoke the new query when the current query has finished running.
53. The performance bottleneck is the large number of partitions that are in S3 bucket:
- Create an AWS Glue partition index. Enable partition filtering.
- Use Athena partition projection based on the S3 bucket prefix
54. Use Amazon Managed Service for Apache Flink (Kinesis Data Analytics) to analyze the data by using multiple types of aggregations to perform time-based analytics over a window of up to 30 minutes.
55. EBS General Purpose SSD storage from gp2 to gp3. Prevent any interruption data loss during the migration:
- Change the volume type of the existing gp2 volumes to gp3. Enter new values for volume size, IOPS, and throughput.
56. The company's analytics team must export large date elements every day until the migration is complete. The date elements are the result of SQL joins across multiple tables. The data must be in Parquet format:
- Use a SQL query to create a view in the EC2 instance-based SQL Server databases that contains the required data elements. Create and run an AWS Glue crawler to read the view. Create an AWS Glue job that retrieves the data and transfers the data in Parquet format to S3 bucket. Schedule the Glue job to run every day.
57. `STL_ALERT_EVENT_LOG` table views for record anomalies when a query optimizer identifies conditions that might indicate performance issues.
