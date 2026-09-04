

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NeutralJobStatusRunningResultState(enum.StrEnum):
    WAITING = "waiting"

    def visit(self, waiting: typing.Callable[[], T_Result]) -> T_Result:
        if self is NeutralJobStatusRunningResultState.WAITING:
            return waiting()
