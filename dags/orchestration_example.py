from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="my_first_orchestration",
    description="testing the orchestration",
    schedule_interval="@daily",
    start_date=datetime(2024,1,1),
    end_date=datetime(2024,7,14)
) as dag:
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="sleep 2 && echo 'Ejecutando Tarea 1' "
    )

    task_2 = BashOperator(
        task_id="task_2",
        bash_command="sleep 10 && echo 'Ejecutando Tarea 2' "
    )

    task_3 = BashOperator(
        task_id="task_3",
        bash_command="sleep 30 && echo 'Ejecutando Tarea 3' "
    )

    task_1 >> [task_2,task_3]