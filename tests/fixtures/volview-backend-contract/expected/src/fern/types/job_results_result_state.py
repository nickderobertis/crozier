

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobResultsResultState(enum.StrEnum):
    READY = "ready"
    INCOMPLETE = "incomplete"

    def visit(self, ready: typing.Callable[[], T_Result], incomplete: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobResultsResultState.READY:
            return ready()
        if self is JobResultsResultState.INCOMPLETE:
            return incomplete()
