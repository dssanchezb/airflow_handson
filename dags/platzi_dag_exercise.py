from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor

def satellite_get_data_simulation():
    pass

with DAG(
    dag_id="platzi_dag",
    schedule_interval="@once",
    start_date=datetime(2024,7,1)
) as dag:
    task_1 = BashOperator(
        task_id="nasa_simulation",
        bash_command="sleep 20 && echo 'NASA SIMULATION ... ITS OK' > /opt/airflow/fs/response_{{ds_nodash}}.txt "
    )

    task_2 = FileSensor(
        task_id="validate_nasa_notification",
        filepath="/opt/airflow/fs/response_{{ds_nodash}}.txt"
    )

    task_3 = BashOperator(
        task_id="exec_spacex_api",
        bash_command="curl -o /opt/airflow/fs/history.json -L 'https://api.spacexdata.com/v4/history'"
    )

    task_4 = PythonOperator(
        task_id="satellite_simulation",
        python_callable=satellite_get_data_simulation
    )

    task_5 = BashOperator(
        task_id="send_notification",
        bash_command="sleep 20 && echo 'INFORMACIÓN ENVIADA A LAS PERSONAS INTERESADAS!!!' "
    )

    task_1 >> task_2 >> [task_3,task_4] >> task_5