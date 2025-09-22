import pandas as pd


class Client:
    def __init__(self, raw_data, output_data):
        self.raw_data_path = raw_data
        self.output_data_path = output_data

    def get_data(self):
        return pd.read_csv(self.raw_data_path)

    def save_data(self, data):
        data.to_csv(self.output_data_path, index=False)
