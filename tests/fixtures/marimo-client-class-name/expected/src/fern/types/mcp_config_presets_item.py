

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class McpConfigPresetsItem(enum.StrEnum):
    CONTEXT7 = "context7"
    MARIMO = "marimo"

    def visit(self, context7: typing.Callable[[], T_Result], marimo: typing.Callable[[], T_Result]) -> T_Result:
        if self is McpConfigPresetsItem.CONTEXT7:
            return context7()
        if self is McpConfigPresetsItem.MARIMO:
            return marimo()
