# Core Data Concepts in Azure
## Core Data Concepts and Roles
- [Microsoft Azure Data Fundamentals Certification (DP-900)](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)
    - Relational data, non-relational data, transactional workload, analytical workload
    - 60 exam questions
    - Scenario-based single answer questions, arrange in the correct sequence, drag and drop, mark review.
    - Core data concepts (15-20%), non-relational, and relational data (50-60%), analytics workload (25-30%)
- With the Azure portal, you can build, manage, and monitor everything from simple web apps to complex cloud deployments. Create custom dashboards for an organized view of resources and configure accessibility options for an optimal experience.
- Relational databases typically hold tables represented by rows and columns. Databases that hold tables in this form are called relational databases.
    - Structure data is typically tabular data that is represented by rows and columns in a database.
    - Typically stored in a relational database such as SQL Server or Azure SQL Database
- A key-value store is similar to a relatioinal tables, except that each row can have any number of columns.
- Not all data is structured or even semi-structured.
    - Audio, and video files, and binary data files might not have a specific structure --> unstructured data.
    - It can be stored in Azure Blob storage, Azure Cosmos DB
    - Provisioning: setting-up the database server

- Normalization is the process by which your data is split into a number of well-defined tables, with few columns each, and with references one tables to another.
    - A narrow table is a table with few columns
- A transaction is defined as a sequence of operations that are atomic and the transactional database must adhere to the ACID properties:
    - Transactional systems are often high-volume, sometimes handling many millions of transactions in a single day. The data being processed has to be accessible very quickly. 
    - The work performed by transactional systems is often referred to as Online Transactional Processing (OLTP).
    - Atomicity guarantees that each transaction is treated as a single unit, which either succeeds completely, or fails completely.
    - Consistency ensurses that a transaction can only take the data in the database from one valid state to another.
    - Isolation ensurese the concurrent executioin of transactions leaves the database in the same state that would have been obtained if the transaction were executed sequentially.
    Durability guarantees that once a transaction has been committed, it will be remain commited even if there's system failure such as a power outage or crash.
- Batch processing is suitable for handling large datasets efficiently. Stream processing is intended for individual records or micro-batches consisting of few records.
    - Election counting, production line reporting, and credit card billing.
- Streaming handles data in real-time. Unlike batch processing, there's no waiting until the next batch processing interval, and data processed as individual pieces rather than being processed a batch at a time.
    - Retail purchaisng real-time system, and ride-sharing apps.

- Job roles: database adminsitrator, data engineer, data analyst.
- Database Administrator: manage databases, assign permissions, manage backups, restore data
    - Design, implementation maintenance, and operational aspects.
    - Availability and consistent performance and optimizations
    - Implementation of policies, tools, and processes
    - Security management
    - Installing and upgrading the database server and application tools, enrolling users and maintaining system security, backing up and restoring databases in case of any failures.
    - Tools: SQL Server Management Studio, pgAdmin for PostgreSQL, MySQL Workbench, Azure Data Studio.
    - SQL Server Management Studio: generate Transact-SQL scripts for almost all of functionality that SSMS provides. This gives the DBA the ability to schedule and automate many common tasks.
- Data Engineer:
    - Design and implement data related assets: data ingestion pipelines, transformation activities, and data stores for analytical workloads.
        - Collaborating with stakeholders to design and implement data-related assets that include data ingestion pipelines, cleansing and transformation activities, and data stores for analytical workloads.
    - Apply cleansing routines
    - Identify business rules
    - Turn data into useful information
    - Ensure data privacy, manage and monitor data stores and data pipelines
    - Aligning data architecture and business requirements
    - Indentifying ways to improve data reliability, efficiency, and quality.
    - Conducting research for industry and business questions.
    - Deploying sophisticated analytics programs, machine learning, and statistical methods.
    - Preparing data for predictive and prescriptive modeling and using data to discover tasks that can be automated.
- Data Analyts: enable organizations to make informed decisions
    - Explore and analyze data
    - Create visualizations and charts
    - Enable advanced analytics
    - Finding hidden patterns using data
    - Making large or complex data more accessible, understandable, and usable.
    - Power BI is turn unrelated sources of data into coherent, visually immersive, and interactive insights.
### Microsoft Azure
- Cloud computing is a way to rent compute power and storage from someone else's data center. When you're done using them you give them back your build only for what you use. Instead of maintanining CPUs and storage in your data center, you rent them for the time that you need them.
- Provides computing services over the internet using a pay-as-you-go pricing model.
    - In a consumption-based model, you don’t need to purchase and manage costly infrastructure that they may or may not use to its full capacity.
- Azure runs business applications by providing global scale consistency and seamless integration, with on-premises environments.
- Azure Marketplace that the place you can find, try, buy, and deploy the software and services you need to build new solutions and manage your cloud infrastructure.
    - You can provision end-to-end solutions quickly and reliably, hosted in your own Azure environment.
- Azure Services:
    - Compute Services: virtual machines, serverless, containers.
    - Cloud Storage: disks attached to virtual machines, vault shares or databases.
    - Networking: set-up private network connections on-premises environments, and configure and control traffic into and out of Azure efficiently.
    - App Hosting: run the entire web application on a managed platform in Windows or Linux.
    - Artificial Intelligence: machine learning, prebuilt cognitive services.
    - Internet of Things: integrate sensors and devices and manage them with IoT hubs.
    - Integration: logic apps and services bus connect applications and services and allow for workflows to orchestrate business processes.
    - Security: global security intelligence monitoring. 
- List of [Azure Services](https://azure.microsoft.com/en-us/products)
### Cloud Computing Advantages
- The benefits of cloud computing: high availability, scalability, elasticity, agility, geo-distribution, disaster recovery.
    - With Agility, cloud-based resources can be deployed and configured quickly as your application requirements change.
- With vertical scaling, computing capacity can be increased by additional RAM or CPUs to a virtual machine. You can scale vertically by adding additional virtual machines to your configuration.
- With horizontal scaling, computing capicity can be increased by adding instances of resource.
- Capital expenditure (CapEX) is the upfront spending of money on physical infrastructure and then deducting that upfront expense over time.
- Operational expenditure (OpEX) is where you spend money on products or services and are build for them at the moment of use.
- Lowers your operating costs that you don't have up-front costs.
- Add resources that readily available, according to your needs.
- Pay for additional resources when they are needed or stop paying for resources that are no longer needed.

- [Service Models in Azure](https://learn.microsoft.com/en-us/training/modules/align-requirements-in-azure/) <br>
![Cloud Service Models](/assets/cloud_service_models.png)
- The PaaS cloud service model is a managed hosting environment. In this model the cloud provider manages the vitural machines and networking resources. The cloud tenant deploys their applications into this managed hosting environment.
- The IaaS is the cloud service model that is closest to managing physical servers. In this model the cloud provider keeps the hardware up to date but operating system maintenance and network configuration are left to the cloud tenant.

- Serverless Computing enables developers to build applications faster by eliminating the need for them to manage infrastructure.
- [Private, Public, and Hybrid clouds](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-are-private-public-hybrid-clouds/)

## Concepts of Relational and Non-relational Data
