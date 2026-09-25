

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PredictionsPredictionsItemPredictionsZeroItemAttentionMapSource(enum.StrEnum):
    LLM = "llm"
    MODEL = "model"

    def visit(self, llm: typing.Callable[[], T_Result], model: typing.Callable[[], T_Result]) -> T_Result:
        if self is PredictionsPredictionsItemPredictionsZeroItemAttentionMapSource.LLM:
            return llm()
        if self is PredictionsPredictionsItemPredictionsZeroItemAttentionMapSource.MODEL:
            return model()
