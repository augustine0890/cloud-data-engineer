# Migration and Transfer
## AWS Application Discovery Service
- Plan migration projects by gathering information about on-premises data centers.
- Server utilization data and dependency mapping are important for migrations.
- Agentless Discovery (AWS Agentless Discovery Connector)
  - VM inventory, configuration, and performance history such as CPU, memory, and disk usage.
- Agent-based Discovery (AWS Application Discovery Agent)
  - System configuration, system performance, running processes, and details of the network connections between systems.

## Database Migration Service (DMS)
- Migrate databases to AWS easily and securely. The source or target of the migration must be on AWS.
- Supports:
  - Homogeneous migrations: Oracle to Oracle
  - Heterogeneous migrations: Microsoft SQL Server to Aurora
- Continuous Data Replication using CDC
- The CDC process works by collecting changes to the database logs using the database engine's native API:
  - Full load plus Change data capture (CDC) — the task migrates existing data and then updates the target database based on changes to the source databases.
  - Change data capture (CDC) only — the task migrates ongoing changes after you have data on your target database.
- Have to create an EC2 instance to perform the replication tasks:
  - Source DB --> EC2 instance Running DMS --> Target DB
- AWS Schema Conversion Tool (SCT)
  - Convert your Database's Schema from one engine to another
  - OLTP: SQL Server or Oracle to MySQL, Postgres, Aurora
  - OLAP: Teradata or Oracle to Redshift
  - 