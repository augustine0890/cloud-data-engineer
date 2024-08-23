# Task 2: Extract Step
- Create the Azure Databricks resource
![azure_databricks_resource](../assets/extract_step_1.png)
- Create Databricks Cluster
![databricks_cluster](../assets/extract_step_2.png)
- Upload the CSV files to DFBS
![csv_DFBS](../assets/extract_step_3.png)
![csv_DFBS](../assets/extract_step_4.png)
- Write the dataset into Bronze store with Delta format.
![databricks_cluster](../assets/extract_step_5.png)
- The Python notebook for extracting data from raw to  Delta file system
    - [extract.ipynb](../notebooks/extract.ipynb)