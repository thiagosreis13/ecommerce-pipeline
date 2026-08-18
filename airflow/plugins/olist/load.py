import pandas as pd
from io import StringIO
from airflow.providers.postgres.hooks.postgres import PostgresHook
import logging

DATASETS = {
    "olist_customers_dataset.csv": "raw_customers",
    "olist_geolocation_dataset.csv": "raw_geolocation",
    "olist_order_items_dataset.csv": "raw_order_items",
    "olist_order_payments_dataset.csv": "raw_order_payments",
    "olist_order_reviews_dataset.csv": "raw_order_reviews",
    "olist_orders_dataset.csv": "raw_orders",
    "olist_products_dataset.csv": "raw_products",
    "olist_sellers_dataset.csv": "raw_sellers",
    "product_category_name_translation.csv": "raw_category_translation",
}

def load_dataset(dados_csv: str, destino: str) -> None:
    csvStringIO = StringIO(dados_csv)
    df = pd.read_csv(
        csvStringIO,
        encoding="utf-8",
    )
    postgres_hook = PostgresHook(postgres_conn_id="postgres_ecommerce", schema="ecommerce")
    engine = postgres_hook.get_sqlalchemy_engine()

    df.to_sql(
        destino,
        con=engine,
        if_exists="replace",
        index=False
    )

def load_all_datasets(**kwargs):
    dados = kwargs['ti'].xcom_pull(task_ids='extract')

    for nome_arquivo, tabela_destino in DATASETS.items():
        load_dataset(dados[nome_arquivo], tabela_destino)