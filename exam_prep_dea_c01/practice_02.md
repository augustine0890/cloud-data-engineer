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