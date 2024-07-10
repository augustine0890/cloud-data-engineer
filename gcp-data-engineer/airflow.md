# Apache Airflow
- Apache Airflow is a way to programmatically author, schedule, and monitor (batch) data pipelines.
- Not a data streaming solution neither a data processing framework
- Signle Node Architecture: Web server, Metastore, Scheduler, Executor (Queue).
- A graph that represents a data pipeline with tasks and directed dependencies
    - The scheduler parses for new DAG files every 5 minutes by default.
    - An Operator is a task.
- An Executor defines how your tasks are executed, whereas a worker is a process executing your task.
- The Scheduler schedules your tasks, the web server serves the UI, and the database stores the metadata of Airflow.
## DAG Scheduling
- `start_date`: the timestamp from which the scheduler will attempt to backfill
- 