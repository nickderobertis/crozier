

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsAiPluginFilterByFieldValueField(enum.StrEnum):
    """
    The field to filter.
    """

    AI_PLUGIN = "ai_plugin"

    def visit(self, ai_plugin: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsAiPluginFilterByFieldValueField.AI_PLUGIN:
            return ai_plugin()
