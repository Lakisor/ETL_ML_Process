import pandas as pd
from sqlalchemy import create_engine


class Client:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)

    def get_data(self, table_name: str = "input_data") -> pd.DataFrame:
        query = f"SELECT * FROM {table_name};"
        return pd.read_sql(query, self.engine)

    def save_data(self, data: pd.DataFrame, table_name: str = "output_data") -> None:
        data.to_sql(table_name, self.engine, if_exists="replace", index=False)
