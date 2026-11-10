

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptOneType(enum.StrEnum):
    TEXT = "text"

    def visit(self, text: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptOneType.TEXT:
            return text()
