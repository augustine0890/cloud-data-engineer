# Microsoft Azure SQL
## Relational Data Services in Microsoft Azure
- Database Management System (DBMS) handles the physical aspects of a database, such as where and how it's stored, who can access it, and how to ensure that it's available when required.
- Azure virtual machines: still requires DBMS management
- Azure relational data services: manages the DBMS for you
- A virtual network enables to connect virtual machines in Azure services together. It's isolated from other virtual networks created by other users and from the internet.
- IaaS enables to create a virtual infrastructure in the cloud that mirrors the way an on-premises data center might work.
- Azure Data Services fall into the PaaS category. These services are a series of DBMSs managed bu Microsoft in the Cloud.
- The PaaS solution requires the lowest administrative effort and capital expenditure.
- __Microsoft SQL Server__
    - Shift operations to the cloud to take advantage of cloud services.
    - Migrating from the system running on premises to an Azure virtual machine is no different than moving the databases from one on premises server to another.
- __Azure SQL Database__
    - Single database: quickly set up and run a single SQL Server database. Microsoft ensures the privacy of DB. The DB automatically scales and resources are allocated or de-allocated as required.
    - Elastic pool: multiple databases can share the same resources (memory, data storage space, and processing power). This model is useful if you have DBs with resource requirements that vary over time and can help you to reduce costs.
    - Managed instance
- Modern cloud applications that require latest features.
- Applications that require high availability.
- Systems with a variable load for scalability.


## Provisioning, Deploying, and Querying Relational Data in Microsoft Azure
- Compare Data Definition Language (DDL) versus Data Manipulation Language (DML)