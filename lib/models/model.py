import pandas as pd
import numpy as np

class Model:
    @staticmethod
    def predict(data):
        data = data.copy()
        scores = np.random.normal(loc=0, scale=1, size=data.shape[0])
        data['score'] = scores.round(2)
        return data