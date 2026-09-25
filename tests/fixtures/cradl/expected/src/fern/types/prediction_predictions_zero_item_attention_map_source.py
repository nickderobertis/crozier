

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PredictionPredictionsZeroItemAttentionMapSource(enum.StrEnum):
    LLM = "llm"
    MODEL = "model"

    def visit(self, llm: typing.Callable[[], T_Result], model: typing.Callable[[], T_Result]) -> T_Result:
        if self is PredictionPredictionsZeroItemAttentionMapSource.LLM:
            return llm()
        if self is PredictionPredictionsZeroItemAttentionMapSource.MODEL:
            return model()
