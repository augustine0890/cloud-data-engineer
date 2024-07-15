# Data Modeling
- Relational databases include a schema of tables that are linked to each other.
- If you need horizontal scalability in your database to improve scalability and performance, it is best to use a non-relational database in that scenario.
- Relational databases are the optimmum choice of databases when you have small amounts of data and when you need to join tables, do aggregations or any type of analysis on the data. They allow for ACID transactions, so if this is important for your business need, stay with relational database.

## PostgreSQL
### Set up a PostgreSQL Docker
1. Install Docker
2. Pull the PostgreSQL docker image:
- `docker pull postgres:latest`
3. Run PostgreSQL docker with specified database
- `docker run --name my-postgres -e POSTGRES_DB=studentdb -e POSTGRES_USER=student -e POSTGRES_PASSWORD=student -d -p 5432:5432 postgres:latest`
- Connect the PostgreSQL container:
    - `docker exec -it my-postgres psql -U student -d studentdb`
### Relational Data Models
- Normalization
    - To reduce data redundancy and increase data integrity
    - Keep relationships between tables together with foreign keys
    - All columns in the table must reply on the Primary Key
    - No transitive dependencies: to get from A to C without going through B. Updating data in just 1 place.
The process of normalization is a step by step process:
    - First Normal Form (1NF)
    - Second Normal Form (2NF)
    - Third Normal Form (3NF)
- Denormalization
    - The process of trying to improve the read performance of a database at the expense of losing some write performance by adding redundant copies of data.
    - Must be done in read heavy workloads to increase performance.
- Fact and Dimension Tables
- Fact table consists of the measurements, metrics or facts of a business process.
- Dimension: a structure that categorizes facts and measures in order to enable users to answer business questions. Dimensions are people, products, place, and time.
- Star Schema: is a type of database schema that is optimized for querying large datasets. It is designed in a denormalized form, which simplifies and speeds up read operations.
- Snowflake Schema: is more normalize form of database schema than a star schema. It involves normalizaing dimension tables into multiple related tables, which can reduce redundancy but increase complexity.

## NoSQL Database (Apache Cassandra)
- NoSQL is better when you have large amounts of data for which you need high availability or if you need to scale out quickly.
- When to use a NoSQL Database:
    - Large amounts of data
    - Need horizontal scalability
    - Need high throughput - fast reads
    - Need a flexible schema
    - Need high availability
    - Need to be able to store different data type formats
    - Users are distributed with low latency
- Apache Cassandra uses its own query language CQL.
- Keyspace: collection of tables (database)
- Table: a group of partitions
- Rows: a single item

### NoSQL Data Models
- In a distributed database, in order to have high availability, you will need copies of your data.
- CAP Theorem:
    - Consistency: every read from the database gets the latest (and correct) piece of data or an error
    - Availability: every request is received and a response is given, without a guarantee that the data is the latest update.
    - Partition tolerance: the system continues to work regardless of losing network connectivity between nodes.
- Data Modeling in Cassandra:
    - Denormalization must be done for fast reads.
    - Always think Queries first
    - One table per query is a great strategy
    - If your business needs calls for ad-hoc queries, these are not strength of Apache Cassandra --> create a new table that will fit your new query.
- Apache Cassandra does not allow for duplicated data in the rows.
- It depends on the data you have and the queries you will run. You may need to combine several columns in the Primary Key to make a Composite Key so that each of the rows are unique.
- The PRIMARY KEY is made up of the partition key and the clustering columns.
    - The clustering column is not required in the primary key. It can be used for ordering the data in the table, but is not required.