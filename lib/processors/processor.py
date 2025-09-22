import pandas as pd

class Processor:
    @staticmethod
    def process(data: pd.DataFrame) -> pd.DataFrame:
        data = data.copy()
        data['birthday_dt'] = pd.to_datetime(data['birthday_dt'], format="%Y/%m/%d")
        return data
