

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptBlockDataNullishContentType(enum.StrEnum):
    COMPLETION = "completion"

    def visit(self, completion: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptBlockDataNullishContentType.COMPLETION:
            return completion()
