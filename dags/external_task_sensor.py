from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="external_task_sensor",
    description="Sensor DAG",
    schedule_interval="@daily",
    start_date=datetime(2024,7,1),
    end_date=datetime(2024,7,14)
) as dag:
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="sleep 10 && echo 'hola desde el bash operator' ",
        depends_on_past=True
    )