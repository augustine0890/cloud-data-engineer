# Core Data Concepts in Azure
## Core Data Concepts and Roles
- Job roles: database adminsitrator, data engineer, data analyst.
- Database Administrator: manage databases, assign permissions, manage backups, restore data
- Data Engineer: 
    - Apply cleansing routines
    - Identify business rules
    - Turn data into useful informatioin
- Data Analyts: enable organizations to make informed decisions
    - Explore and analyze data
    - Create visualizations and charts
- [Microsoft Azure Data Fundamentals Certification (DP-900)](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)
    - Relational data, non-relational data, transactional workload, analytical workload
    - 60 exam questions
    - Scenario-based single answer questions, arrange in the correct sequence, drag and drop, mark review.
    - Core data concepts (15-20%), non-relational, and relational data (50-60%), analytics workload (25-30%)

- Relational databases typically hold tables represented by rows and columns. Databases that hold tables in this form are called relational databases.
    - Structure data is typically tabular data that is represented by rows and columns in a database.
    - Typically stored in a relational database such as SQL Server or Azure SQL Database
- A key-value store is similar to a relatioinal tables, except that each row can have any number of columns.
- Not all data is structured or even semi-structured.
    - Audio, and video files, and binary data files might not have a specific structure --> unstructured data.
    - It can be stored in Azure Blob storage, Azure Cosmos DB
- Normalization is the process by which your data is split into a number of well-defined tables, with few columns each, and with references one tables to another.
    - A narrow table is a table with few columns
- A transaction is defined as a sequence of operations that are atomic and the transactional database must adhere to the ACID properties:
    - Atomicity guarantees that each transaction is treated as a single unit, which either succeeds completely, or fails completely.
    - Consistency ensurses that a transaction can only take the data in the database from one valid state to another.
    - Isolation ensurese the concurrent executioin of transactions leaves the database in the same state that would have been obtained if the transaction were executed sequentially.
    Durability guarantees that once a transaction has been committed, it will be remain commited even if there's system failure such as a power outage or crash.
- Batch processing is suitable for handling large datasets efficiently. Stream processing is intended for individual records or micro-batches consisting of few records.
    - Election counting, production line reporting, and credit card billing.
- Streaming handles data in real-time. Unlike batch processing, there's no waiting until the next batch processing interval, and data processed as individual pieces rather than being processed a batch at a time.
    - Retail purchaisng real-time system, and ride-sharing apps.

- Provisioning: setting-up the database server


## Concepts of Relational and Non-relational Data
