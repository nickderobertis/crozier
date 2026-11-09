

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsAiRequestModelFilterByFieldValueField(enum.StrEnum):
    """
    The field to filter.
    """

    AI_REQUEST_MODEL = "ai_request_model"

    def visit(self, ai_request_model: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsAiRequestModelFilterByFieldValueField.AI_REQUEST_MODEL:
            return ai_request_model()
