

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DecisionOutcome(enum.StrEnum):
    GRANTED = "granted"
    DENIED = "denied"
    TAILGATE = "tailgate"

    def visit(
        self,
        granted: typing.Callable[[], T_Result],
        denied: typing.Callable[[], T_Result],
        tailgate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DecisionOutcome.GRANTED:
            return granted()
        if self is DecisionOutcome.DENIED:
            return denied()
        if self is DecisionOutcome.TAILGATE:
            return tailgate()
