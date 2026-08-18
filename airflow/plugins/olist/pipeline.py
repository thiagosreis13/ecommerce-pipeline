from olist.extract import download_dataset
from olist.load import load_dataset


def extract_load_datasets(filename : str, destino : str) -> None: 
    dataset = download_dataset(filename)

    load_dataset(dataset, destino)