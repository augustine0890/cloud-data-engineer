# Data Lakes and Lakehouses with Spark and Azure Databricks
## Big Data Ecosystem, Data Lakes, and Spark
- Hadoop incorporate two key components:
    - The Hadoop Distributed File System (or HDFS) provides distributed storage with high-throughput access to data.
    - MapReduce provides a way to conduct massive parallel processing for large amounts of data.
- The major difference between Spark and Hadoop is how they use memory. Hadoop writes intermediate results to disk whereas Spark tries to keep data in memory whenever possible --> makes Spark faster for many use cases.
- Apache Pig: SQL-like language that runs on top of Hadoop MapReduce
- Apace Hive: SQL-like interface that runs on top of Hadoop MapReduce.
- In map reduce, data is organized into (key, value) pairs. The shuffle step finds all of the data across clusters that have the same key. And all of those data points with the same key are brought into the same network node for further processing.
- Hadoop and Spark have led to the development and popularity of data lakes to process large amounts of both structured and unstructured data.
- A data lake, pours all of the data into a single repository, ready to be consumed by whoever and wherever they need.
- The key features of data lakes include:
    -  Lower costs associated with using big data tools for ETL/ELT operations.
    - Data lakes provides schema-on-read rather than schema-on-write which lowers the cost and work of ingesting large amounts of data.
    - Data lakes provides support for structured, semi-structured and unstructured data.
### Lakehouse Architecture
- Lake house seeks to combine the strength of both data lakes and data warehouses.
- The key innovation of the lakehouse architecture is the creation of a metadata and data governance layer on top of the data lake.
    - The creates a pool of raw data as well as a curated set of data.
    - This provides the flexibility and benefits we previously saw with data lakes, and it also provides solutions to the weaknesses in data lakes.
- Lakehouse Features:
    - Raw ingested data can be considered bronze.
    - After some filtering, cleaning, and augmenting, the data can be considered silver.
    - Finally, with the addition of business-level aggregates such as you might see with a star schema, data can be considered gold and ready for analytics and reporting needs.


## Data Wrangling with Spark
## Data Lakes and Azure Databricks