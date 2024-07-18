from airflow import DAG
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import pendulum


#definicion estandar de dag usando standar constructor
#my_dag = DAG(dag_id="my_dag_name",start_date=pendulum.datetime(2024,1,1,tz="UTC"),
#             schedule_interval="@daily",catchup=False)

#definicion de DAG utilizando context manager
with DAG(
    dag_id="my_first_dag",
    description="my first dag",
    start_date=datetime(2024,7,1),
    schedule_interval="@once"
) as dag:
    t1 = EmptyOperator(task_id="dummy")
    t1

#definicion de DAG utilizando DAG DECORATOR
#@dag(start_date=pendulum.datetime(2024,1,1,tz="UTC"),
#     schedule_interval="@daily",catchup=False)

#def generate_dag():
#    op = EmptyOperator(task_id="task")

#dag = generate_dag()