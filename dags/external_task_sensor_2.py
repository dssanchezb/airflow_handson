from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import datetime

with DAG(
    dag_id="external_task_sensor_2",
    description="Sensor DAG",
    schedule_interval="@daily",
    start_date=datetime(2024,7,1),
    end_date=datetime(2024,7,14)
) as dag:
    task_1 = ExternalTaskSensor(
        task_id="waiting_dag",
        external_dag_id="external_task_sensor",
        external_task_id="task_1",
        poke_interval=10
    )

    task_2 = BashOperator(
        task_id="task_2",
        bash_command="sleep 10 && echo 'DAG 2 FINALIZADO!' ",
        depends_on_past=True
    )

    task_1 >> task_2