import numpy as np
import pandas as pd


class Model:
    @staticmethod
    def predict(data: pd.DataFrame) -> pd.DataFrame:
        data = data.copy()
        scores = np.random.normal(loc=0, scale=1, size=data.shape[0])
        data["score"] = scores.round(2)
        return data
