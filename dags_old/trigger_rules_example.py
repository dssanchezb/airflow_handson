from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.utils.trigger_rule import TriggerRule

def dummy_function():
    raise Exception

def test():
    print("hola desde python")

default_args = {}

with DAG(
    dag_id="monitoring_trigger",
    description="monitoriando dag",
    schedule_interval="@daily",
    start_date=datetime(2024,1,1),
    end_date=datetime(2024,7,1),
    default_args=default_args,
    max_active_runs=1
) as dag:
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="sleep 10 && echo 'hola desde el bash operator' ",
        trigger_rule=TriggerRule.ALL_SUCCESS,
        retries=2,
        retry_delay=5,
        depends_on_past=True
    )
    task_2 = BashOperator(
        task_id="task_2",
        bash_command="sleep 10 && echo 'HOLA DESDE LA TAREA 2' ",
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALL_SUCCESS,
        depends_on_past=True
    )
    task_3 = PythonOperator(
        task_id="task_3",
        python_callable=test,
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALWAYS,
        depends_on_past=True
    )