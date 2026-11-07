

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsAiProviderFilterByFieldValueField(enum.StrEnum):
    """
    The field to filter.
    """

    AI_PROVIDER = "ai_provider"

    def visit(self, ai_provider: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsAiProviderFilterByFieldValueField.AI_PROVIDER:
            return ai_provider()
