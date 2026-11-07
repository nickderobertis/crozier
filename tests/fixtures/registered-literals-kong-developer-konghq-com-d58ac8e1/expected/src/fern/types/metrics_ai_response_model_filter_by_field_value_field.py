

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsAiResponseModelFilterByFieldValueField(enum.StrEnum):
    """
    The field to filter.
    """

    AI_RESPONSE_MODEL = "ai_response_model"

    def visit(self, ai_response_model: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsAiResponseModelFilterByFieldValueField.AI_RESPONSE_MODEL:
            return ai_response_model()
