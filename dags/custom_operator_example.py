from airflow import DAG
from datetime import datetime
from helloOperator import HelloOperator

with DAG(
    dag_id="my_first_custom_operator",
    description="my first dag operator",
    start_date=datetime(2024,7,14)
) as dag:
    task_1 = HelloOperator(
        task_id="hello",
        name="Kyra__Morgan"
    )
    task_1