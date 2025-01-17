from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(
    'dummy_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
) as dag:
    tarefa1 = DummyOperator(task_id='tarefa1')
    tarefa2 = DummyOperator(task_id='tarefa2')
    tarefa3 = DummyOperator(task_id='tarefa3')

    # Definindo dependências
    tarefa1 >> tarefa2 >> tarefa3  # tarefa1 -> tarefa2 -> tarefa3