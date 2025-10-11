from typing import List

from pydantic import BaseModel, Field


class InputData(BaseModel):
    data: str = Field(
        ...,
        description="Входные данные для препроцессинга"
    )


class ProcessedData(BaseModel):
    data: str = Field(
        ...,
        description="Входные данные для модели"
    )


class OutputData(BaseModel):
    score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Уверенность модели в предсказании (от 0 до 1)"
    )


class PostprocessedData(BaseModel):
    prediction: int = Field(
        ...,
        description="Предсказанный класс модели (0 или 1)"
    )


class OutputRecord(BaseModel):
    text: str
    score: float
    prediction: int


class OutputBatch(BaseModel):
    records: List[OutputRecord]
