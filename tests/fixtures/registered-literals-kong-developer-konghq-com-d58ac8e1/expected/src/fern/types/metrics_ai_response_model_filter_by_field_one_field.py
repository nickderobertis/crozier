

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsAiResponseModelFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    AI_RESPONSE_MODEL = "ai_response_model"

    def visit(self, ai_response_model: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsAiResponseModelFilterByFieldOneField.AI_RESPONSE_MODEL:
            return ai_response_model()
