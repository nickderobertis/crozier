

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobResultsErrorResultsNotReadyResultState(enum.StrEnum):
    WAITING = "waiting"

    def visit(self, waiting: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobResultsErrorResultsNotReadyResultState.WAITING:
            return waiting()
