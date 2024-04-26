1. Ingest .csv format data into S3. Run Athena queries on one or two columns:
- Create a Glue ETL job to read from the .csv structured data source. Configure the job to write the data into the data lake in Parquet format.
2. Each HR department should be able to access records for only employees who are within the HR department's Region:
- Register the S3 path as an AWS Lake Formation location.
- Enable fine-grained access control in AWS Lake Formation. Add a data filter for each Region.
3. The deployed Step Functions state machine is not able to run the EMR jobs:
- Verify that the Step Functions state machine code has all IAM permissions that are necessary to create and run the EMR jobs. Verify that the Step Functions state machine code also includes IAM permissions to access the Amazon S3 buckets that the EMR jobs use. Use Access Analyzer for S3 to check the S3 access properties.
- Query the flow logs for the VPC. Determine whether the traffic that originates from the EMR cluster can successfully reach the data providers. Determine whether any security group that might be attached to the EMR cluster allows connections to the data source servers on the informed ports.
4. Launch new EC2 instance by using an AMI that is backed by a root Amazon Elastic Block Store (EBS) volume that contains the application data. Apply the default settings to the EC2 instance.
5. To use Spark to access Athena:
- Athena workgroup
6. AWS Glue Data Catalog synchronizes with the S3 storage when adds new partitions to the bucket:
- Use code that writes data to Amazon S3 to invoke the Boto3 AWS Glue create_partition API call.
7. Use software as a service (SaaS) applications to gather data by using third-party tools:
- Amazon AppFlow
8. Parquet format in S3 bucket, query only one column of the data:
- Use S3 Select to write a SQL SELECT statement to retrieve the required column from the S3 objects.
9. Automate refresh schedules for Redshift materialized views:
- Use the query editor v2 in Amazon Redshift to refresh the materialized views.
10. Orchestrate a data pipeline that consists of Lambda function and Glue job:
- Use an AWS Step Functions workflow that includes a state machine. Configure the state machine to run the Lambda function and then the AWS Glue job.