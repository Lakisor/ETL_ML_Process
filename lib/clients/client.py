import os

import pandas as pd
from sqlalchemy import create_engine
from datasets import load_dataset

from lib.constants.queries import get_data_query
from lib.dto import OutputBatch


class Client:
    def __init__(self, database_url: str, data_path: str = "data/raw/imdb.csv"):
        self.engine = create_engine(database_url)
        self.data_path = data_path

        if not os.path.exists(self.data_path):
            dataset = load_dataset("imdb", split="train[:100]")
            df = pd.DataFrame(dataset)[["text"]]
            os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
            df.to_csv(self.data_path, index=False)

    def csv_to_db(self, table_name: str = "input_data") -> None:
        df = pd.read_csv(self.data_path)
        df.to_sql(table_name, self.engine, if_exists="replace", index=False)

    def get_data(self, table_name: str = "input_data") -> pd.DataFrame:
        query = get_data_query(table_name)
        return pd.read_sql(query, self.engine)

    def save_data(self, batch: OutputBatch, table_name: str = "output_data") -> None:
        df = pd.DataFrame(
            [
                {
                    "text": record.text,
                    "score": record.score,
                    "prediction": record.prediction,
                }
                for record in batch.records
            ]
        )
        df.to_sql(table_name, self.engine, if_exists="replace", index=False)
