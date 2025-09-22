from lib.processors.processor import Processor
from lib.clients.client import Client
from lib.models.model import Model
from lib.utils import config


class Worker:
    def __init__(self):
        self.config = config
        self.client = Client(self.config.RAW_FILE, self.config.OUTPUT_FILE)
        self.processor = Processor()
        self.model = Model()

    def start(self):
        data = self.client.get_data()
        processed_data = self.processor.process(data)
        scored_data = self.model.predict(processed_data)
        self.client.save_data(scored_data)

