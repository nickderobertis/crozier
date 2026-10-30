

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DoneFinishReason(enum.StrEnum):
    """
    - `stop`: the model finished the answer.
    - `length`: the answer hit the output token limit.
    """

    STOP = "stop"
    LENGTH = "length"

    def visit(self, stop: typing.Callable[[], T_Result], length: typing.Callable[[], T_Result]) -> T_Result:
        if self is DoneFinishReason.STOP:
            return stop()
        if self is DoneFinishReason.LENGTH:
            return length()
