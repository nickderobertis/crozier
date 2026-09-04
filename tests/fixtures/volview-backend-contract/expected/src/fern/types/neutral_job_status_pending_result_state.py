

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NeutralJobStatusPendingResultState(enum.StrEnum):
    WAITING = "waiting"

    def visit(self, waiting: typing.Callable[[], T_Result]) -> T_Result:
        if self is NeutralJobStatusPendingResultState.WAITING:
            return waiting()
