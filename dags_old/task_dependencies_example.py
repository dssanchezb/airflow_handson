#existen dos formas de crear dependencia de tareas:
# 1. utilizando .set_downstream(nombreTarea)
# 2.utilizando bitshift: tarea_1 >> tarea_2 >> tarea_3

#tambien se pueden ejecutar tareas en paralelo
# 1. tarea_1.set_downstream([tarea_2,tarea_3])
# 2. tarea_1 >> [tarea_2,tarea_3
# esto lo que hace es que una vez se ejecute la tarea_1 las tareas 2 y 3 se ejecutaran en paralelo

from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator

def print_hello():
    print("hola desde python")


with DAG(
    dag_id="dependencies",
    description="using python operator",
    schedule_interval="@once",
    start_date=datetime(2024,7,5)
) as dag:
    task_1 = PythonOperator(
                        task_id="task_1",
                        python_callable=print_hello
                      )
    task_2 = BashOperator(
        task_id="task_2",
        bash_command="echo 'hello from bash operator and dependencies dag' "
    )

    task_3 = EmailOperator(
        task_id="task_3",
        to="davidsantiagosanchezb@gmail.com",
        subject="test from airflow",
        html_content='<h3>Este es un correo de prueba enviado desde Airflow.</h3>'

    )

    task_1.set_downstream(task_2)