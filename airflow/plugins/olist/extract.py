import logging
import requests

BASE_URL = "https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/"

DATASETS = [
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv",
]

#FUNCAO PARA FAZER O DOWNLOAD DE CADA ARQUIVO DENTRO DA VARIAVEL DATASETS
def download_dataset(filename: str) -> str:
    """Baixa um único CSV do repositório da Olist e retorna o conteúdo como texto."""
    url = BASE_URL + filename
    logging.info(f"Baixando {url}")

    response = requests.get(url)
    response.raise_for_status()  # levanta erro se status != 200

    return response.text

#FUNCAO Q CHAMA O DOWNLOAD PASSANDO COMO PARAMETRO O NOME DO ARQUIVO
#GRAVA CADA ARQUIVO EM 1 DATASET
def extract_all_datasets(**kwargs) -> dict:
    """Baixa todos os datasets da Olist e retorna um dicionário {nome_arquivo: conteudo_csv}."""
    datasets = {}

    for filename in DATASETS:
        content = download_dataset(filename)
        datasets[filename] = content
        logging.info(f"{filename}: {len(content)} caracteres baixados")

    return datasets