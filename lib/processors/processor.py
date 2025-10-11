import string

import pandas as pd

from lib.dto import InputData, OutputData, ProcessedData, PostprocessedData


class Processor:
    @staticmethod
    def preprocess(input_data: InputData) -> ProcessedData:
        text = input_data.data
        translator = str.maketrans("", "", string.punctuation + "—…«»")
        clean_text = text.translate(translator)
        words = clean_text.split()
        filtered_words = [word for word in words if len(word) >= 2]
        processed_data = " ".join(filtered_words)

        return ProcessedData(data=processed_data)

    @staticmethod
    def postprocess(input_data: OutputData) -> PostprocessedData:
        return PostprocessedData(prediction=(1 if input_data.score >= 0.5 else 0))
