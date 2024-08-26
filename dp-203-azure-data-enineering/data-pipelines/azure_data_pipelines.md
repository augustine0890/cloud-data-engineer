# Data Pipelines with Azure
- There are two main tools in the Azure cloud platform to create data pipelines:
    - Azure Data Factory
    - Synapse Analytics, referred to as Synapse Pipelines in the Synapse Workspace
- For the final project, there are Azure Cloud Services will be used:
    - Data Factory
    - Azure SQL DB, PostgreSQL DB
    - Blob Storage, and Data Lake Gen2
    - Azure Synapse

## Azure Data Pipeline Components
- Pipeline in Azure Data Factory or Synapse are logical grouping of various activities such as data movement, data transformation and control flow:
    1. Copy data activity is used to load data from on-prem SQL server to Azure Data Lake
    2. Dataflow activity to extract data from Data Lake, transform and load into Synapse
    3. Control Flow activity to iteratively perform the copy data activities or data flow activities.