

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionPredictionContentParamType(enum.StrEnum):
    CONTENT = "content"

    def visit(self, content: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionPredictionContentParamType.CONTENT:
            return content()
