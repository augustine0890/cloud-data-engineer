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
