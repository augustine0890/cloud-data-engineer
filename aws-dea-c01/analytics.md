# Analytics

## AWS Glue

## Amazon Athena
- Serverless interactive queries of S3 data
- Interactive query service for S3 (SQL)
  - No need to load data, it stays in S3
- Supports many data formats:
  - CST, TSV, JSON (human-readable)
  - ORC, Parquet (columnar, splittable)
  - Avro (splittable)
  - Snappy, Zlib, LZO, Gzip compression
- Unstructured, semi-structured, or structured
- Use cases: ad-hoc queries of web logs, query staging data before loading to Redshift, analyze cloudtrail/cloudfront/ELB etc. logs in S3, integration with Jupyter notebooks, integration with QuickSight, integration via JDBC with other visualization tools.
- Athena + Glue:
  - S3 --> AWS Glue --> Athena --> QuickSight
- Pay-as-you-go:
  - $5 per TB scanned
  - Successful or cancelled queries count, failed queries do not.
  - No charge for DDL
  - Save lots of money by using columnar formats.
- Optimizing performance:
  - Use columnar data (ORC, Parquet)
  - Small number of large files performs better than large number of small files
  - Use partitions
- ACID transactions
  - Powered by Apache Iceberg: just add `'table_type' = 'ICEBERG'` in your `CREATE TABLE`
  - Concurrent users can safely make row-level modifications
  - Benefits from periodic compaction to preserve performance.
- Supports federated queries, allowing to run SQL queries across data stored in relational, non-relational, object, and custom data sources. 
- Highly formatted reports and visualization: that's what QuickSight is for
- ETL: use Glue instead

**Apache Spark**
- Distributed processing framework for big data
- In-memory caching, optimized query execution
- Structured Streaming: a constantly growing DataSet
  - Data Stream --> Unbounded Table (data stream as an unbounded Input Table) = new rows appended to input table.
- Spark + Redshift
  - Allows Spark datasets from Redshift (SQL data source)
  - Useful for ETL using Spark
  - S3 --> Redshift --> EMR (Spark) --> Redshift
- Athena for Apache Spark
  - Can run notebooks with Spark within Athena console (encrypted automatically or with KMS)
  - Selectable as an alternate analytics engine (vs. Athena SQL)