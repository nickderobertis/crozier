

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TurnStateRunningStatus(enum.StrEnum):
    """
    Turn is still executing.
    """

    RUNNING = "running"

    def visit(self, running: typing.Callable[[], T_Result]) -> T_Result:
        if self is TurnStateRunningStatus.RUNNING:
            return running()
