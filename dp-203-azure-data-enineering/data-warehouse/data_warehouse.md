# Data Warehouses with Azure
- Schema: the structure of data described in formal way supported by the database management system.
- Data warehouse: a central storage of information that can be queried and used for analysis
    - Optimize data analysis processes and gathers data from multiple sources.
- Operational DBs:
    - Too slow for analytics, too many joins
    - Too hard to understand
- Technical Perspective:
    - Extract the data from the source systems used for operations, transform the data, and load it into a dimensional model.
        - The dimensional model is designed to make it easy for business users to work with the data and improve analytical queries performance.
        - The technologies used for storing dimensional models are different than traditional technologies.
    - Business-user-facing application are needed, with clear visuals (BI) apps.
- Fact tables: columns record events recorded in quantifiable metrics like quantity of an item, duration of the call, a book rating.
- Dimension tables: columns contain attributes like the store at which an item is purchased, or the customer who made the call.

## ELT and Data Warehouse in Cloud
- Data pipeline technologies to move from source to warehouse, as well as between the stages of the Extract, Load, and Transform (ELT) process.
    - The Transform step is often the most costly and by doing it last, DE can perform JUST IN TIME transformations to meet the highest priority business needs first.
    - Data are loaded into the destination using either raw data or staging tables.
    - Also allow DE to quickly and easily ingest the large amounts of data from the transactional systems.
- The three major cloud providers: Azure Synapse, Amazon Redshift, GCP Big Query.

## Azure Data Warehouse
- Data ingestion is often accomplished using blob storage or similar technologies
- Data storage can be accomplished using the warehouse platform - Azure Synapse
- Data analysis can utilize Azure Analysis Services
- Data visualization id made possible using Microsoft Power BI.

**Ingesting Data into Azure Synapse**
- Create Linked Services: a linked service is where you define your connection information to other services.
- Create a pipeline: a pipeline contains the logical flow for an execution of a set of activities
- Use a trigger or a one-time data ingestion: can manually start a data ingestion or you can schedule a trigger.

**SQL to SQL ELT in Azure**
- Start with data ingested into either Blob Storage or Azure Delta Lake Gen2
- Create EXTERNAL staging tables in the Data Warehouse
- Transform data from staging tables to DW tables

## Building Azure Data Warehouse of Bike Share Data Analytics
### Task 1: Create your Azure Resource

### Submission Intructions
- PDF of the star schema you designed based on the relational diagram and the business problems outlined.
- Screenshot of your linked Azure Blob storage showing the 4 datasets copied in from Postgres (Proof of Extract step)
- Copy/paste of the script used for the external table create and load (Proof of Load step). You will have 4 of these, one for each source table.
- SQL code for creating each of the tables (CETAS) per your star schema.
