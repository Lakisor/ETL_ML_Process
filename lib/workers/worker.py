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
        data = self.client.get_data("input_data")
        processed_data = self.processor.process(data)
        scored_data = self.model.predict(processed_data)
        self.client.save_data(scored_data, "output_data")

