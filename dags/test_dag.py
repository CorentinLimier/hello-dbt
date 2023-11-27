"""Example DAG demonstrating the usage of the extraction via Inlets and Outlets."""

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.lineage.entities import Table, File
from airflow.utils.dates import datetime, timedelta


def create_table(cluster, database, name):
    return Table(
        database=database,
        cluster=cluster,
        name=name,
    )

t1 = create_table("c1", "d1", "t1")
t2 = create_table("c1", "d1", "t2")
t3 = create_table("c1", "d1", "t3")
t4 = create_table("c1", "d1", "t4")
f1 = File(url = "http://randomfile")

dag = DAG(
    'manuallineage',
    start_date=datetime(2020, 12, 23),
    description='A dbt wrapper for airflow',
    schedule_interval=timedelta(days=1),
    catchup=False
)

task1 = BashOperator(
    task_id='task1',
    bash_command='echo "{{ task_instance_key_str }}" && sleep 1',
    inlets=[t1, t2],
    outlets=[t3],
    dag=dag,
)

task2 = BashOperator(
    task_id='task2',
    bash_command='echo "{{ task_instance_key_str }}" && sleep 1',
    inlets=[t3, f1],
    outlets=[t4],
    dag=dag,
)

task1 >> task2
