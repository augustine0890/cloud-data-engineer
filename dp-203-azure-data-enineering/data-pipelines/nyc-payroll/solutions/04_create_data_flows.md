**Create data flow to load 2020 Payroll data from Azure DataLake Gen2 storage to SQL DB**

- Create a new data flow
- Select the dataset for 2020 payroll file as the source
- Click on the + icon at the bottom right of the source, from the options choose sink. A sink will get added in the dataflow
- Select the sink dataset as 2020 payroll table created in SQL db

Repeat the same process to add data flow to load data for each file in Azure DataLake to the corresponding SQL DB tables.