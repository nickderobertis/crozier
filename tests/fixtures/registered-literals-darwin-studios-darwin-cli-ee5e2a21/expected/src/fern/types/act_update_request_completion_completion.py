

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActUpdateRequestCompletionCompletion(enum.StrEnum):
    YES = "YES"
    PARTIAL = "PARTIAL"
    NO = "NO"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        yes: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
        no: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActUpdateRequestCompletionCompletion.YES:
            return yes()
        if self is ActUpdateRequestCompletionCompletion.PARTIAL:
            return partial()
        if self is ActUpdateRequestCompletionCompletion.NO:
            return no()
        if self is ActUpdateRequestCompletionCompletion.UNKNOWN:
            return unknown()
