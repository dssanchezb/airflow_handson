from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

with DAG(
    dag_id="file_sensor_example",
    description="file sensor operator",
    schedule_interval="@daily",
    start_date=datetime(2024,7,1)
) as dag:
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="sleep 10 && touch /tmp/file.txt"
    )
    task_2 = FileSensor(
        task_id="waiting_file",
        filepath="/tmp/file.txt"
    )
    task_3 = BashOperator(
        task_id="task_3",
        bash_command="sleep 20 && echo 'EL ARCHIVO EXISTE' "
    )

    task_1 >> task_2 >> task_3