

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HiddenReasoningMessageState(enum.StrEnum):
    REDACTED = "redacted"
    OMITTED = "omitted"

    def visit(self, redacted: typing.Callable[[], T_Result], omitted: typing.Callable[[], T_Result]) -> T_Result:
        if self is HiddenReasoningMessageState.REDACTED:
            return redacted()
        if self is HiddenReasoningMessageState.OMITTED:
            return omitted()
