from airflow import DAG
from datetime import datetime
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator


from olist.pipeline import extract_load_datasets
from olist.load import DATASETS


dag = DAG(
    'ecommerce_olist',
    schedule =None,
    default_args={
        'owner': 'airflow',
        'retries': 1,
        'start_date': datetime(2023, 1, 1)
    },
    catchup=False,
    tags=["ecommerce","olist"]

)


tasks = []
for nome_arquivo, tabela_destino in DATASETS.items():
    task_id_gerado = "extract_load_" + tabela_destino
    tasks.append(PythonOperator(
        task_id = task_id_gerado,
        python_callable=extract_load_datasets,
        op_kwargs={"filename": nome_arquivo, "destino": tabela_destino},
        dag=dag
    ))


airbyte_task = AirbyteTriggerSyncOperator(
    task_id="airbyte_sync_ecommerce",
    airbyte_conn_id="airbyte_default",
    connection_id="421dda8a-174b-4507-9d21-d29a2d99dc77",
    asynchronous=False,
    dag=dag
)


tasks >> airbyte_task

"""
extract_task = PythonOperator(
    task_id= 'extract',
    python_callable=extract_all_datasets,
    dag=dag

)

load_task = PythonOperator(
    task_id= 'load',
    python_callable=load_all_datasets,
    dag=dag
)


extract_task >> load_task
"""