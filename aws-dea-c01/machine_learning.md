# Machine Learning

## Amazon SageMaker
- A fully managed service that allows data scientists and developers to easily build, train, and deploy machine learning models at scale.
- Provides built-in algorithms that you can immediately use for model training.
- Scenario 1:
  - Extract historical data from the RDS database and the real-time data from Kinesis into an S3 bucket. Use SageMaker to access this data, preprocess it, train the model, and then deploy the model for real-time and batch predictions.
  - It centralizes the data in S3, which can natively access. Preprocessing, training, and deploying within SageMaker ensure a streamlined workflow. Allowing flexibility in handling both real-time and batch processing use cases.
- Scenario 2:
  - Ingest streaming data from Kinesis into SageMaker Feature Store, periodically exporting the features to an S3 bucket. Use SageMaker to train the model on data from this bucket and deploy it for real-time predictions.
  - SageMaker Feature Store to capture and store feature vectors from the streaming data. By periodically aggregating this data to S3, the company can ensure consistent feature engineering for both training and real-time prediction.
## SageMaker Feature Store
- A "feature" is just a property used to train a machine learning model.
- ML models require fast, secure access to feature data for training.
- Kinesis, Kafka Streaming, Spark, Data Wrangler .etc --> SageMaker Feature Store (Online Store -> Offline Store (S3)) --> Model:
  - Streaming access via PutRecord/GetRecord API's
  - Batch access via the offline S3 store (use with anything that hits S3, like Athena, Data Wrangler. Automatically creates a Glue Data Catalog for you.)
- Store feature data in a consistent manner, ensuring that the same features used during model training are available and consistent for real-time predictions. 
## SageMaker ML Lineage Tracking
- Create and store your ML workflow (MLOps)
- Keep a running history of your models
- Tracking for auditing and compliance
- Automatically or manually created tracking entities
## SageMaker Data Wrangler
- Provide end-to-end visibility into the ML workflow, offering a clear trace of how model artifacts were created, what data was used, and which parameters were set during tranining.
- ETL pipeline in SageMaker Studio to prepare data for machine learning.
- Design data flows for importing, cleaning, and transforming data from diverse sources, and then export the prepared data for analysis or training in SageMaker.
