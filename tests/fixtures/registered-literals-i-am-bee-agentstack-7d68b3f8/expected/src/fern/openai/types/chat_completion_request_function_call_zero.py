

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionRequestFunctionCallZero(enum.StrEnum):
    NONE = "none"
    AUTO = "auto"

    def visit(self, none: typing.Callable[[], T_Result], auto: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionRequestFunctionCallZero.NONE:
            return none()
        if self is ChatCompletionRequestFunctionCallZero.AUTO:
            return auto()
