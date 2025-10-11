import os
import torch
import pandas as pd
from transformers import BertForSequenceClassification, BertTokenizer

from lib.dto import OutputData, ProcessedData


class Model:
    def __init__(self, model_path="data/bert_model", model_name="bert-base-uncased"):
        if not os.path.exists(model_path):
            os.makedirs(model_path, exist_ok=True)
            BertForSequenceClassification.from_pretrained(model_name).save_pretrained(
                model_path
            )
            BertTokenizer.from_pretrained(model_name).save_pretrained(model_path)

        self.model = BertForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = BertTokenizer.from_pretrained(model_path)
        self.model.eval()

    @torch.no_grad()
    def predict(self, input_data: ProcessedData) -> OutputData:
        inputs = self.tokenizer(
            input_data.data, padding=True, truncation=True, return_tensors="pt"
        )
        outputs = self.model(**inputs)

        score = round(
            torch.nn.functional.softmax(outputs.logits, dim=1)[:, 1].item(), 3
        )

        return OutputData(score=score)
