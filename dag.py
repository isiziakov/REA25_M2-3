from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from ultralytics import YOLO

start_date = datetime(2025, 2, 3, 13, 22)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 2, 3, 13, 0),
    'retries': 1,
}

def my_python_function(**kwargs):
    model = YOLO("yolo11n.pt")
    results = model.train(data="/home/c9/Рабочий стол/C9_M3/yolo.yaml", epochs=100)
    with open("res.txt", 'w', encoding='utf-8') as file:
        file.write(f"Время обучения {time / 60}\n")
        file.write(f"Время обучения на эпоху {etime}\n")
        file.write(f"F1_score {res.box.f1}\n")


with DAG(
    dag_id='_m3_dag',
    default_args=default_args,
    schedule_interval='0 15 * * *',  # Каждый день в 18:00
    catchup=True,
) as dag:

    run_my_function = PythonOperator(
        task_id='run_my_python_function',
        python_callable=my_python_function,
        provide_context=True,  # Позволяет передавать контекст задачи в функцию
    )
