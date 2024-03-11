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

## Amazon S3
- The S3 Infrequent Access storage class will ensure that data is cost effectively made available for occasional analysis by using SQL with Athena.
  - A lifecycle rule that migrates data to the S3 Glacier Flexible Retrieval storage class will ensure that data is available for compliance evaluation with 12 hours. Configure the lifecycle rule to delete the data after 10 years.

## Redshift
- Redshift data sharing gives you the ability to share live data across Redshift clusters and Redshift Serverless endpoints at no additional cost.
- Redshift Serverless automatically provisions and scales data warehouse capacity to run the test workloads. You pay only for the compute capacity provisioned. There are no compute costs when no workloads are running.
- Redshift materialized views to speed up queries that are predictable and repeated.
  - Runs SQL REFRESH on the materialized view would ensure that the latest data from the current sales table is included in the report.

## Amazon Glue
- AWS Glue DataBrew is a visual data preparation tool that gives you the ability to clean and normalize data without the need to write code. DataBrew provides data masking mechanisms to obfuscate PII data during the data preparation process.
- You need to grant your IAM role permissions that AWS Glue can assume when calling other services on your behalf.
  - Includes access S3 for any sources, targets, scripts, and temporary directories that you use with AWS Glue.
  - Permission is needed by crawlers, jobs, and development endpoint.
- You can use the job run monitoring section of the AWS Glue console to determine the appropriate DPU capacity for this scenario. The job monitoring section of the AWS Glue console use the result of previous job runs to determine the appropriate DPU capacity.

## Amazon SageMaker
- SageMaker ML Lineage Tracking creates and stores information about the steps of an ML workflow.
  - It gives you the ability to establish model governance and audit standards. And helps to ensure that the data being used to run ML decisions is accurate, complete, and trustworthy.

## Amazon Simple Queue Service (SQS)
- AWS SQS is a message queue services. An SQS queue adds a highly available buffer between data producers and consumers.
  - A `DeleteMessage API` call is the typical method to remove message from a queue. A consumer application receives the messages, processes the message, and then tells the queue to delete the message.
  - The `maxReceiveCount` is a property of a queue that indicates how many times a message can be received before the message is deleted and added to a dead-letter queue. If a message is received repeatedly but not deleted, then the issue could originate in the data in the queue rather in the consumers.
  - To purge a queue removes all messages from the queue without the deletion of the queue. You can purge a queue as a troubleshooting step to reset an application.


## Amazon AppFlow
- AWS AppFlow, a flow transfer data between a source and a destination. Amazon AppFlow supports many AWS services and SaaS applications as sources or destinations. A solution that use Amazon AppFlow can continuously send data from the SaaS application to Redshift with least operational overhead. 


## Amazon Macie
- Data security service that discovers sensitive data by using machine learning and pattern matching, provides visibility into data security risks, and enables automated protection against those risks.
- Macie can analyze data in S3 buckets and determine if the data contains sensitive data like PII (personally identifiable information):
  - Macie creates findings based on its analysis. User can view the findings as a report in the AWS Management Console.
  - Macie can also create events that are sent to the default event bus for EventBridge. You can create a rule that filters the findings being generated by Macie. Then, EventBridge can invoke the masking application. This solution meets all requirements and has the lowest operational overhead.

## Amazon Elastic File System (EFS)
- AWS EFS is a scalable file storage service that you can integrate with Lambda or other compute options.
  - Lambda can access the data by using NFS. Additionally, the data is accessible from all concurrently running Lambda functions.

## Some AWS Services and Features
- AWS Identity and Access Management (IAM)
- AWS Key Management Service (AWS KMS)
[Reference](https://docs.aws.amazon.com/)