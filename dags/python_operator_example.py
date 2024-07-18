from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

def print_hello():
    print("hola desde python")


with DAG(
    dag_id="python_operator",
    description="using python operator",
    schedule_interval="@once",
    start_date=datetime(2024,7,5)
) as dag:
    t1 = PythonOperator(
                        task_id="hello_from_python",
                        python_callable=print_hello
                      )