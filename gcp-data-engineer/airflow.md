# Apache Airflow

## Orchestration
- DE: ingesting data into the data warehouse to produce datasets for different teams.

## Aifflow
- Apache Airflow is a way to programmatically author, schedule, and monitor (batch) data pipelines.
- Not a data streaming solution neither a data processing framework
- Signle Node Architecture: Web server, Metastore, Scheduler, Executor (Queue).
- A graph that represents a data pipeline with tasks and directed dependencies
    - The scheduler parses for new DAG files every 5 minutes by default.
    - An Operator is a task (describles a single task in a workflow).
- An Executor defines how your tasks are executed, whereas a worker is a process executing your task.
- The Scheduler schedules your tasks, the web server serves the UI, and the database stores the metadata of Airflow.
- Sensor: it's a long running task waiting for an event to happen. A poke function is called every n seconds to check if the criteria are met.
- Celery Executor: allows distributing the execution of task instances to multiple worker nodes.

## DAG Scheduling
- DAG: a collection of all the tasks you want to run, organised in a way that reflects their relationships and dependencies with no cycles.
- `start_date`: the timestamp from which the scheduler will attempt to backfill
- `schedule_interval`: how often a DAG runs (`start_date` + `schedule_time`)
- `end_date`: the timestamp from which a DAG ends
- Monitor tasks with Flower
    - `docker-compose down && docker-compose --profile flower up -d`