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