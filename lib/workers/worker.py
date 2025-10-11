import pandas as pd

from lib.dto import InputData, ProcessedData, OutputData, OutputRecord, OutputBatch
from lib.processors.processor import Processor
from lib.clients.client import Client
from lib.models.model import Model
from lib.utils import config


class Worker:
    def __init__(self):
        self.config = config
        self.client = Client(self.config.DATABASE_URL)
        self.processor = Processor()
        self.model = Model()

    def start(self) -> None:
        self.client.csv_to_db()
        data = self.client.get_data("input_data")
        results = []
        for _, record in data.iterrows():
            processed_record = self.processor.preprocess(
                InputData(data=str(record["text"]))
            )
            score = self.model.predict(ProcessedData(data=processed_record.data))
            prediction = self.processor.postprocess(OutputData(score=score.score))

            output_record = OutputRecord(
                text=str(record["text"]),
                score=score.score,
                prediction=prediction.prediction,
            )

            results.append(output_record)
        batch = OutputBatch(records=results)
        self.client.save_data(batch, "output_data")
