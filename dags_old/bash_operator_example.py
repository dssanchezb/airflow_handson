from airflow import DAG
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import pendulum

with DAG(
    dag_id="bash_operator",
    description="using bash operator",
    start_date=datetime(2024,7,1)
) as dag:
    t1 = BashOperator(task_id="hello_with_bash_operator",
                      bash_command="curl -o /tmp/archivo_descargado.pdf https://www.hq.nasa.gov/alsj/a17/A17_FlightPlan.pdf")